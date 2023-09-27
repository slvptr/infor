import sys
from collections import Counter

if __name__ == "__main__":
    with open(sys.argv[1], encoding='utf-8') as f:
        msg = f.read()
        stat = Counter(list(msg))

        for i in stat:
            ch = i
            if i == "\t":
                ch = "\\t"
            if i == "\n":
                ch = "\\n"
            
            print("{}: {}".format(ch, stat[ch]))