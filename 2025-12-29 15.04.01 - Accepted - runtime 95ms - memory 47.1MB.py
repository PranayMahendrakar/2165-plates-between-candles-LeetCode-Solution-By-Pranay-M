class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        # Prefix sum of plates
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if s[i] == '*' else 0)
        
        # Nearest candle to the left
        left = [-1] * n
        candle = -1
        for i in range(n):
            if s[i] == '|':
                candle = i
            left[i] = candle
        
        # Nearest candle to the right
        right = [n] * n
        candle = n
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                candle = i
            right[i] = candle
        
        result = []
        for l, r in queries:
            # Find leftmost candle at or after l, rightmost at or before r
            left_candle = right[l]
            right_candle = left[r]
            if left_candle < right_candle:
                result.append(prefix[right_candle + 1] - prefix[left_candle])
            else:
                result.append(0)
        
        return result