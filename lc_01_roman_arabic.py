# class Solution:
#     def romanToInt(self, s: str) -> int:
#         pass
#
#     def is_s(self)
#         1 <= len(s) <= 15
#         set(s) is in ['I', 'V', 'X', 'L', 'C', 'D', 'M']  # set belongs
#         pass
#
#     def encoding:

result = 0
s = 'MMMDCCXXIV'  # 3724
s2 = 'MMMCMLXXXIV'  # 3984
s3 = 'MMMDCCCLXXXVIII'  # 3888
s4 = 'MMDCCLVII'  # 2757


class Solution:
    def __init__(self):
        self.roman_number = None

    def roman_to_int(self, roman_number: str) -> int:
        self.roman_number = roman_number
        """ function to converse latin numbers into 'arabic number'

        :param roman_number: string of valid roman number
        :return: int result
        """

        # dictionary with keys to represent roman Numbers and values to represent 'arabic numbers'
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # variable to store result of reading next letter
        result = 0
        # looping by str range without last letter
        for letter in range(len(roman_number) - 1):
            # pulling int value from dict and compare it with next letter
            # if latin digit is on the left and is lower than lower of its value the whole result
            if (roman_dict.get(roman_number[letter])) < (roman_dict.get(roman_number[letter + 1])):
                # if number on left is lower from next number is true then number is subtract from result
                result -= (roman_dict.get(roman_number[letter]))
            else:
                # sum otherwise
                result += (roman_dict.get(roman_number[letter]))
        # looping skipped last element as if condition would error with trying to compare last element with next one that
        # does not exist. and last element in roman numbers is always positive so its added now
        result += roman_dict.get((roman_number[len(roman_number) - 1]))
        return result



print(roman_to_int(s))
print(roman_to_int(s2))
print(roman_to_int(s3))
print(roman_to_int(s4))
