from http import server

# 命令行传参
from sys import argv  #list[str1, str2...]

def main():
    if not argv[0]:
        return
    server.HTTPServer(('0.0.0.0', int(argv[0])), Job)

class Job(server.BaseHTTPRequestHandler):
    pass
