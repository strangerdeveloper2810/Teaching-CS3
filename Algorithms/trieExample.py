class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word


def check_spelling(text, trie):
    words = text.split()
    misspelled_words = []
    for word in words:
        if not trie.search(word):
            misspelled_words.append(word)
    return misspelled_words


# Khởi tạo Trie và thêm danh sách từ vựng
vocabulary = ["một", "hai", "ba", "tư", "lăm", "sáu"]
trie = Trie()
for word in vocabulary:
    trie.insert(word)

# Kiểm tra chính tả trong văn bản
text = input("Mời bạn nhập từ cần kiểm tra: ")
misspelled_words = check_spelling(text, trie)
print(f"Các từ sai chính tả: {', '.join(misspelled_words)}")
