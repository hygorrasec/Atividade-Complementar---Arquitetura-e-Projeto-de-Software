class StringUtils:  # OK.
    def reverse_string(self, s):
        return s[::-1]  # OK.

    def is_palindrome(self, s):
        return s == s[::-1]  # OK.
