class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        
        word = []
        words = []
        
        for i in range(len(s) - 1):
            if s[i] != ' ':
                word.append(s[i])
                if s[i + 1] == ' ':
                    words.append(''.join(word))
                    word = []
                    
        if word or s[-1] != ' ': 
            word.append(s[-1])
            words.append(''.join(word))
            
        words.reverse()
        
        return " ".join(words)