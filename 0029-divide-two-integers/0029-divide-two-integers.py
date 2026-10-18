class Solution:

  def divide(self, dividend: int, divisor: int) -> int:
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    if dividend == INT_MIN and divisor == -1:
      return INT_MAX

    negative = (dividend < 0) ^ (divisor < 0)

    dividend = -dividend if dividend > 0 else dividend
    divisor = -divisor if divisor > 0 else divisor

    quotient = 0
    while dividend <= divisor:
      temp_divisor = divisor
      multiple = 1

      while temp_divisor >= -1073741824 and dividend <= (temp_divisor << 1):
        temp_divisor <<= 1
        multiple <<= 1

      dividend -= temp_divisor
      quotient += multiple

    return -quotient if negative else quotient