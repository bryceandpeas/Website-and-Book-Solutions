import argparse
import nmap


def nmap_scan(target_host, target_port):

    # Create scanner object
    port_scanner = nmap.PortScanner()
    # Run scan
    port_scanner.scan(target_host, target_port)
    # Get ouput from scanner
    output = port_scanner[target_host]['tcp'][int(target_port)]['state']
    # Print output
    print('Nmap Scanner: \n'
          'Scanned: {0} tcp/{1}'
          'Returned: {2}'.format(target_host, target_port, output))

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

    for target_port in target_ports:
        nmap_scan(target_host, target_port)


if __name__ == '__main__':
    main()
