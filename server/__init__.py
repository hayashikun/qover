from concurrent import futures

import grpc

from proto.qoin.proto import hello_pb2_grpc, face_mesh_pb2_grpc, hand_tracking_pb2_grpc
from server.face_mesh import FaceMeshService
from server.hand_tracking import HandTrackingService
from server.hello import HelloService


class Server:
    def __init__(self, max_workers=3):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))

    def run(self, port=50051):
        hello_service = HelloService()
        hand_tracking_service = HandTrackingService()
        face_mesh_service = FaceMeshService()

        hello_pb2_grpc.add_GreeterServicer_to_server(hello_service, self.server)
        hand_tracking_pb2_grpc.add_HandTrackingServicer_to_server(hand_tracking_service, self.server)
        face_mesh_pb2_grpc.add_FaceMeshServicer_to_server(face_mesh_service, self.server)
        self.server.add_insecure_port(f'0.0.0.0:{port}')
        self.server.start()
        print(f"Server running http://0.0.0.0:{port}")
        self.server.wait_for_termination()


if __name__ == "__main__":
    server = Server()
    server.run()
