import random
import math
import runlength
import huffman


# Generates a list of bits with optional weighted probability and seed.
def rand_bin_word(length, p=0.5, seed=None):
    assert(p < 1)
    random.seed(seed)
    bit_string = [1 for i in range(round(length*p))] + \
        [0 for i in range(round(length*(1 - p)))]

    return random.sample(bit_string, length)


def verify_compression(original, decompressed):
    assert original == decompressed, "Not equal"
    print("Compression ok.")


def test_huffman():
    p = 0.4
    word_len = 4
    words = 64

    word_list = []

    for i in range(words):
        word_list.append(rand_bin_word(word_len, p))
    
    [tree, compressed] = huffman.encode(word_list, p)

    decompressed = huffman.decompress(tree, compressed)

    verify_compression(word_list, decompressed)

    
    entr = tree.entropy()
    ml = tree.m_L()
    
    tree.disp_tree()

    print("Entropy:\t\t", entr)
    print("m_L:\t\t\t", ml)
    print("Redundance:\t\t", ml - entr)
    print("Compression ratio:\t", huffman.compression_ratio(tree, ml))


#test_rl()
test_huffman()
