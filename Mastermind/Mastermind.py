def mastermind():
    print(gameRules())
    player = mastermindPlayerChoice()
    if player == 'kraker':
        print('\n\n')
        gameBord = []
        for i in range(10):
            gameBordEmptyPlus = ["({})({})({})({})  [{}][{}] ".format(' ', ' ', ' ', ' ', ' ', ' ')]
            gameBord = gameBord + gameBordEmptyPlus
        for emptylines in gameBord:
            print(emptylines)
        print('\n')
        code = randomCode()
        for x in range(10):
            codeGuess = guess()
            gameBord = kraker(code, gameBord[1:] , codeGuess)
            for lines in gameBord:
                print(lines)
            if codeGuess == code:
                print('Je bent een mastermind, het is je gelukt de code te kraken!')
                break

def kraker(code, gameBord, codeGuess):
        positionCorrect = 0
        colorCorrect = 0
        for p in code:
            if p in codeGuess:
                colorCorrect += 1
        for x in range(len(codeGuess)):
            if codeGuess[x] == code[x]:
                positionCorrect += 1
        gameBordFullPlus = ["({})({})({})({})  [{}][{}] ".format(codeGuess[0], codeGuess[1], codeGuess[2], codeGuess[3], positionCorrect, colorCorrect)]
        gameBord = gameBord + gameBordFullPlus
        print(gameBord)
        print(code)
        print('\n')
        return gameBord
def guess():
    print("\n(R)ood, (B)lauw, (G)roen, (P)aars, (Z)wart en (W)it")
    color1 = input('Kleur1: ')
    color2 = input('Kleur2: ')
    color3 = input('Kleur3: ')
    color4 = input('Kleur4: ')
    codeGuess = [color1, color2, color3, color4]
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
        playerChoice = input("Welke speler wilt u zijn? Code-kraker of Code-bedenker: ")
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
          "De Code-bedenker verzint een code van 4 kleuren, er 6 zijn kleuren om uit te kiezen.\n"
          "De kleuren in de code mogen meer dan 1 keer voorkomen.\n"
          "De Code-kraker mag proberen de kleurencode te kraken door te gokken.\n"
          "De Code-kraker heeft 10 pogingen.\n"
          "Rechts van de kleuren combinatie zie je hoeveel kleuren in de juiste positie staan.\n"
          "Daarnaast staan hoeveel van de gekozen kleuren in de codecombinatie voorkomen.\n"
          "Het spel bestaat uit de volgende kleuren: (R)ood, (B)lauw, (G)roen, (P)aars, (Z)wart en (W)it\n")
    return rules



mastermind()