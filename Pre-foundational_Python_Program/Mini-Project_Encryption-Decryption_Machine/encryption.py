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


def get_c(char, n, e):
    """
    This function takes a char (char) and the public keys (n, e) as arguments
    and returns the cipher of this char using the simplified version of the RSA algorithm.

    The function ord() is used to convert a char to an integer.

    Arguments:
    `char`: a string representing a char.
    `n`: an integer representing the first value of the public key.
    `e`: an integer representing the second value of the public key.

    Output:
    `c`: an integer representing the cipher of the char.

    Example:
    get_c('a', 221, 5) should return 54 as output.
    """

    char_as_int = ord(char)
    c = (char_as_int ** e) % n

    return c


def get_cipher(string):
    """
    This function takes a string as argument, encrypt the string
    using a simplified version of the RSA algorithm and return the cipher.

    Arguments:
    `string`: a string representing the message to encrypt.

    Output:
    `cipher`: a list of integers representing the cipher (c) for each character.

    Example:
    get_cipher('apple') should return [54, 125, 125, 75, 186] as cipher.
    """

    [d, n, e] = get_private_and_public_keys()
    cipher = []

    for char in string:
        c = get_c(char, n, e)
        cipher.append(c)

    return cipher


def encrypt():
    """
    This function takes a string as user input, encrypt the string
    using a simplified version of the RSA algorithm and print the cipher
    separating the list of integers by comma.

    Arguments:
    None.

    Output:
    None.

    Example:
    Call encrypt() passing 'apple' as user input should print '54,125,125,75,186'
    """
    user_input = input('Enter the message to encrypt (Example: apple): ')

    cipher = get_cipher(user_input)

    cipher_by_comma = ','.join(str(c) for c in cipher)
    print(cipher_by_comma)


encrypt()
