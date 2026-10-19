class Solution:
    def isPalindrome(self, s: str) -> bool:
        # print("Z: ", "z".isalnum())
        # print("?: ", "?".isalnum())
        # print("1: ", "1".isalnum())
        # print(":: ", ":".isalnum())

        i = 0 
        j = len(s) - 1
        while i < j:
            front = s[i].lower()
            back = s[j].lower()
            while not back.isalnum():
                j -= 1
                back = s[j].lower()
                if j < i:
                    return True
            while not front.isalnum():
                i += 1
                front = s[i].lower()
                if j < i:
                    return True

            print("front: ", front)
            print("back: ", back)

            if front != back:
                return False
            i += 1
            j -= 1
        
        return True

        