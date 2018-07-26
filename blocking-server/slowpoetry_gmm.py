# This is the blocking version of the Slow Poetry Server.

import argparse, os, socket, time, sys


def parse_args():
    usage = """usage: %prog [options] poetry-file

This is the Slow Poetry Server, blocking edition.
Run it like this:

  python slowpoetry.py <path-to-poetry-file>

If you are in the base directory of the twisted-intro package,
you could run it like this:

  python blocking-server/slowpoetry.py poetry/ecstasy.txt

to serve up John Donne's Ecstasy, which I know you want to do.
"""

    parser = argparse.ArgumentParser(description=usage)

    help = "The poetry file."
    parser.add_argument('file', type=argparse.FileType('r'), help=help)

    help = "The port to listen on. Default to a random available port."
    parser.add_argument('--port', type=int, help=help)

    help = "The interface to listen on. Default is localhost."
    parser.add_argument('--iface', help=help, default='localhost')

    help = "The number of seconds between sending bytes."
    parser.add_argument('--delay', type=float, help=help, default=.7)

    help = "The number of bytes to send at a time."
    parser.add_argument('--num-bytes', type=int, help=help, default=10)

    args = parser.parse_args()

    return args



def send_poetry(sock, poetry_file, num_bytes, delay):
    """Send some poetry slowly down the socket."""

    inputf = open(poetry_file)

    while True:
        bytes = inputf.read(num_bytes)

        if not bytes: # no more poetry :(
            sock.close()
            inputf.close()
            return

        print 'Sending %d bytes' % len(bytes)

        try:
            sock.sendall(bytes) # this is a blocking call
        except socket.error:
            sock.close()
            inputf.close()
            return

        time.sleep(delay)


def serve(listen_socket, poetry_file, num_bytes, delay):
    while True:
        sock, addr = listen_socket.accept()

        print 'Somebody at %s wants poetry!' % (addr,)

        send_poetry(sock, poetry_file, num_bytes, delay)


def main():
    if len(sys.argv) < 2 :
        sys.exit('file err: Please provide a poetry file')
    poetry_file = sys.argv[1]
    options = parse_args()
       
    print 'Poetry file:',poetry_file
    print 'Options:',options.iface, options.port, options.num_bytes, options.delay


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((options.iface, options.port or 0))
    sock.listen(5)

    print 'Serving %s on port %s.' % (poetry_file, sock.getsockname()[1])

    serve(sock, poetry_file, options.num_bytes, options.delay)


if __name__ == '__main__':
    main()
