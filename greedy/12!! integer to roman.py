class Solution:
    def intToRoman(self, num: int) -> str:
        val_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]

        ans = []
        for val, symbol in val_map:
            while num >= val:
                ans.append(symbol)
                num -= val
        return ''.join(ans)

    def intToRomanBrute(self, num:int) -> str:
        roman_dic = {1:"I", 5:"V", 10:"X",50:"L",100:"C",500:"D",1000:"M"}
        ans = ""
        while num > 0:
            if num >= 1000:
                ans += "M"
                num -= 1000

            elif num >= 900:
                ans += "CM"
                num -= 900

            elif num >= 500:
                ans += "D"
                num -= 500

            elif num >= 400:
                ans += "CD"
                num -= 400

            elif num >= 100:
                ans += "C"
                num -= 100

            elif num >= 90:
                ans += "XC"
                num -= 90

            elif num >= 50:
                ans += "L"
                num -= 50

            elif num >= 40:
                ans += "XL"
                num -= 40

            elif num >= 10:
                ans += "X"
                num -= 10

            elif num >= 9:
                ans += "IX"
                num -= 9

            elif num >= 5:
                ans += "V"
                num -= 5

            elif num >= 4:
                ans += "IV"
                num -= 4

            elif num >= 1:
                ans += "I"
                num -= 1

        return ans

if __name__ == "__main__":
    sol = Solution()
    assert sol.intToRoman(3749) == "MMMDCCXLIX", "Failed 1"
    assert sol.intToRoman(58) == "LVIII", "Failed 2"
    print("all tests passed")
