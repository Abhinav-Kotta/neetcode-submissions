class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += word + "\n"

        return res

    def decode(self, s: str) -> List[str]:
        res = s.split("\n")
        res.pop()
        return res