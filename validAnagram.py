"""First attempt below, uses arrays and .sort() as this removes duplicates, after this lengths are taken and if they are the same length then they are anagrams"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        array1=[]
        array2=[]

        length=len(s)
        for letter in range(0,length):
            array1.append(str(s)[letter])
        
        length=len(t)
        for letter in range(0,length):
            array2.append(str(t)[letter])

        CompS=array1.sort()
        CompT=array2.sort()

        if array1==array2:
            return True
        return False  


"""Second attempt below uses a hashmap to check the quantity of each letter, if they match then the words are anagrams"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        CountT,CountS={},{}

        for item in range(len(s)):
            CountS[s[item]]=1+CountS.get(s[item],0)
            CountT[t[item]]=1+CountT.get(t[item],0)
        return CountS==CountT
