class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = []  
        for c in s:
            if c.isalnum():
                news.append(c.lower())
        news = "".join(news)  
        
        l = len(news)
        for i in range(l // 2):  
            if news[i] != news[l - 1 - i]:  
                return False  
        
        return True  
        
