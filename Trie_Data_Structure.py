# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        node = self.root # keep moving through nodes. Dont change root
        for character in word:
            if character in node.children:
                node = node.children[character]
            else:
                node.children[character] = Trie()
                node = node.children[character]
        node.endOfWord=True
        #print(node, node.endOfWord)
        #self.traverse(self.root)
    
    def traverse(self, node):
        a = [node]
        while len(a)>0:
            cur_node = a.pop(0)
            for child in cur_node.children:
                print(child, cur_node.endOfWord)
                a.append(cur_node.children[child])
        
        
    def search(self, word: str) -> bool:
        return self.search_helper(word, self.root)
        
    def search_helper(self, word, node):
        #print(node.children, word, node.endOfWord)
        
        for i in range(len(word)):
            character = word[i]
            #print("char", character, node.children, node.endOfWord)
            
            if character==".":
                for child in node.children: # From here there should be atleast one path
                    if self.search_helper(word[i+1:], node.children[child]):
                        return True
                return False
            
            if character not in node.children:
                return False
            
            elif character in node.children:
                return self.search_helper(word[i+1:], node.children[character])
                
        return node.endOfWord
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)