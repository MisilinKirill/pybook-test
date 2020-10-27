def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    ciphertext = a_vigenere(plaintext, keyword, 1)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    plaintext = a_vigenere(ciphertext, keyword, -1)
    return plaintext

def a_vigenere(plaintext: str, keyword: str, is_cipher: int) -> str:
    ciphertext = ""
    i = 0
    for idx, x in enumerate(plaintext):
        if i >= len(keyword):
            i = 0
        code_key = sh(keyword[i], x, is_cipher)
        ciphertext += change_symbol(x, code_key)
        i = i + 1
    return ciphertext


def find_pos(input_x: str) -> int:
    lst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", \
           "w", "x", "y", "z"]
    for idx, x in enumerate(lst):
        if x.lower() == input_x.lower():
            return idx
    return -1


def sh(key_x: str, x: str, is_cipher: int) -> int:
    m = find_pos(x)
    k = find_pos(key_x)
    return ((m + k * is_cipher) % 26)


def change_symbol(x: str, shift: int) -> str:
    i_code = ord(x)
    i_first = 0;
    if (i_code >= ord('a') and i_code <= ord('z')) or \
            (i_code >= ord('A') and i_code <= ord('Z')):
        if x.isupper():
            i_first = ord("A")
        else:
            i_first = ord("a")
        return chr(i_first + shift)
    else:
        return x
