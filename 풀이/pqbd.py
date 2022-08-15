mirror = {}
turn = {}

mirror['a'] = '.'
mirror['b'] = 'd'
mirror['c'] = '.'
mirror['d'] = 'b'
mirror['e'] = '.'
mirror['f'] = '.'
mirror['g'] = '.'
mirror['h'] = '.'
mirror['i'] = 'i'
mirror['j'] = '.'
mirror['k'] = '.'
mirror['l'] = 'l'
mirror['m'] = 'm'
mirror['n'] = 'n'
mirror['o'] = 'o'
mirror['p'] = 'q'
mirror['q'] = 'p'
mirror['r'] = '.'
mirror['s'] = '.'
mirror['t'] = '.'
mirror['u'] = '.'
mirror['v'] = 'v'
mirror['w'] = 'w'
mirror['x'] = 'x'
mirror['y'] = '.'
mirror['z'] = '.'
mirror['^'] = '$'
mirror['$'] = '^'
mirror['#'] = '#'

turn['a'] = '.'
turn['b'] = 'q'
turn['c'] = '.'
turn['d'] = 'p'
turn['e'] = '.'
turn['f'] = '.'
turn['g'] = '.'
turn['h'] = '.'
turn['i'] = '.'
turn['j'] = '.'
turn['k'] = '.'
turn['l'] = 'l'
turn['m'] = '.'
turn['n'] = '.'
turn['o'] = 'o'
turn['p'] = 'd'
turn['q'] = 'b'
turn['r'] = '.'
turn['s'] = 's'
turn['t'] = '.'
turn['u'] = '.'
turn['v'] = '.'
turn['w'] = '.'
turn['x'] = 'x'
turn['y'] = '.'
turn['z'] = 'z'
turn['^'] = '$'
turn['$'] = '^'
turn['#'] = '#'

def longestMirrorPalindrome(s):
    # Transform S into T.
    # For example, S = "abba", T = "^#a#b#b#a#$".
    # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n
    C = R = 0
    for i in range (1, n-1):
        P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
        # Attempt to expand palindrome centered at i
        
        while i - 1 - P[i] >= 0 and T[i + 1 + P[i]] == mirror[T[i - 1 - P[i]]]:
            P[i] += 1

        # If palindrome centered at i expand past R,
        # adjust center based on expanded palindrome.
        if i + P[i] > R:
            C, R = i, i + P[i]

    # Find the maximum element in P.
    maxLen, CI = max((n, i) for i, n in enumerate(P))
    candidates = [(n, i) for i, n in enumerate(P) if n == maxLen]
    answer_string = min([s[(centerIndex[1]  - maxLen)//2: (centerIndex[1]  + maxLen)//2] for centerIndex in candidates])
    return answer_string
    
def longestTurnPalindrome(s):
    # Transform S into T.
    # For example, S = "abba", T = "^#a#b#b#a#$".
    # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n
    C = R = 0
    for i in range (1, n-1):
        P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
        # Attempt to expand palindrome centered at i
        while i - 1 - P[i] >= 0 and T[i + 1 + P[i]] == turn[T[i - 1 - P[i]]]:
            P[i] += 1

        # If palindrome centered at i expand past R,
        # adjust center based on expanded palindrome.
        if i + P[i] > R:
            C, R = i, i + P[i]

    # Find the maximum element in P.
    maxLen, CI = max((n, i) for i, n in enumerate(P))
    candidates = [(n, i) for i, n in enumerate(P) if n == maxLen]
    answer_string = min([s[(centerIndex[1]  - maxLen)//2: (centerIndex[1]  + maxLen)//2] for centerIndex in candidates])
    return answer_string
    
# exp_str= "ppbboqqbboqqppoddppoddqq"
# exp_str = "aaapqbdcksppddxbboqqppodd"
exp_str = input().strip()


print(max([longestTurnPalindrome(exp_str),longestMirrorPalindrome(exp_str)], key=len))
