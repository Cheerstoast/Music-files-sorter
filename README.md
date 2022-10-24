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

But before you build the program, **navigate to the parent/upper folder of your music files.**

Afer that, build the program. First get the ZIP from github, unzip it, and then delete the zip file. 


    curl -s -LO https://github.com/Cheerstoast/Music-files-sorter/archive/refs/heads/main.zip -o main.zip && unzip main.zip && rm main.zip

## 3. Usage

    
To run the program, just run

    python3 Music-files-sorter-main/main.py

The program is totally fool-proof. It took a long time to make it so.

The user must put valid input and output directories for the program to analyze. The input and output directories could be the same, if you just wanted to tidy up the music folder.

Supported formats include: .mp3 .wav .flac .ogg and .m4a

If some parts of the metadata are missing, it would just ask you for them.

If any errors occur, the program would terminate with an error message.

### Enjoy >!<
