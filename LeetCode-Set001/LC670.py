class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(map(int, str(num)))  # Convert the number to a list of digits
        max_idx = len(digits) - 1  # Start tracking from the last digit
        left_idx, right_idx = -1, -1  # Indices to store the swap positions

        # Traverse the digits from right to left
        for i in range(len(digits) - 1, -1, -1):
            # Update the max_idx if the current digit is greater than the max found so far
            if digits[i] > digits[max_idx]:
                max_idx = i
            # If the current digit is less than the max digit found to the right, mark a potential swap
            elif digits[i] < digits[max_idx]:
                left_idx, right_idx = i, max_idx

        # If there's a valid swap, perform it
        if left_idx != -1:
            digits[left_idx], digits[right_idx] = digits[right_idx], digits[left_idx]

        # Convert the list of digits back to an integer and return the result
        return int(''.join(map(str, digits)))

        
        # digits = []
        # while num:
        #     last_digit = num % 10
        #     num = num // 10
        #     digits.append(last_digit)

        # print(digits)
        # digits = digits[::-1]
        # print(digits)

        # for i in range(len(digits)):
        #     max_digit = digits[i]
        #     max_digit_index = i
        #     for j in range(i+1, len(digits)):
        #         if digits[j] >= max_digit:
        #             max_digit_index = j
        #         max_digit = max(max_digit, digits[j])
        #     if max_digit > digits[i]:
        #         digits[i], digits[max_digit_index] = digits[max_digit_index], digits[i]
        #         break
        # print(digits)
    
        # res = 0
        # for e in digits:
        #     res = res*10 + e
  

        # return res