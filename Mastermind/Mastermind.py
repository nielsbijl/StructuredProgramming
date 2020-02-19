import codeBreakerAlgorithm as breaker
import checkCode as checkCode
import time
import random
def mastermind():
    codeGuess = [' ', ' ', ' ', ' ']
    print(gameRules())
    player = mastermindPlayerChoice()
    gameBord = gameBordCreateEmptyBord()
    for emptyGameBordLine in gameBord:
        print(emptyGameBordLine)
    if player == 'kraker':
        code = randomCode()
    else:
        print("Verzin de geheime code!")
        code = chooseColor()
        algorithm = input("Welk algoritme wilt u runnen? [random/simple/worstcase]")
    possibleCode = breaker.combinationList() #Lijst met alle mogelijke codes
    for gameTurn in range(10):       #Vanaf hier beginnen de 10 beurten
        if player == 'kraker':
            codeGuess = chooseColor()
        else:
            check = checkCode.feedback(code, codeGuess)
            positionCorrect = check[0]
            colorCorrect = check[1]
            if algorithm == 'random':
                codeGuess = randomCode()
            elif algorithm == "simple":
                possibleCode = breaker.simpleAlgorithm(positionCorrect, colorCorrect, possibleCode, gameTurn, codeGuess)
                codeGuess = possibleCode[0]
            elif algorithm == "worstcase":
                possibleCode = breaker.simpleAlgorithm(positionCorrect, colorCorrect, possibleCode, gameTurn, codeGuess)
                codeGuess = breaker.worstCaseAlgorithm(possibleCode)
        gameBord = gameBordUpdate(code, gameBord, codeGuess)
        if gameBord == True:
            print('De code is gekraakt!!! Het kostte : ' + str(
                gameTurn + 1) + ' beurten! \n')
            break
        else:
            for gameBordLines in gameBord:
                print(gameBordLines)
def gameBordUpdate(code, gameBord, codeGuess):
    print("\n")
    check = checkCode.feedback(code, codeGuess)
    positionCorrect = check[0]
    colorCorrect = check[1]
    gameBord = gameBordCreate(gameBord[1:], codeGuess, positionCorrect, colorCorrect)
    if codeGuess == code:
        return True
    else:
        return gameBord
def gameBordCreateEmptyBord():
    gameBord = []
    codeGuess = [' ', ' ', ' ', ' ']
    positionCorrect = 0
    colorCorrect = 0
    for emptyGameBordLine in range(10):
        gameBord = gameBordCreate(gameBord, codeGuess, positionCorrect, colorCorrect)
    return gameBord
def gameBordCreate(gameBord, codeGuess, positionCorrect, colorCorrect):
    gameBordFullPlus = ["({})({})({})({})  [{}][{}] ".format(codeGuess[0], codeGuess[1], codeGuess[2], codeGuess[3], positionCorrect, colorCorrect)]
    gameBord = gameBord + gameBordFullPlus
    return gameBord
def chooseColor():
    print("\n(R)ood, (B)lauw, (G)roen, (P)aars, (Z)wart en (W)it [r/b/g/p/z/w]")
    codeGuess = []
    for x in range(4):
        color = ""
        while (color not in ['r', 'b', 'g', 'p', 'z', 'w']):
            color = (input("Kies kleur {}: ".format(x+1))).lower()
        codeGuess.append(color)
    return codeGuess
def randomCode():
    import random
    code = []
    for x in range(4):
        code += random.choice(['r', 'b', 'g', 'p', 'z', 'w'])
    return code
def mastermindPlayerChoice():
    player = 'error'
    while player == 'error':
        playerChoice = input("Welke speler wilt u zijn? Code-kraker of Code-bedenker[kraker/bedenker]: ")
        if 'kraker' in playerChoice:
            player = 'kraker'
        elif 'bedenker' in playerChoice:
            player = 'bedenker'
        else:
            player = 'error'
            print("Voer een geldige speler in!!")
    print("U bent player: " + player)
    return player
def gameRules():
    rules = ("\nDit zijn de spelregels:\n"
          "De Code-bedenker verzint een code van 4 kleuren, er 6 zijn kleuren om uit te kiezen ( )( )( )( ).\n"
          "De kleuren in de code mogen meer dan 1 keer voorkomen.\n"
          "De Code-kraker mag proberen de kleurencode te kraken door te gokken.\n"
          "De Code-kraker heeft 10 pogingen.\n"
          "Rechts van de kleuren combinatie zie je hoeveel kleuren in de juiste positie staan [].\n"
          "Daarnaast staan hoeveel van de gekozen kleuren in de codecombinatie voorkomen [].\n"
          "Het spel bestaat uit de volgende kleuren: (R)ood, (B)lauw, (G)roen, (P)aars, (Z)wart en (W)it\n")
    return rules



mastermind()