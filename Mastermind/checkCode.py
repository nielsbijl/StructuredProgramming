def checkGuess(code, codeGuess):
    print(code)
    positionCorrect = 0
    colorCorrect = 0
    codeList = []
    codeList += codeGuess
    for color in code:
        for p in codeList:
            if color == p:
                colorCorrect += 1
                codeList.remove(p)
                break
    for x in range(len(codeGuess)):
        if codeGuess[x] == code[x]:
            positionCorrect += 1
    colorCorrect -= positionCorrect
    return positionCorrect, colorCorrect