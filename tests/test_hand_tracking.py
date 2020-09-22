import threading

import grpc

from proto.mediapipe.framework.formats import landmark_pb2
from proto.qoin.proto import hand_tracking_pb2_grpc, hand_tracking_pb2
from tests import ServerTestCase


class TestHandTracking(ServerTestCase):
    def test_bypass(self):
        stub = hand_tracking_pb2_grpc.HandTrackingStub(self.channel)
        should_send = False

        def push():
            def request_generator():
                while True:
                    if should_send:
                        landmarks = [landmark_pb2.NormalizedLandmark(x=0, y=0, z=0)]
                        landmark_list = landmark_pb2.NormalizedLandmarkList(landmark=landmarks)
                        yield hand_tracking_pb2.HandTrackingPushRequest(landmark_list=landmark_list)

            try:
                stub.HandTrackingPushStream(request_generator())
            except grpc._channel._InactiveRpcError:  # noqa
                pass

        threading.Thread(target=push).start()

        def pull(_self, stream_event):
            res = stub.HandTrackingPullStream(hand_tracking_pb2.HandTrackingPullRequest())
            try:
                for _ in res:
                    stream_event.set()
            except grpc._channel._MultiThreadedRendezvous:  # noqa
                pass

        events = list()
        for i in range(self.workers):
            event = threading.Event()
            threading.Thread(target=pull, args=(self, event)).start()
            events.append(event)

        for event in events:
            self.assertFalse(event.is_set())

        should_send = True

        for event in events:
            event.wait(1)

        for event in events[:-1]:
            self.assertTrue(event.is_set())
        self.assertFalse(events[-1].is_set())

        self.channel.close()
