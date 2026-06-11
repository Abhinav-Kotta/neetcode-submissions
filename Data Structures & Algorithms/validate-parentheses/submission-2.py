class Solution:
    def isValid(self, s: str) -> bool:
        list = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in closeToOpen:
                if list and list[-1] == closeToOpen[c]:
                    list.pop()
                else:
                    return False
            else:
                list.append(c)
        
        return True if not list else False

                
