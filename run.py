# Cyber-F0x
# Bad Char Chunker
import argparse

def main(size):
    bad_chars = [ i for i in range(0,256)]
    parsed = (list(split(bad_chars,size)))
    print("#Breaking List down in to {} chunks".format(size))
    print("bad += b\"\"")
    for i, each_chunk in enumerate(parsed):
        x = ""
        for each_byte in each_chunk:
            x += (hex(each_byte))
    print("bad +=b\"{}\" # Chunk {} Size {} bytes".format(x.replace("0x","\\x"),i,len(each_chunk)))


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--size',default=16)
    args = parser.parse_args()
    main(args.size)