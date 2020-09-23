import fire

from demo import DemoServer
from server import Server


def run(run_demo=False, port=9999, workers=10):
    if run_demo:
        server = DemoServer(max_workers=workers)
    else:
        server = Server(max_workers=workers)

    server.run(port=port)


if __name__ == "__main__":
    fire.Fire(run)
