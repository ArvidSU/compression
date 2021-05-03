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


# Count number of elements in list recusively. Assuming a non-bit element is a byte long.
def size_bits(word_list):
    #print(word_list)
    if isinstance(word_list, list):
        if len(word_list) == 0:
            return 0
        return size_bits(word_list[0]) + size_bits(word_list[1:])
    elif word_list == 1 or word_list == 0:
        return 1
    else:
        return 8


# Not very thought out function to get the compression ratio.
def compression_ratio(original, compressed):
    print("Compression ratio: ", size_bits(compressed)/size_bits(original))


# Binary entropy function. (Might need some adjustments and ensurance of correct usage.)
def bin_entropy(p):
    if (p == 1):
        print("Entropy: ", 1)
    print("Entropy: ", -p*math.log2(p) - (1 - p)*math.log2(1 - p))


# Deprecated 🙃🙃
def test_rl():
    p = 0.3
    word_list = rand_bin_word(64, p)

    rl_comp = runlength.runlength_compression(word_list)

    rl_decomp = runlength.runlength_decompression(rl_comp)


    verify_compression(word_list, rl_decomp)
    bin_entropy(p)
    compression_ratio(word_list, rl_comp)


def test_huffman():
    p = 0.4
    word_len = 4
    words = 32

    word_list = []

    for i in range(words):
        word_list.append(rand_bin_word(word_len, p))
    
    [tree, compressed] = huffman.encode(word_list, p)

    decompressed = huffman.decompress(tree, compressed)

    verify_compression(word_list, decompressed)
    bin_entropy(p)
    compression_ratio(word_list, compressed)


#test_rl()
test_huffman()
