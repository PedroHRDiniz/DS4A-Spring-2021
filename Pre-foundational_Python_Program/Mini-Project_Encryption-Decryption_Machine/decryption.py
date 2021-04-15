def get_private_and_public_keys():
    """
    This function returns the private and public keys of the
    RSA encryption-decryption machine using a simplified version
    of the RSA algorithm.

    Arguments:
    None.

    Output:
    `d`: an integer representing the private key.
    `n`: an integer representing the first value of the public key.
    `e`: an integer representing the second value of the public key.

    Example:
    get_private_and_public_keys() should return d=77, n=221, e=5 as output.
    """
    p = 13  # first prime number
    q = 17  # second prime number
    n = p * q  # public key first value
    phi = (p - 1) * (q - 1)  # phi(n)
    e = 5  # public key second value (1 < e < phi, where phi % e != 0)
    i = 2  # an integer
    d = int((i * phi + 1) / e)  # private key

    return d, n, e


def decrypt_c(c, d, n):
    """
    This function takes an integer (c) as first argument representing the cipher
    of a char, an integer (d) as second argument representing the private key and
    an integer (n) as third argument representing the first value of the public key
    and returns the char decrypted using the simplified version of the RSA algorithm.

    The function chr() is used to convert an integer to a char.

    Arguments:
    `c`: an integer representing the cipher of a char.
    `d`: an integer representing the private key.
    `n`: an integer representing the first value of the public key.

    Output:
    `decrypted`: an string representing the char decrypted.

    Example:
    decrypt_c(54, 77, 221) should return 'a' as output.
    """
    decrypted_float = (c ** d) % n

    decrypted = chr(int(decrypted_float))

    return decrypted


def decrypt_cipher(cipher_list):
    """
    This function takes a list of strings (cipher_list) as argument representing
    the cipher for each character, decrypts the cipher using a simplified
    version of the RSA algorithm and returns the original message.

    Arguments:
    `cipher_list`: a list of strings representing the cipher for each character.

    Output:
    `message`: a string representing the original message.

    Example:
    decrypt_cipher([54, 125, 125, 75, 186]) should return 'apple' as message.
    """

    [d, n, e] = get_private_and_public_keys()
    message = ''

    for cipher in cipher_list:
        c = int(cipher)
        cipher_decrypted = decrypt_c(c, d, n)
        message += cipher_decrypted

    return message


def decrypt():
    '''
    This function takes a string as user input representing the cipher
    for each character separated by comma, decrypts the cipher using
    a simplified version of the RSA algorithm and prints the original message.

    Arguments:
    None.

    Output:
    None.

    Example:
    Call decrypt() passing '54,125,125,75,186' as user input should print 'apple'
    '''

    input_message = '''
    Enter the cipher integers to decrypt.
    Make sure to enter the cipher list separating the integers with commas.
    (Example: 54,125,125,75,186): '''

    user_input = input(input_message)

    cipher_list = user_input.split(',')

    message = decrypt_cipher(cipher_list)

    print(message)


decrypt()
