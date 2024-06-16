import socket
import time


def wait_for_db(host, port, timeout=60):
    start_time = time.time()
    while True:
        try:
            sock = socket.create_connection((host, port), timeout)
            sock.close()
            print(f"Database at {host}:{port} is available.")
            return True
        except (socket.error, socket.timeout):
            if time.time() - start_time >= timeout:
                print(f"Timeout waiting for database at {host}:{port}.")
                return False
            else:
                time.sleep(1)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python wait_for_db.py <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    wait_for_db(host, port)
