import os
import socket
import threading
import logging
import time

# Logging Configuration: Output logs to the console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[logging.StreamHandler()]  # Use StreamHandler for console logging
)

LOGO = """
\033[92m
██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗  ██████╗ ██╗    ██╗ █████╗ ██████╗ ██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔═══██╗ ██╔══██╗██║    ██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║       █████╗  ██║   ██║ ██████╔╝██║ █╗ ██║███████║██████╔╝██║  ██║
██╔═══╝ ██║   ██║██╔═██║    ██║       ██╔══╝  ██║   ██║ ██╔═██║ ██║███╗██║██╔══██║██╔═██║ ██║  ██║
██║     ╚██████╔╝██║ ██║    ██║       ██║     ╚██████╔╝ ██║ ██║ ╚███╔███╔╝██║  ██║██║ ██║ ██████╔╝
╚═╝      ╚═════╝ ╚═╝ ╚═╝    ╚═╝       ╚═╝      ╚═════╝  ╚═╝ ╚═╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝ ╚═╝ ╚═════╝ 
\033[0m
"""

class PortForwarder(threading.Thread):
    """
    A thread that handles port forwarding between a source and a target.
    """
    def __init__(self, source_host, source_port, target_host, target_port):
        super().__init__()
        self.source_host = source_host
        self.source_port = source_port
        self.target_host = target_host
        self.target_port = target_port

    def run(self):
        try:
            # Set up listener
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((self.source_host, self.source_port))
            server.listen(5)
            logging.info(f"Listening on {self.source_host}:{self.source_port}")
            print(f"\033[94mListening on {self.source_host}:{self.source_port} and forwarding to {self.target_host}:{self.target_port}\033[0m")

            while True:
                client_socket, address = server.accept()
                logging.info(f"Connection received from {address}")
                print(f"\033[92mConnection received from {address}\033[0m")
                threading.Thread(target=self.forward_traffic, args=(client_socket,)).start()

        except Exception as e:
            logging.error(f"Error: {e}")
            print(f"\033[91mError: {e}\033[0m")

    def forward_traffic(self, client_socket):
        """
        Handles traffic forwarding between the client and the target.
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as remote_socket:
                remote_socket.connect((self.target_host, self.target_port))
                while True:
                    data = client_socket.recv(4096)
                    if len(data) == 0:
                        break
                    remote_socket.sendall(data)
                    response = remote_socket.recv(4096)
                    client_socket.sendall(response)
        except Exception as e:
            logging.error(f"Error forwarding traffic: {e}")
        finally:
            client_socket.close()


def get_public_ip():
    """
    Gets the public IP of the machine.
    """
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception as e:
        logging.error(f"Error retrieving public IP: {e}")
        return "Unknown"


def main():
    print(LOGO)
    print("\033[93mWelcome to the Port Forwarding Tool\033[0m")
    print("\033[94m--------------------------------------\033[0m")

    # Prompt user for the port to forward
    try:
        source_port = int(input("\033[94mEnter the source port to forward from: \033[0m"))
    except ValueError:
        print("\033[91mInvalid port. Exiting...\033[0m")
        return

    # Automatically determine target host and port
    target_host = "8.8.8.8"  # Example: Google's public DNS server
    target_port = 80  # Example: HTTP port

    source_host = "0.0.0.0"  # Listen on all available network interfaces

    # Display Configuration
    public_ip = get_public_ip()
    logging.info(f"Forwarding link: http://{public_ip}:{source_port}")
    print(f"\033[92mYour forwarding link is: http://{public_ip}:{source_port}\033[0m")
    logging.info(f"Targeting: {target_host}:{target_port}")

    # Start Port Forwarding
    forwarder = PortForwarder(source_host, source_port, target_host, target_port)
    forwarder.daemon = True  # Ensure thread exits when main program ends
    forwarder.start()

    logging.info("Port forwarding started.")
    print("\033[92mPort forwarding initialized successfully!\033[0m")
    print("\033[94mPress Ctrl+C to stop.\033[0m")

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\033[91m\nStopping port forwarding...\033[0m")
        logging.info("Port forwarding stopped by user.")
        os._exit(0)


if __name__ == "__main__":
    main()
