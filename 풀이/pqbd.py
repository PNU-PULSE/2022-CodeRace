mirror = {}
turn = {}

ALPHABET =      'abcdefghijklmnopqrstuvwxyz^$#'
MIRROR_STR =    '.d.b....i..lm.oqp....vwx..$^#'
TURN_STR =      '.q.p.......l.uodb.s.n..x.z$^#'

for _key, _value in zip(ALPHABET, MIRROR_STR):
    mirror[_key] = _value
    
for _key, _value in zip(ALPHABET, TURN_STR):
    turn[_key] = _value

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
        
        if T[i] == mirror[T[i]]:
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
        if T[i] == turn[T[i]]:
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

answer_cand = [longestTurnPalindrome(exp_str),longestMirrorPalindrome(exp_str)]
answer_cand = sorted(answer_cand)
answer = max(answer_cand, key=len)
if answer:
    print(answer)
else:
    print("NOANSWER")
