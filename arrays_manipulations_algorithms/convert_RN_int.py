class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        # also, iterate over the string. if one char is smaller than the one follwing, subtract otherwise add
        len_s = len(s)
        count = 0
        for i, v in enumerate(s):
            if i + 1 == len_s: # 1,2,3
                return count + my_dict[v]
            nex_value = s[i+1]
            if my_dict[v] < my_dict[nex_value]:
                count = count - my_dict[v]
            else:
                count = count + my_dict[v]

Sol = Solution()
print(Sol.romanToInt('III'))
print(Sol.romanToInt("LVIII"))
print(Sol.romanToInt('MCMXCIV'))