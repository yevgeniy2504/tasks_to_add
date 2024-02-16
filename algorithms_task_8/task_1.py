"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на примеры с урока,
 сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

from collections import Counter, namedtuple
import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    freq_map = Counter(text)
    priority_queue = [Node(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]


def build_huffman_codes(root, prefix="", codes={}):
    if root is not None:
        if root.char is not None:
            codes[root.char] = prefix
        build_huffman_codes(root.left, prefix + "0", codes)
        build_huffman_codes(root.right, prefix + "1", codes)
    return codes


def huffman_encoding(text):
    if len(text) == 0:
        return "", None

    root = build_huffman_tree(text)
    codes = build_huffman_codes(root)
    encoded_text = ''.join([codes[char] for char in text])
    return encoded_text, root


def huffman_decoding(encoded_text, root):
    if len(encoded_text) == 0:
        return ""

    current_node = root
    decoded_text = ""
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = root

    return decoded_text


if __name__ == "__main__":
    text = "Hello, World!"
    encoded_text, tree = huffman_encoding(text)
    print("Encoded text:", encoded_text)
    decoded_text = huffman_decoding(encoded_text, tree)
    print("Decoded text:", decoded_text)
