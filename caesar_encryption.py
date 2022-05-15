def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ''.join(list(map(lambda x: a[x] if type(x) is int else x, list(map(lambda x: (a.index(x) + 3) % 26 + 26 * x.isupper() if x.isalpha() else x, plaintext)))))
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = ''.join(list(map(lambda x: a[x] if type(x) is int else x, list(map(lambda x: (a.index(x) - 3) % 26 + 26 * x.isupper() if x.isalpha() else x, ciphertext)))))
    return plaintext

if __name__ == '__main__':
    assert encrypt_caesar('PYTHON') == 'SBWKRQ'
    assert encrypt_caesar('python') == 'sbwkrq'
    assert encrypt_caesar("Python3.6") == 'Sbwkrq3.6'
    assert decrypt_caesar("SBWKRQ") == 'PYTHON'
    assert decrypt_caesar("sbwkrq") == 'python'
    assert decrypt_caesar("Sbwkrq-3.6") == 'Python-3.6'
    print('[OK]')