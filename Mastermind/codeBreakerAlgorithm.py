import checkCode as checkCode
def combinationList():
    colors = ['r', 'b', 'g', 'p', 'z', 'w']
    combinations = []
    for color1 in colors:
        for color2 in colors:
            for color3 in colors:
                for color4 in colors:
                    combinations.append([color1, color2, color3, color4])
    return sorted(combinations)

def simpleAlgorithm(positionCorrect, colorCorrect, possibleCode, gameTurn, codeGuess):#A Simple Strategy
    newPossibleCode = []
    newPossibleCode += possibleCode
    feedback = (positionCorrect, colorCorrect)
    if gameTurn > 0:
        newPossibleCode.remove(codeGuess)
        for possibleCode in possibleCode:
            check = checkCode.feedback(codeGuess, possibleCode)
            if check != feedback:
                if possibleCode in newPossibleCode:
                    newPossibleCode.remove(possibleCode)
    return newPossibleCode

def worstCaseAlgorithm(possibleCode):
    colorPossibleFeedback = []
    for color in possibleCode:
        possibleFeedback = [[[0, 0], 0], [[0, 1], 0], [[0, 2], 0], [[0, 3], 0], [[0, 4], 0], [[1, 0], 0], [[1, 1], 0],
                            [[1, 2], 0], [[1, 3], 0], [[2, 0], 0], [[2, 1], 0], [[2, 2], 0], [[3, 0], 0], [[4, 0], 0]]
        for code in possibleCode:
            check = checkCode.feedback(color, code)
            check = [check[0], check[1]]
            indexcounter = 0
            for feedback in possibleFeedback:
                if check == feedback[0]:
                    possibleFeedback[indexcounter][1] += 1
                indexcounter += 1
        possibleFeedback.sort(key=lambda feedback: feedback[1])
        colorPossibleFeedback += [[color, possibleFeedback[-1][1]]]
    colorPossibleFeedback.sort(key=lambda feedback: feedback[1])
    return colorPossibleFeedback[0][0]





# possibleCode = combinationList()
# x = worstCaseAlgorithm(possibleCode)
# print(x)

# def nielsAlgorithm(positionCorrect, colorCorrect, possibleCode, x):#A Simple Strategy
#     oldPossibility = []
#     oldPossibility += possibleCode
#     if x > 0:
#         guesstColor = possibleCode[0]
#         possibleCode.remove(guesstColor)
#         colorCounter = []
#         for c in guesstColor:
#             colorCounter.append([c, guesstColor.count(c)])
#         for s in colorCounter:
#             if s[1] > 2:
#                 keep = s[0]
#         for i in oldPossibility:
#             for color in guesstColor:
#                 if color in i:
#                     if (positionCorrect == 0) and (colorCorrect == 0):
#                         if i in possibleCode:
#                             possibleCode.remove(i)
#                     elif (positionCorrect == 0) and (colorCorrect == 4):
#                         if i not in possibleCode:
#                             possibleCode.remove(i)
#                     elif (positionCorrect == 2) and (colorCorrect == 2):
#                         if i not in possibleCode:
#                             possibleCode.remove(i)
#                     elif (positionCorrect == 1) and (colorCorrect == 2):
#                         if keep not in possibleCode:
#                             possibleCode.remove(i)
#                     elif (positionCorrect == 2) and (colorCorrect == 1):
#                         if keep not in possibleCode:
#                             possibleCode.remove(i)
#     return possibleCode

""""Kooi, B. (2020). YET ANOTHER MASTERMIND STRATEGY. Department of Philosophy, University of Groningen, The Netherlands, 1–10."""