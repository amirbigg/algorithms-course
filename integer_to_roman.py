class Solution(object):
    def intToRoman(self, num):
        roman_symbols = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        roman_values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        roman_string = []

        for symbol, value in zip(roman_symbols, roman_values):
            while num >= value:
                num -= value
                roman_string.append(symbol)
        return ''.join(roman_string)

