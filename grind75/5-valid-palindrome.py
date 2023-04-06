class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create a string, add if character is alphanumeric
        # create a reverseed string
        # check if the strings are equal
        s = s.casefold()
        string = ''
        for char in s:
            if char.isalnum():
                string += char

        reverse = string[::-1]

        return string == reverse