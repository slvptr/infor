literal_ranges = [(1040, 1106), (32, 65), (91, 97), (123, 127), (9, 11)]

def init_alphabet():
    global literal_ranges

    alphabet = []
    literal_to_index = dict()
    
    for pair in literal_ranges:
        for i in range(pair[0], pair[1]):
            alphabet.append(chr(i))
            literal_to_index[chr(i)] = len(alphabet) - 1
    
    return alphabet, literal_to_index
    

def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
        
    return old_s, old_t
    

if __name__ == "__main__":
    alphabet, literal_to_index = init_alphabet()

    print("Размер алфавита:", len(alphabet), "\n") 
    print("--- Алфавит ---\n", " ".join(alphabet)) 
    
    
    
    
    
    
