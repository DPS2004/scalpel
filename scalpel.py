from os import system, name
import msvcrt
consoleinput = "false"

#IF THINGS ARE NOT WORKING, UNCOMMENT THE FOLLOWING LINE.
#consoleinput = "true"


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


print("Welcome to Scalpel. ")
while 0 == 0:
    print("1. Effect repeater")
    print("2. Grade calculator")
    print("3. Credits")
    print("4. Exit")
    selection = input("Please enter a number: ")
    if selection == "1":
        clear()
        bpmeasure = int(input("How many beats per measure? (default is 8)"))
        firstblock = input('What is the first block? (copy and paste from "y":, to },)')
        secondblock = input('What is the second block? (same format as first)')
        blockdistance = int(input("What is the distance between these events in beats?"))
        effectdistance = int(input("What is the distance between the first first block and the second first block?"))
        startmeasure = int(input("What measure should this effect start?"))
        startbeat = int(input("What beat should this effect start?"))
        repeatnumber = int(input("How many times should this effect repeat?"))
        print("Calculating...")
        i = 1
        barone = startmeasure
        beatone = startbeat
        while i < repeatnumber + 1:
            if beatone >= bpmeasure + 1:
                beatone = beatone - bpmeasure
                barone = barone + 1

            effectone = '		{ "bar": ' + str(barone) + ', "beat": ' + str(beatone) + ', ' + firstblock + '\n'
            bartwo = barone
            beattwo = beatone + blockdistance
            if beattwo >= bpmeasure + 1:
                beattwo = beattwo - bpmeasure
                bartwo = bartwo + 1
            effecttwo = '		{ "bar": ' + str(bartwo) + ', "beat": ' + str(beattwo) + ', ' + secondblock + '\n'
            with open("output.txt", "a") as outputfile:
                outputfile.write(effectone)
                outputfile.write(effecttwo)
            beatone = beatone + effectdistance
            i = i + 1
        print("done! check output.txt")
        waitforkey()
        clear()

    if selection == "2":
        clear()
        hitcount = int(input("how many times does the player have to hit a button? (do not count cpu rows)"))
        print("A rank: " + str(round(hitcount*0.1)) + " misses.")
        print("B rank: " + str(round(hitcount*0.2)) + " misses")
        print("C rank: " + str(round(hitcount*0.3)) + " misses")
        print("D rank: " + str(round(hitcount*0.4)) + " misses")
        print("E rank: " + str(round(hitcount*0.5)) + " misses")
        print("F rank: " + str(round(hitcount*0.6)) + " misses")
        waitforkey()
        clear()
    if selection == "3":
        clear()
        print("Made with <3 by DPS2004#5143")
        waitforkey()
        clear()
    if selection == "4":
        break
