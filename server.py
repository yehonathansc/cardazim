import socket
import struct
import argparse
import sys



###########################################################
####################### YOUR CODE #########################
###########################################################


def recieve_data(server_ip, server_port):
    '''
    Send data to server in address (server_ip, server_port).
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.bind((server_ip, server_port))
        soc.listen()
        conn = soc.accept()[0]
        with conn:
            data = conn.recv(1024)
            data = struct.unpack(f'<i {len(data)-4}s', data)[1].decode()
            print(f"Recieved data: {data}")
    

###########################################################
##################### END OF YOUR CODE ####################
###########################################################


def get_args():
    parser = argparse.ArgumentParser(description='Send data to server.')
    parser.add_argument('server_ip', type=str,
                        help='the server\'s ip')
    parser.add_argument('server_port', type=int,
                        help='the server\'s port')
    return parser.parse_args()


def main():
    '''
    Implementation of server.
    '''
    args = get_args()
    try:
        recieve_data(args.server_ip, args.server_port)
    except Exception as error:
        print(f'ERROR: {error}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
