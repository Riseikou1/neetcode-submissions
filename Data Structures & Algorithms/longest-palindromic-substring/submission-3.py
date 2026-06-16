class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manacher(s):
            # Step 1: insert '#' between chars (preprocessing)
            t = '#' + '#'.join(s) + '#'
            n = len(t)
            p = [0] * n    # radius array for palindrome lengths
            l, r = 0, 0    # boundaries of current rightmost palindrome

            for i in range(n):
                if i < r:
                    # Use previously computed palindrome info via symmetry
                    mirror = l + (r - i)
                    # p[i] starts at least as the minimum between:
                    # 1) distance to the right boundary, and
                    # 2) palindrome radius at the mirrored position
                    p[i] = min(r - i, p[mirror])
                else:
                    p[i] = 0  # outside the current palindrome, start fresh

                # Try to expand palindrome centered at i
                while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]:
                    p[i] += 1  # expand radius by 1

                # Update current rightmost palindrome if expanded past r
                if i + p[i] > r:
                    l = i - p[i]
                    r = i + p[i]

            return p

        p = manacher(s)
        resLen, center_idx = max((v, i) for i, v in enumerate(p))
        resIdx = (center_idx - resLen) // 2
        return s[resIdx : resIdx + resLen]
