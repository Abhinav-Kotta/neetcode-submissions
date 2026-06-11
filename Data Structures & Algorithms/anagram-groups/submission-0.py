class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappy = {}
        for string in strs:
            s = ''.join(sorted(string))
            if s not in mappy:
                mappy[s] = [string]
            else:
                mappy[s].append(string)

        res = []
        for i in mappy:
            res.append(mappy[i])

        return res