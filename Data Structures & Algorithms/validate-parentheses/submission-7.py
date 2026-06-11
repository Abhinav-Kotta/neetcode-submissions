class Solution:
    def isValid(self, s: str) -> bool:
        list = []
        dict = {')' : '(', '}' : '{', ']' : '['}
        for c in s:
            if c in dict:
                if list and dict[c] == list[-1]:
                    print("1st here")
                    list.pop()
                else:
                    return False
            else:
                list.append(c)
        
        if not list:
            return True
        else:
            return False

                
