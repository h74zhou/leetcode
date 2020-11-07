import operator

def solution(min_cheermote_amount, valid_cheermotes, messages):
    cheerMoteDict = {}
    for num, mote in enumerate(valid_cheermotes):
        cheerMoteDict[mote] = num

    def containsCheer(word):
        for cheermote in cheerMoteDict.keys():
            if word.startswith(cheermote):
                return True
        return False

    def getCheer(word):
        for cheermote in valid_cheermotes:
            if word.startswith(cheermote):
                return cheermote

    def getCheerBytes(word, cheer):
        digit = ""
        for i in range(len(cheer), len(word)):
            digit += word[i]
        return int(digit) if len(digit) > 0 else 0

    totalCheerDict = {}
    for message in messages.split(","):
        messageBytesTotal = 0
        tempDict = {}
        for word in message.split():
            if containsCheer(word):
                currCheer = getCheer(word)
                currBytes = getCheerBytes(word, currCheer)
                messageBytesTotal += currBytes
                print messageBytesTotal

                if currBytes > 10000 or messageBytesTotal > 100000 or currBytes < min_cheermote_amount:
                    tempDict = {}
                    break

                tempDict[currCheer] = tempDict.get(currCheer, 0) + currBytes

        for key, val in tempDict.iteritems():
            totalCheerDict[key] = totalCheerDict.get(key, 0) + val

    if len(totalCheerDict) == 0:
        return ["NO_CHEERS"]

    sortedCheerDict = sorted(totalCheerDict.items(), key = operator.itemgetter(1), reverse=True)
    answer = []

    for cheer, val in sortedCheerDict:
        answer.append(cheer + str(val))

    return answer


# print solution(1, ["cheer"], "cheer10000 cheer10000 cheer10000 cheer10000 cheer10000 cheer10000 cheer10000 cheer10000 cheer10000 cheer10000 cheer1, cheer4")
print solution(1, ["cheer"], "cheer1 cheer10001, cheer4")





