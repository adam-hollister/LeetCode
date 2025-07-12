class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}

        total = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        total += roman[s[-1]]  # Always add the last symbol
        return total

    def romanToInt2(self, s: str) -> int:
        roman_dic = {
            "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,
            "IV": 4,"IX": 9,"XL": 40,"XC": 90,"CD": 400,"CM": 900
        }
        ans = 0
        i = 0
        while i < len(s):
            if i < len(s)-1 and (s[i] + s[i+1]) in roman_dic:
                    ans += roman_dic[(s[i] + s[i+1])]
                    i+=1
            else:
                ans += roman_dic[s[i]]
            i+=1
        return ans

if __name__ == "__main__":
    sol = Solution()
    assert sol.romanToInt("III") == 3, "Failed 1"
    assert sol.romanToInt("MCMXCIV") == 1994, "Failed 2"
    print("all tests passed")
