from lib.Server import Server


if __name__ == '__main__':
    server = Server()
    server.create_server('0.0.0.0', 4455)


