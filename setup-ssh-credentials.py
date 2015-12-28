#!/usr/bin/python

import argparse
import os
import time
import tempfile
from boto import ec2


def create_key(args):
    key_name = 'scylla-test-{}'.format(time.strftime('%Y-%m-%d-%H.%M.%S'))
    key_filename = os.path.join(tempfile.gettempdir(),
                                '{}.pem'.format(key_name))
    conn = ec2.connect_to_region(args.region)
    key = conn.create_key_pair(key_name)
    key.save(tempfile.gettempdir())
    os.chmod(key_filename, 0o400)
    print(key_name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('ec2-attach-network-interface')
    parser.add_argument('--region', help='ec2 region', default='us-west-2')
    parser.add_argument('--operation', help='key_operation', default='create')
    args = parser.parse_args()
    try:
        create_key(args)
    except Exception, details:
        print('Error creating key: {}'.format(details))
