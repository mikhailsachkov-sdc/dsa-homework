class Solution:
    def toHex(self, num: int) -> str:

        if num == 0:
            return "0"

        if num < 0:
            num += 2 ** 32

        result = ""

        HEX_DIGITS = "0123456789abcdef"
        while num > 0:
            digit = num & 0xf
            result = HEX_DIGITS[digit] + result
            num >>= 4

        return result

