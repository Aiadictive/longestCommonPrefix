class Solution:
    def longestCommonPrefix(self,strs):
        if (strs == None or len(strs) == 0):
            return ""
        i=0
        while i < len(strs[0]):             
            c=strs[0][i:i+1]
            j=1
            while  j < len(strs):
                if (i == len(strs[j]) or strs[j][i:i+1] != c):
                    return strs[0][0:i]
                j=j+1
            i=i+1        
        return strs[0]
def main():
    sol=Solution()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))
if __name__=="__main__":
    main()