# Counts number of 1s and 0s in a word starting with 1s.
def runlength_compression(word_list):

    bit_list = []
    bit_list.append(0)
    c = 0
    btc = True

    for bit in word_list:

        if bit != btc:
            c += 1
            btc = not btc
            bit_list.append(0)

        bit_list[c] += 1

    return bit_list


def runlength_decompression(rl_list):

    word_list = []

    btc = True

    for times in rl_list:
        for c in range(times):
            word_list.append(int(btc))
        btc = not btc

    return word_list
