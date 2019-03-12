#!/bin/python3.7
from heapq import heappush, heappop, heapify
from numpy import log2
import magic
from PIL import Image
import sys
import os

def ascii_distribution(data, n):
    """
    return the distribution of the
    data in the form of a list.
    """
    _data = ["".join([chr(data[i-j]) for j in range(0,n)]) for i in range(n-1,len(data))]
    dist = [[float(_data.count(sym))/float(len(_data)), [sym, "", float(_data.count(sym))/float(len(_data))]] for sym in set(_data)]
    return dist

def ascii_huffman(data, n):
    """
    return a tuple with the 
    huffman encryption based in the
    ascii dictionary, the entropy and
    the expected length.
    (dictionary, entropy, expected length)
    """
    huff_dist = ascii_distribution(data, n)
    heapify(huff_dist)
    while len(huff_dist) > 1:
        lo = heappop(huff_dist)
        for pair in lo[1:]:
            pair[1] = "0"+pair[1]
        hi = heappop(huff_dist)
        for pair in hi[1:]:
            pair[1] = "1"+pair[1]
        h = [lo[0]+hi[0]]+lo[1:]+hi[1:]
        heappush(huff_dist, h)
    huff_code = sorted(huff_dist[0][1:], key=lambda p: (len(p[1]), p))
    entropy = -sum([sym[-1]*log2(sym[-1]) for sym in huff_code])
    expected_length = sum([float(len(sym[1]))*sym[-1] for sym in huff_code])
    return huff_code, entropy, expected_length


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Introduce a filename to read.", file=sys.stderr)
        sys.exit(1)
    name = sys.argv[1]
    
    data = ""
    if os.path.exists (name):
        if magic.from_file(name, mime=True).startswith('image'):
            with Image.open (name) as im:
                data = list(im.getdata())
        else:
            with open(name, "rb") as fp:
                data = fp.read()
    else:
        print("No file in directory with name:"+sys.argv[1]+"\n", file=sys.stderr)
        sys.exit(1)
    
    huffman, H, L  = ascii_huffman(data, 2)
    print ("Entropy of the text: {0:f}\nExpected length: {1:f}\nOriginal size: {2:d}\nCompression rate: {3:f}".format(H, L, len(data), 16.0/L))
    
    data1 = [data[0]]+[(data[i]-data[i-1])//2+128 for i in range(1, len(data))]
    huffman, H, L  = ascii_huffman(data1, 2)
    print ("Entropy of the text: {0:f}\nExpected length: {1:f}\nOriginal size: {2:d}\nCompression rate: {3:f}".format(H, L, len(data1), 16.0/L))
