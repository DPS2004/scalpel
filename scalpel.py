from os import system, name, path
import os
import glob
import sys
import re
import msvcrt

consoleinput = "false"
from PIL import Image
#IF THINGS ARE NOT WORKING, UNCOMMENT THE FOLLOWING LINE.
#consoleinput = "true"
def filelen(file):
    with open(file) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def findline(filename, linenum):
    line = 0
    with open(filename, "r") as file:
        for _ in range(linenum):
            line = file.readline()
    return line


def smparse(file):
    print("finding bpms...")
    with open(file) as openfile:
        for l in openfile:
            for part in l.split():
                if "#BPMS:" in part:
                    with open("smbpm.temp", "a") as outputfile:
                        outputfile.write(re.sub("[,=]", "\n", part[6:-1]))
    print("finding audio file...")
    with open(file) as openfile:
        for l in openfile:
            for part in l.split():
                if "#MUSIC:" in part:
                    with open("smaud.temp", "a") as outputfile:
                        outputfile.write(part[7:-1])
    print("finding offset...")
    with open(file) as openfile:
        for l in openfile:
            for part in l.split():
                if "#OFFSET:" in part:
                    with open("smoff.temp", "a") as outputfile:
                        outputfile.write(str(abs(float(part[8:-1]) * 1000)))
    print("done parsing", file)


def cleanup(full):
    for item in os.listdir('output/'):
        if item.endswith(".gif"):
            os.remove(os.path.join('output/', item))
    for item in os.listdir('.'):
        if item.endswith(".temp"):
            os.remove(os.path.join('.', item))
    if full == "y":
        for item in os.listdir('.'):
            if item.endswith(".txt"):
                os.remove(os.path.join('.', item))
        for item in os.listdir('output/'):
            if item.endswith(".txt"):
                os.remove(os.path.join('output/', item))
        for item in os.listdir('output/'):
            if item.endswith(".png"):
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
if input("remove files from last use? (y or n)") == "y":
    cleanup("y")
print("Welcome to Scalpel. (Super Cool Awesome Level Program: Extra Lines!)")
while 0 == 0:
    print("1. Effect repeater")
    print("2. Grade calculator")
    print("3. GIF exporter")
    print("4. Clone hero BPM converter")
    print("5. Stepmania/itg bpm converter")
    print("6. Easy Custom Characters")
    print("7. Credits")
    print("8. Exit")
    selection = input("Please enter a number: ")
    if selection == "1":
        clear()
        bpmeasure = int(input("What is your crotchet length? (default is 8)"))
        firstblock = input('What is the first block? (copy and paste from "y":, to },)')
        secondblock = input('What is the second block? (same format as first)')
        blockdistance = float(input("What is the distance between these events in beats?"))
        effectdistance = float(input("What is the distance between the first first block and the second first block?"))
        startmeasure = int(input("What measure should this effect start?"))
        startbeat = float(input("What beat should this effect start?"))
        repeatnumber = int(input("How many times should this effect repeat?"))
        if path.exists("output/output.txt"):
            os.remove("output/output.txt")
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
        waitforkey()
        clear()
    if selection == "3":
        gifname = input("Filename of gif?")
        print("Processing gif...")
        giffps = giflook(gifname)
        print("Done processing.")
        cleanup("n")
        bpm = int(input("bpm of the song?"))
        framecount = int(input("How many frames?"))
        loopcount = int(input("How many times do you want this gif to play?"))
        bpmeasure = int(input("What is your chrotchet length? (default is 8)"))
        startmeasure = int(input("What measure should this GIF start at?"))
        startbeat = int(input("What beat? "))
        contentmode = input("how should it be scaled?(ScaleToFill, AspectFit, AspectFill, Center, Tiled)")
        room = int(input("what room?(if unsure, 0)"))
        yval = int(input("editor Y value? (if unsure, 0)"))
        print("Processing...")
        if path.exists("output/output.txt"):
            os.remove("output/output.txt")
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
        clear()
        infile = input("Enter clone hero file: ")
        spacing = int(input("In CH - How long is one beat in position: ")) * 2
        crotchet = int(input("In RD - What is your crotchet length: "))
        space = int(input("How many spaces for indentation? (if unsure, put 2)"))
        if path.exists("output/output.txt"):
            os.remove("output/output.txt")
        outfilewrite = open("output/output.txt", 'w')
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
                    bar = str(int(int(info[space]) / spacing / crotchet) + 1)
                    beat = str(float(int(info[space]) / spacing % crotchet) + 1)
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
        smfile = input("fileame of .sm file?")
        smparse(smfile)
        newfile = input("make a new .rdlevel file?(y or n)")
        if newfile == "n":
            bpmeasure = int(input("What is your crotchet length? (default is 8)"))
        else:
            bpmeasure = 8
        if newfile == "y":
            if path.exists("output/output.rdlevel"):
                os.remove("output/output.rdlevel")
            outname = "output/output.rdlevel"
            with open(outname, "a") as outputfile:
                outputfile.write('{' + '\n' + '	"settings":' + '\n' + '	{' + '\n' + '		"version": 26, ' + '\n' + '		"artist": "", ' + '\n' + '		"song": "", ' + '\n' + '		"author": "", ' + '\n' + '		"previewImage": "", ' + '\n' + '		"previewSong": "", ' + '\n' + '		"previewSongStartTime": 0, ' + '\n' + '		"previewSongDuration": 10, ' + '\n' + '		"description": "", ' + '\n' + '		"tags": "", ' + '\n' + '		"separate2PLevelFilename": "", ' + '\n' + '		"levelMode": "", ' + '\n' + '		"firstBeatBehavior": "RunNormally", ' + '\n' + '		"multiplayerAppearance": "HorizontalStrips", ' + '\n' + '		"rankMaxMistakes": [20, 15, 10, 5], ' + '\n' + '		"rankDescription":' + '\n' + '		[' + '\n' + '			"Better call 911, now!",' + '\n' + '			"Ugh, you can do better",' + '\n' + '			"Not bad I guess...",' + '\n' + '			"We make a good team!",' + '\n' + '			"You are really good!",' + '\n' + '			"Wow! Thats awesome!!"' + '\n' + '		]' + '\n' + '	},' + '\n' + '	"rows":' + '\n' + '	[' + '\n' + '	],' + '\n' + '	"events":' + '\n' + '	[' + '\n')
        else:
            if path.exists("output/output.txt"):
                os.remove("output/output.txt")
            outname = "output/output.txt"
        with open(outname, "a") as outputfile:
            outputfile.write('		{ "bar": 1, "beat": 1, "y": 0, "type": "PlaySong", "filename": "' + findline("smaud.temp", 1) + '", "volume": 100, "offset": ' + findline("smoff.temp", 1) + ', "bpm": ' + findline("smbpm.temp", 2)[:-1] + ' }, ' + '\n')
        bpmcount = 2
        while bpmcount < filelen("smbpm.temp"):
            beatone = (float(findline("smbpm.temp", bpmcount + 1)[:-1]) % bpmeasure) + 1
            barone = float(findline("smbpm.temp", bpmcount + 1)[:-1]) / bpmeasure
            newbpm = float(findline("smbpm.temp", bpmcount + 2)[:-1])
            with open(outname, "a") as outputfile:
                outputfile.write('		{ "bar": ' + str(round(barone)) + ', "beat": ' + str(beatone) + ', "y": 0, "type": "SetBeatsPerMinute", "beatsPerMinute": ' + str(abs(newbpm)) + ' }, ' + '\n')
            bpmcount = bpmcount + 2
        if newfile == "y":
            with open(outname, "a") as outputfile:
                outputfile.write('	]' + '\n' + '}' + '\n')
        cleanup("n")
        print("done! check " + outname)
        waitforkey()

    if selection == "6":
        clear()
        print("Would you like to learn how to use the custom character template? (y/n)")
        if input("") == "y":
            clear()
            print("1. Replace the black in template1.png and template2.png with the color of your background.")
            print("2. On template1.png paste in your the first frame of sprite in a new layer. Move it to the desired position.")
            print("3. On template2.png paste in your the second frame of sprite in a new layer. Make sure the two sprites are in the same position.")
            print("4. Save the pngs as charactername1.png and charactername2.png respectively. Replace charactername with the name of your character.")
            print("5. In your level add a Boy row on where you want the character to be. Make sure he is the only character in the room.")
            print("Press any key when you are finished with this.")
            waitforkey()


        bpmeasure = int(input("What is your crotchet length? (default is 8)"))
        startmeasure = int(input("At what measure should this character appear?"))
        startbeat = float(input("At what beat should this character appear?"))
        repeatnumber = int(input("For how many beats should this character stay?"))
        charname = input("What is the name of the character")
        yval = int(input("editor Y value? (if unsure, 0)"))
        room = int(input("What room is the Boy in?"))
        clear()
        print("processing...")
        i = 1
        if path.exists("output/output.txt"):
            os.remove("output/output.txt")
        barone = startmeasure
        beatone = startbeat
        while i < repeatnumber + 1:
            if beatone >= bpmeasure + 1:
                beatone = beatone - bpmeasure
                barone = barone + 1
            with open("output/output.txt", "a") as outputfile:
                outputfile.write('		{ "bar": ' + str(int(barone)) + ', "beat": ' + str(beatone) + ', "y": ' + str(yval) + ', "type": "SetForeground", "rooms": [' + str(room) + '], "contentMode": "ScaleToFill", "color": "ffffffff", "image": "' + charname + '1.png", "scrollX": 0, "scrollY": 0 }, ' + '\n')
                outputfile.write('		{ "bar": ' + str(int(barone)) + ', "beat": ' + str(beatone + 0.25) + ', "y": ' + str(yval) + ', "type": "SetForeground", "rooms": [' + str(room) + '], "contentMode": "ScaleToFill", "color": "ffffffff", "image": "' + charname + '2.png", "scrollX": 0, "scrollY": 0 }, ' + '\n')
            beatone = beatone + 1
            i = i + 1
        print("Done! Open output.txt and copy the contents to the .rdlevel file")
        waitforkey()
        clear()
    if selection == "7":
        print("Effect repeater, Gif importer, Stepmania/itg bpm converter, grade calculator and easy custom characters were made with <3 by DPS2004")
        print("Clone hero bpm converter made by Not El Donte and Klyzx")
        waitforkey()
        clear()
    if selection == "8":
        break
