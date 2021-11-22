import socket

def get_local_ip():
    ip = "Unknown"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip
    

def get_pairing_code():
    ip = get_local_ip()
    return ip.split(".")[-1]