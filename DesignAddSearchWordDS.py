class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes (character -> TrieNode)
        self.children = {}
        
        # True if a complete word ends at this node
        self.word = False


class WordDictionary:
    def __init__(self):
        # Root node of the Trie (empty node)
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Start from the root of the Trie
        cur = self.root

        # Insert each character of the word
        for c in word:
            # If the character does not exist, create a new node
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            # Move to the child node
            cur = cur.children[c]

        # Mark the end of the word
        cur.word = True

    def search(self, word: str) -> bool:
        # Depth First Search helper function
        # j -> current index in the word
        # root -> current TrieNode
        def dfs(j, root):
            cur = root

            # Traverse characters starting from index j
            for i in range(j, len(word)):
                c = word[i]

                # Case 1: wildcard '.'
                # It can match ANY character
                if c == ".":
                    # Try all possible child nodes
                    for child in cur.children.values():
                        # If any path returns True, word exists
                        if dfs(i + 1, child):
                            return True
                    # If none match
                    return False

                # Case 2: normal character
                else:
                    # If character does not exist in children, fail
                    if c not in cur.children:
                        return False
                    
                    # Move to the next Trie node
                    cur = cur.children[c]

            # After processing all characters,
            # return True only if it's a complete word
            return cur.word

        # Start DFS from index 0 and root node
        return dfs(0, self.root)
