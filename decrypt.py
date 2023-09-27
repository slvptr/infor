import sys
from utils import extended_gcd, init_alphabet

def decrypt(msg, alphabet, literal_to_index, a, b):
    a1, _ = extended_gcd(a, len(alphabet))
    
    decrypted_msg = []
    for ch in msg:
        x = (a1 * (literal_to_index[ch] - b)) % len(alphabet)
        decrypted_msg.append(alphabet[x])
        
    return ''.join(decrypted_msg)


if __name__ == "__main__":
    alphabet, literal_to_index = init_alphabet()

    inp, out, a, b = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])

    with open(inp, encoding='utf-8') as f:
        msg = f.read()
        encrypted_msg = decrypt(msg, alphabet, literal_to_index, a, b)

    with open(out, 'w', encoding='utf-8') as f:
        f.write(encrypted_msg)