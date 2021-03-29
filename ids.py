#Pohmx development 2021
#Free of use! Python 3.9x
#You will need -pip install pyperclip- in order to use it.

import os, re, pyperclip

beatmaps = "\n".join(os.listdir('G:/osu!/Songs'))
pattern = '^[0-9]*\s'
processed = [n.strip(' ') for n in re.findall(pattern, beatmaps, re.MULTILINE)]
clipboard = ",".join(processed)
pyperclip.copy(clipboard)

#beatmaps = creates a string from all the directories found in the folder to be processed with regex.
#pattern = specifies regex to find numbers until first space; '1 Kenji Ninuma - DISCO★PRINCE' will return '1 ' (space included).
#processed = removes all spaces of the form ' ' in the regex find. the regex find all function has a 'pattern to match', 'string of beatmap directories', 
#'flag to indicate that they are separated with a \n line break character'. if not provided, the regex will fail to match more than 1.
#clipboard = creates a new string of the filtered results in the form of '1,1110,556,87..' and finally it copies it to the clipboard.
