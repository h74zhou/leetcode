import sys


def solution(S):
    # given string S
    # return min number of moves required to obtain a string
    # containing no instances of 3 identical consecutive letters
    if len(S) < 3:
        return 0

    count, answer = 1, 0
    prevLetter = S[0]

    for i in range(1, len(S)):
        letter = S[i]
        if letter == prevLetter:
            count += 1
            if count >= 3:
                answer += count / 3
                count = 0
        else:
            prevLetter = letter
            count = 1
    return answer

print solution("baaaab")
print solution("baaaaab")
print solution("baaaaaaaaab")
