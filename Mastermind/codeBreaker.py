def combinationList():
    colors = ['r', 'b', 'g', 'p', 'z', 'w']
    combinations = []
    for color1 in colors:
        for color2 in colors:
            for color3 in colors:
                for color4 in colors:
                    combinations.append([color1, color2, color3, color4])
    return sorted(combinations)

def simple(positionCorrect, colorCorrect, possibility, x):#A Simple Strategy
    oldPossibility = []
    oldPossibility += possibility
    if x > 0:
        guesstColor = possibility[0]
        possibility.remove(guesstColor)
        colorCounter = []
        for c in guesstColor:
            colorCounter.append([c, guesstColor.count(c)])
        for s in colorCounter:
            if s[1] > 2:
                keep = s[0]
        for i in oldPossibility:
            for color in guesstColor:
                if color in i:
                    if (positionCorrect == 0) and (colorCorrect == 0):
                        if i in possibility:
                            possibility.remove(i)
                    elif (positionCorrect == 0) and (colorCorrect == 4):
                        if i not in possibility:
                            possibility.remove(i)
                    elif (positionCorrect == 2) and (colorCorrect == 2):
                        if i not in possibility:
                            possibility.remove(i)
                    elif (positionCorrect == 1) and (colorCorrect == 2):
                        if keep not in possibility:
                            possibility.remove(i)
                    elif (positionCorrect == 2) and (colorCorrect == 1):
                        if keep not in possibility:
                            possibility.remove(i)
    return possibility
