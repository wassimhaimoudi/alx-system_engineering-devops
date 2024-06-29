#!/usr/bin/python3
# Shares file on web-server web-01
from fabric.api import *

env.hosts = ['18.235.248.15', '100.25.31.89', '52.91.124.204']

def share(local_file_path):
    remote_dest_path = f'~/{local_file_path}'
    put(local_file_path,  remote_dest_path)
    run(f'chmod 755 {remote_dest_path}')
