import sys
import os
import six
import re
import socket
import subprocess
import threading

class Socket(object):

    def __init__(self, hostname, port, option=None):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((hostname, port))
        except:
            raise
        if option is not None:
            self.sock.send(option)
        data = ""
        while "OK" not in data:
            data = self.sock.recv(1024)

    def __del__(self):
        if self.sock:
            self.sock.close()

    def query(self, sentence, pattern):
        assert(isinstance(sentence, six.text_type))
        self.sock.sendall("%s\n" % sentence.encode('utf-8').strip())
        data = self.sock.recv(1024)
        recv = data
        while not re.search(pattern, recv):
            data = self.sock.recv(1024)
            recv = "%s%s" % (recv, data)
        return recv.strip().decode('utf-8')


class Subprocess(object):

    def __init__(self, command, timeout=180):
        subproc_args = {'stdin': subprocess.PIPE, 'stdout': subprocess.PIPE,
                'stderr': subprocess.STDOUT, 'cwd': '.',
                'close_fds': sys.platform != "win32"}
        try:
            env = os.environ.copy()
            self.process = subprocess.Popen(command, env=env, **subproc_args)
            self.process_command = command
            self.process_timeout = timeout
        except OSError:
            raise

    def __del__(self):
        self.process.stdin.close()
        self.process.stdout.close()
        try:
            self.process.kill()
            self.process.wait()
        except OSError:
            pass
        except TypeError:
            pass
        except AttributeError:
            pass


    def query(self, sentence, pattern, encoding='utf-8'):
        assert(isinstance(sentence, six.text_type))
        def alarm_handler():
            raise subprocess.TimeoutExpired(self.process_command, self.process_timeout)

        timer = threading.Timer(self.process_timeout, alarm_handler)
        result = ""
        try:
            self.process.stdin.write(sentence.encode(encoding)+six.b('\n'))
            self.process.stdin.flush()
            while True:
                line = self.process.stdout.readline().rstrip().decode(encoding)
                if re.search(pattern, line):
                    break
                result = "%s%s\n" % (result, line)
        finally:
            timer.cancel()
        return result
