import time

import numpy as np

from proto.mediapipe.framework.formats import landmark_pb2
from proto.qoin.proto import hand_tracking_pb2_grpc, hand_tracking_pb2


class HandTrackingService(hand_tracking_pb2_grpc.HandTrackingServicer):
    hands = np.load("demo/hands.npy")

    def HandTrackingPullStream(self, request, context):
        for hand in self.hands:
            time.sleep(0.1)
            yield hand_tracking_pb2.HandTrackingPushRequest(
                landmark_list=landmark_pb2.NormalizedLandmarkList(
                    landmark=[landmark_pb2.NormalizedLandmark(x=h[0], y=h[1], z=h[2]) for h in hand]
                ))
