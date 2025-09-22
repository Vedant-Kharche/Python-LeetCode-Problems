class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} #defaultdict with list as if elemnet not there goes to next list

        for s in strs: 
            count = [0]*26 # for a to z mapping 
            print("current string is", s)
            for c in s: 
                count[ord(c)-ord("a")]+=1  #using ascii values to find index and incrementing count 
            
            if tuple(count) in res.keys(): 
                temp = res.get(tuple(count))
                print("temp is", temp,type(temp))
                temp.append(s)
                res[tuple(count)] = temp
            else: 
                res[tuple(count)] = [s]

            print("res is", res)
        return res.values()