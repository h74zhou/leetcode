def candyCrush1D(str):
    stack = []

    for letter in str:
        if len(stack) == 0:
            stack.append((letter, 1))
        else:
            topLetter, amt = stack.pop()
            if topLetter == letter:
                stack.append((topLetter, amt + 1))
            else:
                if amt < 3:
                    stack.append((topLetter, amt))
                stack.append((letter, 1))

    if len(stack) > 0:
        topLetter, amt = stack.pop()
        if amt < 3:
            stack.append((topLetter, amt))

    answer = ""
    for letter, amt in stack:
        answer += letter * amt

    return answer


input1, output1 = "aaabbbc", "c"
input2, output2 = "aabbbacd", "cd"
input3, output3 = "aabbccddeeedcba", ""
input4, output4 = "aaabbbacd", "acd"

print "Test 1 Passed" if candyCrush1D(input1) == output1 else "Test 1 Failed"
print "Test 2 Passed" if candyCrush1D(input1) == output1 else "Test 2 Failed"
print "Test 3 Passed" if candyCrush1D(input1) == output1 else "Test 3 Failed"
print "Test 4 Passed" if candyCrush1D(input1) == output1 else "Test 4 Failed"
