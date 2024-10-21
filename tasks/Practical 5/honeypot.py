import socket
import logging
import threading

logging.basicConfig(filename='honeypot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def start_honeypot(host='0.0.0.0', port=8888):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Honeypot is listening on {host}:{port}")
    
    while True:
        try:
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr}")
            logging.info(f"Connection from {addr}")
            response_message = "Welcome to the honeypot! This is a simulated server.\n"
            client_socket.sendall(response_message.encode('utf-8'))
            client_socket.close()
        except Exception as e:
            print(f"Error: {e}")
            logging.error(f"Error: {e}")
            break
    
    server_socket.close()

def run_honeypot_in_thread():
    honeypot_thread = threading.Thread(target=start_honeypot)
    honeypot_thread.daemon = True 
    honeypot_thread.start()
    print("Honeypot is running in a background thread.")

run_honeypot_in_thread()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nHoneypot stopped.")
    logging.info("Honeypot stopped.")
