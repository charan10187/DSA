class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        res = 0
        prev_value = 0

        # Process from right to left
        for ch in reversed(s.upper()):
            value = roman_values[ch]
            if value < prev_value:
                res -= value  # Subtractive case
            else:
                res += value
            prev_value = value

        return res


# Example usage
s = Solution()
print(s.romanToInt('MCMXCIV'))  # ✅ Output: 1994
