# Music files sorter
#### Written in python 3 by Mark Z

## 1. What it does

Basically it sorts your music files into a clean structure:

> Music
>> Joe
>>> Album 1
>>>> 01 - Party.mp3
>>>> 
>>>> 02 - Balloons.mp3
>>>> 
>>> Album 2
>>>> 01 - Kittens.m4a
>>> 
>> Joan
>>> Album 1
>>>> 01 - Hugs.flac

Some apps require music to be stored in this organized way... And this program does it for you. 

## 2. Building
The python modules "tinytag" and "glob" are required to be installed. Put this in command line to install them.

    pip3 install tinytag glob2
To get the program, first get the ZIP from github, unzip it, and then delete the zip file.

    curl -o main.zip https://github.com/Cheerstoast/Music-files-sorter/archive/refs/heads/main.zip && unzip main.zip && rm main.zip

## 3. Usage
**Your music files would need to be in the same disk as the "main.py" file.**
    
To run the program, just run

    python3 Music-files-sorter-main/main.py

The program was made to be fool-proof, and the user must put valid input/output directories for the program to analyze.

If you do not know the directory (folder) path, you could put the files you want to sort in the "music" folder, which is in the "Music-files-sorter-main" folder.

The input and output directories could be the same, if you just wanted to tidy up the music folder.

Supported formats include: .mp3 .wav .flac .ogg and .m4a

If some parts of the metadata are missing, it would just ask you for them.

If any errors occur, the program would terminate with an error message.

### Enjoy >!<
