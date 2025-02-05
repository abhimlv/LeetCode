class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = "".join(f"{len(word)}#{word}" for word in strs)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_list = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            word = s[j+1: j+1+length]
            decoded_list.append(word)
            i = j + 1 + length
        return decoded_list
