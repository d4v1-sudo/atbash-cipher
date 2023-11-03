class Solution:
    def solve(self, text):
        ans = ''
        for char in text:
            if 'a' <= char <= 'z':
                ans += chr(ord('z') - (ord(char) - ord('a')))
            elif 'A' <= char <= 'Z':
                ans += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                ans += char
        return ans

ob = Solution()
request = input("Type the message to invert 'a' in 'z', and so on: ")
print(ob.solve(request))

