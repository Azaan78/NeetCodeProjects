
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
