def mastermind():
    mastermindPlayerChoice()
    gameRules()




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
    print("\nDit zijn de spelregels:\n"
          "De Code-bedenker verzint een code van 4 kleuren, er 6 zijn kleuren om uit te kiezen.\n"
          "De kleuren in de code mogen meer dan 1 keer voorkomen.\n"
          "De Code-kraker mag proberen de kleurencode te kraken door te gokken.\n"
          "De Code-kraker heeft 10 pogingen.\n"
          "Rechts van de kleuren combinatie zie je hoeveel kleuren in de juiste positie staan.\n"
          "Daarnaast staan hoeveel van de gekozen kleuren in de codecombinatie voorkomen.")




mastermind()