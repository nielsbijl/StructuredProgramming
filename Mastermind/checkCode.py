def feedback(code, codeGuess):
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
    for i in range(len(codeGuess)):
        if codeGuess[i] == code[i]:
            positionCorrect += 1
    colorCorrect -= positionCorrect
    return positionCorrect, colorCorrect