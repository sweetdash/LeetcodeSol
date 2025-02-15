class Solution:
    def checkNonChar(self, a: str) -> bool:
        if ord(a) not in range(48, 58):
            return True
        return False

    def result(self, a: int, res: int) -> int:
        res = res * 10 + int(a)
        return res

    def myAtoi(self, s: str) -> int:
        s = s.strip()
        low, high = 2**31, 2**31
        low = low * -1
        check = list(s)
        sign = 1
        res = 0
        strLen = len(check)
        if strLen == 0:
            return 0
        if check[0] == "-":
            sign = -1
        elif check[0] == "+":
            pass
        elif self.checkNonChar(check[0]):
            return 0
        else:
            res = self.result(check[0], res)
        for i in range(1, strLen):
            if self.checkNonChar(check[i]):
                return (sign * res)
            res = self.result(check[i], res)
            if res not in range(low, high):
                if sign == -1:
                    res = low
                    return res
                else:
                    res = high - 1
                    return res
        return (sign * res)


if __name__ == "__main__":
    s = input("Enter a string: ")
    sol = Solution()
    print(sol.myAtoi(s))
