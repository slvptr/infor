import sys
from utils import init_alphabet
from math import gcd

def encrypt(msg, alphabet, literal_to_index, a, b):
    encrypted_msg = []
    for ch in msg:
        x = (a * literal_to_index[ch] + b) % len(alphabet)
        encrypted_msg.append(alphabet[x])
        
    return ''.join(encrypted_msg)


if __name__ == "__main__":
    alphabet, literal_to_index = init_alphabet()

    inp, out, a, b = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])

    m = len(alphabet)
    if (gcd(a, m) != 1):
        raise RuntimeError("a и m должны быть взаимно простыми")

    with open(inp, encoding='utf-8') as f:
        msg = f.read()
        encrypted_msg = encrypt(msg, alphabet, literal_to_index, a, b)

    with open(out, 'w', encoding='utf-8') as f:
        f.write(encrypted_msg)



