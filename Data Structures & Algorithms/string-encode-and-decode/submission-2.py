class Solution:

    def encode(self, strs: List[str]) -> str:
        combined_string = ''
        for s in strs:
            combined_string += s + '\n'

        return combined_string
    def decode(self, s: str) -> List[str]:
        decoded_string = []
        word = ''
        for character in s:
            if character == '\n':
                decoded_string.append(word)
                word = ''
            else:
                word += character

        return decoded_string

