import json

"""
Small command-line programm to encrypt or decrypt integer messages
"""

def encrypt(e, n, message):
    if message > n:
        exit('Not possible to encrypt, message is larger than n!')
    return int(divmod(pow(message, e), n)[1])


def decrypt(d, n, encrypted_message):
    return int(divmod(pow(encrypted_message, d), n)[1])


def obtain_personal_keys():
    while True:
        print("Provide filename for keys (default = keys.json): ", end='')
        keys_filename = input()

        if keys_filename == '':
            with open('keys.json') as f:
                keys = json.load(f)
            break
        else:
            try:
                with open('keys.json') as f:
                    keys = json.load(f)
                break
            except FileNotFoundError:
                print('Not valid file')

    e, n = keys['public']
    d, _ = keys['private']

    return e, d, n


def obtain_private_key():
    e, d, n = obtain_personal_keys()
    return d, n


def obtain_public_key():
    e, d, n = obtain_personal_keys()
    return e, n


while True:
    print("What do you want to do?")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("q. quit")
    action = input()

    if action == 'q':
        break
    elif int(action) == 1:
        print("### Encrypting a message using someone else's public key.")
        print('Insert public-key (e, n): ', end='')
        public_key = input()
        e, n = [int(i) for i in public_key[1:-1].split(',')]
        print("### Insert message:", end='')
        message = input()
        encrypted_message = encrypt(e, n, int(message))
        print('### Encrypted message = {}\n'.format(encrypted_message))
    elif int(action) == 2:
        print("### Decrypting a message using one's own private key.")
        d, n = obtain_private_key()
        print("### Insert encrypted message: ", end='')
        message = input()
        decrypted_message = decrypt(d, n, int(message))
        print('### Decrypted message = {}\n'.format(decrypted_message))
