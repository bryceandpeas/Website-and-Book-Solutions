import argparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)


def scan_connection(target_host, target_port):

    try:
        # Create socket - AF_INET for IPv4/hostname - SOCK_STREAM for TCP
        client = socket(AF_INET, SOCK_STREAM)
        # Connect
        client.connect((target_host, target_port))
        # Send data 
        client.send('ViolentPython\r\n')
        # Get
        results = client.recv(100)
        # Get screenlock
        screenLock.acquire()
        # Print response
        print('Scanner: {0}/tcp open'.format(target_port))
        print('Scanner: {0}'.format(results))

    except:
        screenLock.acquire()
        print('Scanner: {0}/tcp closed'.format(target_port))

    finally:
        screenLock.release()

    client.close() 

def scan_port(target_host, target_ports):

    try:
        target_ip = gethostbyname(target_host)

    except:
        print('Scanner: Cannot resolve {0}: Unknown host'.format(target_host))
        return

    try:
        target_name = gethostbyaddr(target_ip)
        print('\nScanner: Result for host: {0}'.format(target_name[0]))
    except:
        print('\nScanner: Result for port: {0}'.format(target_ip))

    setdefaulttimeout(1)

    for target_port in target_ports:
        scan_thread = Thread(target=scan_connection,
                   args=(target_host,int(target_port)))
        scan_thread.start()


def main():

    # Define arguments
    def init_argparse():
        parser = argparse.ArgumentParser('\n')

        parser.add_argument('-H',
                        '--host',
                        type=str,
                        help='Define the target host',
                        required=True)

        parser.add_argument('-p',
                        '--port',
                        type=str,
                        help='Define comma seperted target ports',
                        required=True)

        args = parser.parse_args()

        target_host = args.host
        target_ports = str(args.port).split(',')

        return (target_host, target_ports)

    target_host, target_ports = init_argparse()

    scan_port(target_host, target_ports)


if __name__ == '__main__':
    main()