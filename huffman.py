# Creates a table of words and their frequencies.
def create_freq_table(word_list):
    word_list_unique = []

    # Make a list of unique words.
    for word in word_list:
        if word_list_unique.count(word) == 0:
            word_list_unique.append(word)

    freq_list = []

    for word in word_list_unique:
        freq_list.append((word, word_list.count(word)))

    freq_list.sort(key=lambda occ: occ[1])

    return freq_list


# Root and edge special, compound
def generate_codewords(node, path):
    if (isinstance(node, Compound_node)):
        if (path == 2):
            return generate_codewords(node.children[0], '0'), generate_codewords(node.children[1], '1')

        node.set_codeword(path)
        return generate_codewords(node.children[0], node.codeword + '0'), generate_codewords(node.children[1], node.codeword + '1')

    node.set_codeword(path)


# Lazy visualisation of nodes and their values.
def disp_tree(node):
    node.to_text()
    if (isinstance(node, Compound_node)):
        return disp_tree(node.children[0]), disp_tree(node.children[1])


# Recurively constructs a tree from a list of nodes and returns the root node.
def construct_tree(nodes):
    nodes.sort(key=lambda node: node.p)

    if len(nodes) == 1:
        return nodes[0]

    n1 = nodes[0]
    n2 = nodes[1]
    cn = Compound_node(n1, n2)

    return construct_tree([cn] + nodes[2:])


# Returns codeword and word for all nodes in tree.
def get_code(tree):
    if (isinstance(tree, Compound_node)):
        return get_code(tree.children[0]) + get_code(tree.children[1])
    
    return [tree.codeword] + [tree.word]


# For every word in word_list, 'replaces' it with the codeword
def compress(tree, word_list):
    word_code = get_code(tree)

    compressed = []

    for word in word_list:
        code = word_code[word_code.index(word) - 1]

        code_list = []

        for bit in code:
            code_list.append(int(bit))

        compressed.append(code_list)

    return compressed


# Decompression using traversal of tree.
def decompress(tree, compressed):
    word_list = []
    
    for code in compressed:
        node = tree

        for path in code:
            node = node.children[path]
        word_list.append(node.word)

    return word_list


# Creates a tree from given list of words and the compressed version of the list of words. 
def encode(word_list, p):

    no_words = len(word_list)

    freq_table = create_freq_table(word_list)

    nodes = []

    for occ in freq_table:
        nodes.append(Node(occ[0], occ[1]/no_words))

    tree = construct_tree(nodes)

    generate_codewords(tree, 2)

    return tree, compress(tree, word_list)



class Node:
    def __init__(self, word, p):
        self.word = word
        self.p = p
        self.codeword = ''

    def set_codeword(self, codeword):
        self.codeword = codeword

    def set_parent(self, parent):
        self.parent = parent

    def to_text(self):
        print("\n\nWord: ", self.word, "\np: ",
              self.p, "\nCodeword: ", self.codeword)


class Compound_node(Node):
    def __init__(self, node1, node2):
        Node.__init__(self, None, node1.p + node2.p)
        node1.set_parent(self)
        node2.set_parent(self)
        self.children = [node1, node2]