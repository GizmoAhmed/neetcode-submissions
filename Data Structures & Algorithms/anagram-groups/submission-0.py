class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        grams = {}
        for s in strs:
            gram = "".join(sorted(s))
            print(gram)

            if gram not in grams:
                grams[gram] = len(grams)
                curr = []
                curr.append(s)
                final.append(curr)

            else:
                final[grams[gram]].append(s)
                
        
        print("grams", grams)
        print("final", final) 
        return(final)