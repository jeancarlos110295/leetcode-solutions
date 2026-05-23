# Link: https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""

        nums_romanos = [
            {"symbol" : "M", "value" : 1000},
            {"symbol" : "CM", "value" : 900},
            {"symbol" : "D", "value" : 500},
            {"symbol" : "CD", "value" : 400},
            {"symbol" : "C", "value" : 100},
            {"symbol" : "XC", "value" : 90},
            {"symbol" : "L", "value" : 50},
            {"symbol" : "XL", "value" : 40},
            {"symbol" : "X", "value" : 10},
            {"symbol" : "IX", "value" : 9},
            {"symbol" : "V", "value" : 5},
            {"symbol" : "IV", "value" : 4},
            {"symbol" : "I", "value" : 1},
        ]

        for num_romano in nums_romanos:
            sysmbol = num_romano["symbol"]
            value = num_romano["value"]

            while num >= value:
                result += sysmbol
                num -= value

        return result




ins_Solution = Solution()

print( ins_Solution.intToRoman(3749) )





