import argparse
import logging


parser = argparse.ArgumentParser()

parser.add_argument(
        'configuration',
        help = 'configuration file',
        )

parser.add_argument(
        'known_keys',
        help = 'known keys file',
        )

def read_keys(key_file):

    keys = list()

    with open(key_file, 'r') as configuration:
        for line in configuration.readlines():
            try:
                key, value = line.split('=')
            except ValueError:
                key = line

            keys.append(key.strip())

    return keys

if __name__ == '__main__':

    args = parser.parse_args()

    known_keys = read_keys(args.known_keys)

    configuration_keys = read_keys(args.configuration)

    new_keys = [ k for k in configuration_keys if k not in known_keys ]

    with open(args.known_keys, 'a') as out:
        for k in new_keys:
            out.write(k)
            out.write('\n')
