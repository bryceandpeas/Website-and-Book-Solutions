import pxssh


class Client:

    # Init class
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    # Connect to client
    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print('Botnet: Connection error')
            print('Botnet: Error: {0}'.format(e))

    # Send commands
    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


# Send commands and get output
def botnet_command(command):
    for client in botNet:
        output = client.send_command(command)
        print('Botnet: Connected to {0}'.format(client.host))
        print('Botnet: Output: '.format(output))


# Add a client
def add_client(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)


botNet = []
add_client('127.0.0.1', 'root', '')
add_client('127.0.0.1', 'root', '')
add_client('127.0.0.1', 'root', '')

botnet_command('uname -v')
botnet_command('cat /etc/issue')