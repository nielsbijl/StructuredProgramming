"""*************** OPDRACHT 1 ---- PYRAMIDE*************"""
def Pyramide():
    PyramideSize = int(input("Hoe groot?"))
    minus = False
    counter = 1
    while counter != 0:
        print("*" * counter)
        if counter == PyramideSize:
            minus = True
        if minus:
            counter -= 1
        else:
            counter += 1
def PyramideForLoop():
    PyramideSize = int(input("Hoe groot?"))
    size = (PyramideSize * 2) - 1
    minus = False
    counter = 1
    for x in range(size):
        print("*" * counter)
        if counter == PyramideSize:
            minus = True
        if minus:
            counter -= 1
        else:
            counter += 1
def PyramideReverse():
    PyramideSize = int(input("Hoe groot?"))
    minus = False
    counter = 1
    while counter != 0:
        whitespace = PyramideSize - counter
        print(" " * whitespace + "*" * counter)
        if counter == PyramideSize:
            minus = True
        if minus:
            counter -= 1
        else:
            counter += 1
def PyramideReverseForLoop():
    PyramideSize = int(input("Hoe groot?"))
    size = (PyramideSize * 2) - 1
    minus = False
    counter = 1
    for x in range(size):
        whitespace = PyramideSize - counter
        print(" " * whitespace + "*" * counter)
        if counter == PyramideSize:
            minus = True
        if minus:
            counter -= 1
        else:
            counter += 1
"""************OPDRACHT 2 --------- TEKSTCHECK******************8"""
def StringCheck():
    string1 = input("geef een string")
    string2 = input("geef een string")
    if len(string1) > len(string2):
        string = string1[:len(string2)]
    elif len(string2) > len(string1):
        string = string2[:len(string1)]
    else:
        string = string1

    if string1 == string2:
        print('De twee zinnen zijn identiek aan elkaar!')
    else:
        for index in range(len(string)):
            if string1[index] != string2[index]:
                print("Het eerste verschil zit op index: " + str(index))

"""***************OPDRACHT 3 -------- LIJSTCHEK*******************"""
def count(lst, getalX):
    counter = 0
    for x in lst:
        if x == getalX:
            counter += 1
    return counter
def difference(lst):
    if len(lst) <= 1:
        return "Your list need at least 2 items"
    return max(lst) - min(lst)
def zeroOne(lst):
    one = count(lst, 1)
    zero = count(lst, 0)
    if one > zero and zero <= 12:
        return True
    else:
        return False
"""**************OPDRACHT 4 ---------- PALINDROOM***************"""
def palindroom(string):
    reversedString = ""
    index = len(string)
    while index > 0:
        reversedString += string[index - 1]
        index = index - 1
    if reversedString == string:
        return True
    else:
        return False
"""******************OPDACHT 5 ---- SORTEREN****************"""
def sort(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
"""****************OPDRACHT 6-------- Gemiddelde berekenen*************"""
def everedgeList(lst):
    total = 0
    for x in lst:
        total = total + int(x)
    return total / len(lst)
def everedgeListInList(lst):
    total = 0
    sumListLength = 0
    for list in lst:
        sumListLength = sumListLength + len(list)
        for x in list:
            total = total + int(x)
    return total / sumListLength
"""****************OPDRACHT 7-------- Random*************"""
def random():
    import random
    x = True
    while x:
        randomInt = random.randrange(0, 10)
        guestInt = int(input("Give me a number between 0-10: "))
        if randomInt == guestInt:
            print("You did it!")
            x = False
"""****************OPDRACHT 8------- Compressie*************"""
def compress():
    with open("textfile.txt", "r") as file:
        lines = file.readlines()
        string = ''
        for line in lines:
            line = line.lstrip()
            string = string + line
    with open("newfile.txt", "w") as newfile:
        newfile.write(string)
"""****************OPDRACHT 9------- Cyclisch verschuiven*************"""
def bitShift(ch, n):
    bit = str(ch)
    if n > 0:
        for x in range(n):
            removedBit = bit[0]
            bit = bit[1:]
            bit = bit + removedBit
    elif n < 0:
        for x in range(abs(n)):
            removedBit = bit[-1]
            bit = bit[:-1]
            bit = removedBit + bit
    else:
        bit = "n is invalid"
    return bit
"""****************OPDRACHT 10------- Fibonaci*************"""
def fibonacci(lst, n):
    if n >= 1:
        n -= 1
        sum = lst[-1] + lst[-2]
        lst.append(sum)
        return fibonacci(lst, n)
    else:
        return lst
"""****************OPDRACHT 11------- Caesarcijfer*************"""
def caesarTranslate():
    import string
    alphabet = string.ascii_lowercase
    alphabetUppercase = string.ascii_uppercase
    text = input("Geef een tekst: ")
    rotation = int(input("Geef een rotatie: "))
    newsentence = ''
    for letter in text:
        if letter.lower() in alphabet:
            index = 0
            for x in alphabet:
                if letter.lower() == x.lower():
                    break
                index += 1
            sum = index + rotation
            while sum > 25:
                sum -= 26
            if letter in alphabet:
                letter = alphabet[sum]
            else:
                letter = alphabetUppercase[sum]
        newsentence = newsentence + letter
    return "Caesarcode: {sentence}".format(sentence= newsentence)
"""****************OPDRACHT 12------- FizzBuzz*************"""
def fizzBuzz():
    for i in range(1, 101):
        if ((i % 3) == 0) and ((i % 5) == 0):
            print("FizzBuzz")
        elif (i % 3) == 0:
            print("Fizz")
        elif (i % 5) == 0:
            print("Buzz")
        else:
            print(i)

""" ############### Niels Bijl - 1754339 ##################"""