import time

from proto.qoin.proto import face_mesh_pb2_grpc, face_mesh_pb2


class FaceMeshService(face_mesh_pb2_grpc.FaceMeshServicer):
    data = dict()

    def FaceMeshPullStream(self, request, context):
        st = time.time()
        self.data[st] = None
        while context.is_active():
            d = self.data[st]
            if d is not None:
                self.data[st] = None
                yield face_mesh_pb2.FaceMeshPullReply(landmark_list=d)
        del self.data[st]

    def FaceMeshPushStream(self, request, context):
        for req in request:
            for k in self.data:
                self.data[k] = req.landmark_list
        return face_mesh_pb2.FaceMeshPushReply()
