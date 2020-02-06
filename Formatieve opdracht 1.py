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
