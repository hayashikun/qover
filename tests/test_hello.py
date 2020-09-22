import threading

import grpc

from proto.qoin.proto import hello_pb2_grpc, hello_pb2
from tests import ServerTestCase


class TestHello(ServerTestCase):
    def test_hello(self):
        stub = hello_pb2_grpc.GreeterStub(self.channel)
        res = stub.SayHello(hello_pb2.HelloRequest(name='you'))
        self.assertEqual(res.message, 'Hello, you!')

    def test_hello_stream(self):
        stub = hello_pb2_grpc.GreeterStub(self.channel)

        def test_stream(name, stream_event):
            try:
                res = stub.HelloStream(hello_pb2.HelloRequest(name=name))
                for r in res:
                    if not stream_event.is_set():
                        stream_event.set()
                        self.assertEqual(r.message, f'Hello Stream, {name}!')
            except grpc._channel._MultiThreadedRendezvous:  # noqa
                pass

        events = list()
        for i in range(self.workers + 1):
            event = threading.Event()
            threading.Thread(target=test_stream, args=(f'you_{i}', event)).start()
            events.append(event)

        for event in events:
            event.wait(1)

        for event in events[:-1]:
            self.assertTrue(event.is_set())
        self.assertFalse(events[-1].is_set())

        self.channel.close()

    def test_500_workers(self):
        self.tearDown()
        self.workers = 500
        self.setUp()
        self.test_hello_stream()
