import time

from proto.qoin.proto import hand_tracking_pb2_grpc, hand_tracking_pb2


class HandTrackingService(hand_tracking_pb2_grpc.HandTrackingServicer):
    data = None
    timestamp = 0

    def HandTrackingPullStream(self, request, context):
        last_ts = 1
        while context.is_active():
            if self.timestamp > last_ts:
                last_ts = time.time()
                yield hand_tracking_pb2.HandTrackingPullReply(landmark_list=self.data)

    def HandTrackingPushStream(self, request, context):
        for req in request:
            self.data = req.landmark_list
            self.timestamp = time.time()
        return hand_tracking_pb2.HandTrackingPushReply()
