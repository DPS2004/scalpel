from os import system, name
import msvcrt
consoleinput = "false"
#IF THINGS ARE NOT WORKING, UNCOMMENT THE FOLLOWING LINE.
consoleinput = "true"


def waitforkey():
    if consoleinput == "true":
        input()
    else:
        msvcrt.getch()


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


print("welcome to scalpel. ")
while 0 == 0:
    print("1. effect repeater")
    print("2. grade calculator")
    print("3. credits")
    print("4. exit")
    selection = input("please enter a number: ")
    if selection == "1":
        clear()
        bpmeasure = int(input("how many beats per measure? (default is 8)"))

    if selection == "2":
        clear()
        hitcount = int(input("how many times does the player have to hit a button? (do not count cpu rows)"))
        print("a rank: " + str(round(hitcount*0.1)) + " misses.")
        print("b rank: " + str(round(hitcount*0.2)) + " misses")
        print("c rank: " + str(round(hitcount*0.3)) + " misses")
        print("d rank: " + str(round(hitcount*0.4)) + " misses")
        print("e rank: " + str(round(hitcount*0.5)) + " misses")
        print("f rank: " + str(round(hitcount*0.6)) + " misses")
    if selection == "3":
        clear()
        print("made with <3 by DPS2004#5143")
        waitforkey()
        clear()
    if selection == "4":
        break
