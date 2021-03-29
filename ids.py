#Pohmx development 2021
#Free of use! Python 3.9x
#You will need -pip install pyperclip- in order to use it.

import os, re, pyperclip

beatmaps = "\n".join(os.listdir('G:/osu!/Songs'))
pattern = '^[0-9]*\s'
processed = [n.strip(' ') for n in re.findall(pattern, beatmaps, re.MULTILINE)]
clipboard = ",".join(processed)
pyperclip.copy(clipboard)
#print
print('copied')