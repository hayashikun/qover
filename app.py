from server import Server


def run():
    server = Server(max_workers=10)
    server.run(port=9090)


if __name__ == "__main__":
    run()
