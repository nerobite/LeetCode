"""
Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.
Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals:
1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
2008 is written as 2000=MM, 8=VIII; or MMVIII
1666 uses each Roman symbol in descending order: MDCLXVI.
Input range : 1 <= n < 4000
In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
Examples
to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
86 -> "LXXXVI"
1 -> "I"
from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"LXXXVI"  ->   86
"I"       ->    1
Help
+--------+-------+
| Symbol | Value |
+--------+-------+
|    M   |  1000 |
|   CM   |   900 |
|    D   |   500 |
|   CD   |   400 |
|    C   |   100 |
|   XC   |    90 |
|    L   |    50 |
|   XL   |    40 |
|    X   |    10 |
|   IX   |     9 |
|    V   |     5 |
|   IV   |     4 |
|    I   |     1 |
+--------+-------+
"""
class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        dictory = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM"
        }
        dic_l = sorted(dictory, reverse=True)
        result = ""
        for i in dic_l:
            while val - i >= 0:
                val -= i
                result += dictory[i]
        return result

    @staticmethod
    def from_roman(roman_num : str) -> int:
        dictory = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        result = 0
        i = 0
        while i < len(roman_num):
            if i < len(roman_num) - 1 and roman_num[i] + roman_num[i + 1] in dictory:
                result += dictory[roman_num[i] + roman_num[i + 1]]
                i += 2
            else:
                result += dictory[roman_num[i]]
                i += 1
        return result
