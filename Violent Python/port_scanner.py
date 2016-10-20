import argparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def scan_connection(target_host, target_port):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((target_host, target_port))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print('[+] %d/tcp open' % target_port)
        print('[+] ' + str(results))
    except:
        screenLock.acquire()
        print('[-] %d/tcp closed' % target_port)
    finally:
        screenLock.release()
    connSkt.close() 

def scan_port(target_host, target_ports):
    try:
        target_ip = gethostbyname(target_host)
    except:
        print("[-] Cannot resolve '%s': Unknown host" %target_host)
        return

    try:
        tgtName = gethostbyaddr(target_ip)
        print('\n[+] Scan Results for: ' + tgtName[0])
    except:
        print('\n[+] Scan Results for: ' + target_ip)

    setdefaulttimeout(1)
    for target_port in target_ports:
        t = Thread(target=scan_connection,
                   args=(target_host,int(target_port)))
        t.start()


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

    init_argparse()

    scan_port(target_host, target_ports)


if __name__ == '__main__':
    main()