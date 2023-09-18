class Converter:
    def __init__(self):
      self.conversion_table = {}

    def convert(self, value):
        raise NotImplementedError("Please implement this method in the subclass!")
    
class NumToRoman(Converter):
    def __init__(self):
        super().__init__()
        self.conversion_table = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
            90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }
        self.values = sorted(self.conversion_table.keys(), reverse=True)

    def convert(self, s_num):
        num = int(s_num)
        roman_num = ''
        for value in self.values:
            while num >= value:
                roman_num += self.conversion_table[value]
                num -= value
        return roman_num

class RomanToNum(Converter):
    def __init__(self):
        super().__init__()
        self.conversion_table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def convert(self, s):
        total = 0
        prev_value = 0
        for c in s:
            value = self.conversion_table.get(c, -1)
            if value == -1:
                raise ValueError("Invalid Roman numeral!")
            if value > prev_value:
                total += value - 2 * prev_value
            else:
                total += value
            prev_value = value
        return total
