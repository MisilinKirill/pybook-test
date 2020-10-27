import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in plaintext:
        if ord(i)>96 and ord(i)<123:
            if ord(i)+shift>122:
                ciphertext+=chr(96+(shift-(122-ord(i))))
            else: ciphertext += chr(ord(i)+shift)
        elif ord(i)<91 and ord(i)>64:
            if ord(i)+shift>90:
                ciphertext+=chr(64+(shift-(90-ord(i))))
            else: ciphertext += chr(ord(i)+shift)
        else: ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in ciphertext:
        if ord(i)>96 and ord(i)<123:
            if ord(i)-shift<97:
                plaintext+=chr(123-(shift-(ord(i)-97)))
            else: plaintext += chr(ord(i)-shift)
        elif ord(i)<91 and ord(i)>64:
            if ord(i)-shift<65:
                plaintext+=chr(91-(shift-(ord(i)-65)))
            else: plaintext += chr(ord(i)-shift)
        else: plaintext += i
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift