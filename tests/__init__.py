import threading
import unittest

import grpc

from server import Server


class ServerTestCase(unittest.TestCase):
    port = 50051
    workers = 4

    def setUp(self):
        self.pp_server = Server(max_workers=self.workers)
        self.channel = grpc.insecure_channel(f'localhost:{self.port}')

        start_event = threading.Event()

        def server_start(_self):
            _self.pp_server.run(_self.port)

        def is_server_started(_self):
            return _self.pp_server.server._state.stage == grpc._server._ServerStage.STARTED  # noqa

        def check_server_running(_self):
            while not is_server_started(_self):
                pass
            start_event.set()

        threading.Thread(target=server_start, args=(self,)).start()
        threading.Thread(target=check_server_running, args=(self,)).start()

        start_event.wait(3)

        if not is_server_started(self):
            raise Exception("Failed to start server")

    def tearDown(self):
        self.pp_server.server._state.termination_event.set()
