from os import system, name
import os
import glob
import sys
import msvcrt
consoleinput = "false"
from PIL import Image
#IF THINGS ARE NOT WORKING, UNCOMMENT THE FOLLOWING LINE.
#consoleinput = "true"
def gifcleanup():
    for item in os.listdir('output/'):
        if item.endswith(".gif"):
            os.remove(os.path.join('output/', item))
def giflook(inGif):
    frame = Image.open(inGif)

    nframes = 0
    while frame:
        frame.save('%s/output%s.gif' % ("output", nframes), 'GIF')
        nframes += 1
        try:
            frame.seek(nframes)
        except EOFError:
            break;
    files = glob.glob("output/*.gif")

    for imageFile in files:
        filepath, filename = os.path.split(imageFile)
        filterame, exts = os.path.splitext(filename)
        im = Image.open(imageFile)
        im.save('output/' + filterame + '.png', 'PNG')
    frame.seek(0)
    frames = duration = 0
    while True:
        try:
            frames += 1
            duration += frame.info['duration']
            frame.seek(frame.tell() + 1)
        except EOFError:
            return frames / duration * 1000


def countout():
    list = os.listdir("output") # dir is your directory path
    number_files = len(list)
    return number_files


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


print("Welcome to Scalpel. (Super Cool Awesome Level Program: Extra Lines!)")
while 0 == 0:
    print("1. Effect repeater")
    print("2. Grade calculator")
    print("3. GIF exporter")
    print("4. Clone hero BPM converter")
    print("5. Credits")
    print("6. Exit")
    selection = input("Please enter a number: ")
    if selection == "1":
        clear()
        bpmeasure = int(input("How many beats per measure? (default is 8)"))
        firstblock = input('What is the first block? (copy and paste from "y":, to },)')
        secondblock = input('What is the second block? (same format as first)')
        blockdistance = float(input("What is the distance between these events in beats?"))
        effectdistance = float(input("What is the distance between the first first block and the second first block?"))
        startmeasure = int(input("What measure should this effect start?"))
        startbeat = float(input("What beat should this effect start?"))
        repeatnumber = int(input("How many times should this effect repeat?"))
        os.remove("output.txt")
        print("Processing...")
        i = 1
        barone = startmeasure
        beatone = startbeat
        while i < repeatnumber + 1:
            if beatone >= bpmeasure + 1:
                beatone = beatone - bpmeasure
                barone = barone + 1

            effectone = '		{ "bar": ' + str(int(barone)) + ', "beat": ' + str(beatone) + ', ' + firstblock + '\n'
            bartwo = barone
            beattwo = beatone + blockdistance
            if beattwo >= bpmeasure + 1:
                beattwo = beattwo - bpmeasure
                bartwo = bartwo + 1
            effecttwo = '		{ "bar": ' + str(int(bartwo)) + ', "beat": ' + str(beattwo) + ', ' + secondblock + '\n'
            with open("output.txt", "a") as outputfile:
                outputfile.write(effectone)
                outputfile.write(effecttwo)
            beatone = beatone + effectdistance
            i = i + 1
        print("Done! Open output.txt and copy the contents to the .rdlevel file")
        waitforkey()
        clear()

    if selection == "2":
        clear()
        hitcount = int(input("how many times does the player have to hit a button? (do not count cpu rows)"))
        print("A rank: " + str(round(hitcount*0.1)) + " misses.")
        print("B rank: " + str(round(hitcount*0.2)) + " misses")
        print("C rank: " + str(round(hitcount*0.3)) + " misses")
        print("D rank: " + str(round(hitcount*0.4)) + " misses")
        print("F rank: " + str(round(hitcount*0.5)) + " misses")
        waitforkey()
        clear()
    if selection == "3":
        gifname = input("Filename of gif?")
        print("Processing gif...")
        giffps = giflook(gifname)
        print("Done processing.")
        gifcleanup()
        bpm = int(input("bpm of the song?"))
        framecount = int(input("How many frames?"))
        loopcount = int(input("How many times do you want this gif to play?"))
        bpmeasure = int(input("How many beats per measure? (default is 8)"))
        startmeasure = int(input("What measure should this GIF start at?"))
        startbeat = int(input("What beat? "))
        contentmode = input("how should it be scaled?(ScaleToFill, AspectFit, AspectFill, Center, Tiled)")
        room = int(input("what room?(if unsure, 0)"))
        yval = int(input("editor Y value? (if unsure, 0)"))
        print("Processing...")
        i = 1
        bpf = (bpm / 60) / giffps
        barone = startmeasure
        beatone = startbeat
        while i < loopcount + 1:
            itwo = 0

            while itwo < framecount + 1:
                if beatone >= bpmeasure + 1:
                    beatone = beatone - bpmeasure
                    barone = barone + 1

                with open("output/output.txt", "a") as outputfile:
                    outputfile.write('		{ "bar": ' + str(int(barone)) + ', "beat": ' + str(beatone) + ', "y": ' + str(yval) + ', "type": "SetBackgroundColor", "rooms": [' + str(room) + '], "backgroundType": "Image", "contentMode": "' + contentmode + '", "color": "ffffff", "image": "output' + str(itwo) + '.png", "filter": "NearestNeighbor", "scrollX": 0, "scrollY": 0 }, ' + '\n')

                beatone = beatone + bpf
                itwo = itwo + 1
            i = i + 1
        print("Done! Open output.txt in the output folder and copy the contents to the .rdlevel file")
        waitforkey()
        clear()
    if selection == "4":
        infile = input("Enter clone hero file: ")

        spacing = int(input("In CH - How long is one beat in position: ")) * 2
        crochet = int(input("In RD - What is your crochet length: "))
        space = int(input("How many spaces for indentation? (if unsure, put 2)"))
        outfilewrite = open("output.txt", 'w')
        print("Processing...")


        try:
            with open(infile) as file:
                syncfound = False
                for line in file:
                    line = line[:-1]  # Remove \n from end of each line

                    if line != "[SyncTrack]" and syncfound == False:
                        continue
                    elif syncfound == False:  # Skip until the Sync Track section
                        file.readline()
                        file.readline()
                        file.readline()  # Don't need the original bpm or time sig
                        syncfound = True
                        continue
                    if line == "}":  # End at the end of the bpm section
                        break

                    info = line.split(' ')
                    if info[space + 2] == "TS":  # Don't worry about time signature changes
                        continue

                    bpm = str(float(info[space + 3]) / 1000)  # math
                    bar = str(int(int(info[space]) / spacing / crochet) + 1)
                    beat = str(float(int(info[space]) / spacing % crochet) + 1)
                    rdstr = '        { "bar": ' + bar + ', "beat": ' + beat + ', "y": 0, "type": "SetBeatsPerMinute", "beatsPerMinute": ' + bpm + ' },\n'
                    outfilewrite.write(rdstr)
                outfilewrite.close()
            print("Done! Open output.txt and copy the contents to the .rdlevel file")
            waitforkey()
            clear()
        except:
            print("CH file not found")
            waitforkey()
            clear()
    if selection == "5":
        clear()
        print("Effect repeater, Gif importer, and grade calculator were made with <3 by DPS2004")
        print("Clone hero bpm converter made by Not El Donte and Klyzx")
        waitforkey()
        clear()
    if selection == "6":
        break
