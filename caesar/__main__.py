import argparse
import sys

import caesar


def usage():
    print('\t\t\t Pycaesar\n\n')
    print('Usage: pycaesar -k key -m message')
    print('-k --key                - key is a numeric value to encrypt the message. Mandatory.')
    print('-m --message            - message that is going to be encrypted. Mandatory')
    print('\n\nExamples:\n pycaesar -k 1 -m my super message that is going to be encrypted')
    sys.exit(0)


def parse_args():
    parser = argparse.ArgumentParser(prog='Pycaesar')
    group_request = parser.add_argument_group('Encryption options')
    group_request.add_argument('-k', '--key', nargs="*", type=str, default=[], action="store", dest="key",
                               help="Key is a numeric value to encrypt the message")
    group_request.add_argument('-m', '--message', action='store', dest='message_to_encrypt',
                               help='Message to be encrypted')
    args = parser.parse_args()
    return args


def main():

    if not len(sys.argv[1:]):
        usage()
    args = parse_args()

    if args.key and args.message_to_encrypt and len(args.key) == 1:
        cipher_text = caesar.encrypt(message=args.message_to_encrypt, key=args.key[0])
        print('Cipher text: {}'.format(cipher_text))
    else:
        print('ERROR! You have to send one key and message :)')

if __name__ == "__main__":
    main()
