# Each TrieNode represents a single character in the Trie
class TrieNode:
    def __init__(self):
        # children: dictionary mapping character → next TrieNode
        self.children = {}
        # endOfWord: marks if a complete word ends at this node
        self.endOfWord = False


class PrefixTree:
    def __init__(self):
        # The Trie always starts with an empty root node
        self.root = TrieNode()

    # Inserts a full word into the Trie
    def insert(self, word: str) -> None:
        cur = self.root
        
        # Traverse each character in the word
        for c in word:
            # If the character path doesn't exist, create a new TrieNode
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move to the next node in the Trie
            cur = cur.children[c]
        
        # After inserting all characters, mark the end of the word
        cur.endOfWord = True

    # Searches for an exact word in the Trie
    def search(self, word: str) -> bool:
        cur = self.root

        # Traverse the Trie for each character
        for c in word:
            # If at any step the character is missing → word doesn’t exist
            if c not in cur.children:
                return False
            cur = cur.children[c]

        # Must return True only if this node marks the end of a complete word
        return cur.endOfWord

    # Checks if any word in the Trie starts with the given prefix
    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        # Same as search, but we don't care about endOfWord here
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        # If all characters in prefix are found, return True
        return True
