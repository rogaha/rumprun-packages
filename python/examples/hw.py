import os
import sys
import socket

# Importing these verifies that our static modules built correctly
import math
import ssl
import zlib
import json


def hello_world():
    print("\n" * 4)
    print("Welcome to rumprun/python %d.%d!" % sys.version_info[:2])
    print("{} / {}".format(sys.platform, os.name))
    print(json.dumps({'key': 'value'}))

    if socket.has_ipv6:
        print("IPv6 is enabled")

    try:
        import sqlite3
        print("sqlite {} built correctly".format(sqlite3.sqlite_version))
    except ImportError as e:
        print("sqlite3 not built")

    print("\n" * 2)

if __name__ == '__main__':
    hello_world()

