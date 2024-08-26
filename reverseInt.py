import numpy as np

value = 123


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = int(x)
        buffer = np.array(x)
        print(buffer.dtype, np.int32)
        if buffer.dtype != np.int32:
            print("TRUE")
            return 0

        # Convert to string, reverse sequence, convert to int and make negative if initial value was negative
        s = str(abs(x))
        s = s[::-1]
        arr = np.array(int(s))
        arr = arr * -1 if x < 0 else arr
        return arr.item()
        # return arr.item() if -2_147_483_648 <= x <= 2_147_483_647 else 0


result = Solution()
print(result.reverse(value))

# # Pro solution

# val = 123


# tenths = val % 10  # 123 % 10 = 3
# split = val // 10  # 123 / 10 = 12 (floored)
# hundred = split % 10  # 12 % 10 = 2
# firstdigit = split // 10  # 12 // 10 = 1 (floored)
# result = tenths * 100 + hundred * 10 + 1

# print(result)
