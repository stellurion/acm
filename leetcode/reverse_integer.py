class Solution:
    def reverse(self, x: int) -> int:
        sum = 0

        save = (abs(x))
        counter = pow(10, len(str(save))-1)

        while(counter > 0):
            digit = save % 10
            print(digit)
            sum += (digit * counter)

            counter = counter//10
            save = save//10

        sum = sum if x > 0 else 0-sum
        return sum if abs(sum) < 0x7FFFFFFF else 0
