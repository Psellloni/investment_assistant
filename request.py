import os
import config

from tinkoff.invest import Client


def main():
    with Client(config.TOKEN) as client:
        print(client.instruments.bonds())


if __name__ == "__main__":
    main()