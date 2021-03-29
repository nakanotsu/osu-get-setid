# osu-get-setid

This python script will allow you to get all the beatmap id's in your osu folder.
Simply specify the path to it and the program will copy all found id's to the clipboard in the form of '4561,4,698,..'
This is useful to paste it in the ignored beatmapset ids section of https://osusearch.com/account  
You will need -pip install pyperclip- in order to use it.

# Script Documentation

beatmaps = creates a string from all the directories found in the folder to be processed with regex.  
pattern = specifies regex to find numbers until first space; '1 Kenji Ninuma - DISCO★PRINCE' will return '1 ' (space included).  
processed = removes all spaces of the form ' ' in the regex find. the regex find all function has a 'pattern to match', 'string of beatmap directories',
'flag to indicate that they are separated with a \n line break character'. if not provided, the regex will fail to match more than 1.  
clipboard = creates a new string of the filtered results in the form of '1,1110,556,87..' and finally it copies it to the clipboard.  

# Issues

There may be duplicate beatmaps in your folder, this will reflect when copying the id's and updating it in osusearch, which will have less id's than copied