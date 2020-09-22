from demo.hand_tracking import HandTrackingService
from proto.qoin.proto import hand_tracking_pb2_grpc
from server import Server


class DemoServer(Server):
    def run(self, port=50051):
        hand_tracking_service = HandTrackingService()
        hand_tracking_pb2_grpc.add_HandTrackingServicer_to_server(hand_tracking_service, self.server)
        self.server.add_insecure_port(f'0.0.0.0:{port}')
        self.server.start()
        print(f"Server running http://0.0.0.0:{port}")
        self.server.wait_for_termination()
