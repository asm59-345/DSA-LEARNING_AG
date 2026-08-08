class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        count = s.count(letter)  # Total remaining 'letter's in s from index i onwards
        in_stack_letter = 0     # Count of 'letter' currently in stack
        stack = []
        n = len(s)

        for i, ch in enumerate(s):
            # Maintain monotonic increasing stack order while satisfying constraints
            while stack and stack[-1] > ch:
                # 1. Check if we have enough elements left to form a subsequence of length k
                if len(stack) + (n - i) <= k:
                    break
                # 2. If popping 'letter', check if remaining 'letter's can satisfy 'repetition'
                if stack[-1] == letter and in_stack_letter + count - 1 < repetition:
                    break
                
                popped = stack.pop()
                if popped == letter:
                    in_stack_letter -= 1

            # Append character if conditions allow
            if len(stack) < k:
                if ch == letter:
                    stack.append(ch)
                    in_stack_letter += 1
                elif k - len(stack) > repetition - in_stack_letter:
                    stack.append(ch)

            if ch == letter:
                count -= 1

        return "".join(stack)