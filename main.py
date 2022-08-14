import audio_metadata
import glob
import os

supported_formats = ['mp3','wav','flac','ogg']
files = []

artists = []
albums = []
tracknumbers = []
titles = []
formats = []

# Welcome message
print('\033[H\033[J\001\033[0;92m\002Welcome to this music file sorter.\nAll the music in your specified folder\nwill be processed and sorted.\n\001\033[0m\002')


# Get valid input directory
while 1:
  inputdirectory = input('Enter input folder directory: ')
  if os.path.isdir(inputdirectory):
    print('\nScanning...\nIt may take a long time.')
    break
  else:
    print('\nSorry, that is not a valid directory.\nYou could use "music" as your input directory.\n')

# Directories list contains directories of all files and subfolders within the specified folder.
directories = glob.glob('./' + inputdirectory.split('/')[-1] + '/**', recursive = True)

# Append only music files.
for directory in directories:
  # Encode each directory to avoid bugs for os.isfile()
  directories[directories.index(directory)] = directory.encode()
  # Append all suitable file paths
  if os.path.isfile(directory) and directory.split(".")[-1] in supported_formats:
    files.append(directory)
    formats.append(directory.split(".")[-1])

if not len(files):
  input('\001\033[0;31m\002\nNo songs are detected in the "' + inputdirectory + '" folder.\001\033[0m\002')
  raise RuntimeError
# Show songs detected
input('\033[H\033[J\001\033[0;92m\002OK. ' + str(len(files)) + ' songs are detected in the "' + inputdirectory + '" folder.\nPress enter to process them. ⌲ \001\033[0m\002')

# Part 1: Get artists, albums, track numbers, titles and formats.
for file in files:
  print('\nGetting "' + file.split("/")[-1] + '"...')
  try:
    metadata = audio_metadata.load(file)
    try:
      artist = metadata['tags']['artist'][0]
      print('Artist is ' + artist)
      artists.append(artist)
    except:
      artist = input('Artist of "' + file.split("/")[-1] + '" not found.\nTell me the artist: ')
    try:
      album = metadata['tags']['album'][0]
      print('Album is ' + album)
      albums.append(album)
    except:
      album = input('Album of "' + file.split("/")[-1] + '" not found.\nTell me the album: ')
    try:
      tracknumber = metadata['tags']['tracknumber'][0]
      if int(tracknumber) < 10:
        tracknumber = '0' + tracknumber
      print('Track number is ' + tracknumber)
      tracknumbers.append(tracknumber)
    except:
      title = input('Track number of "' + file.split("/")[-1]  + '" not found.\nTell me the track number: ')
    try:
      title = metadata['tags']['title'][0]
      print('Title is ' + title)
      titles.append(title)
    except:
      title = input('Title of "' + file.split("/")[-1]  + '" not found.\nTell me the title: ')
  except:
    input('\n\n\033[H\033[J\001\033[0;31m\002Sorry, an error occurred getting the music metadata.\n')
    raise RuntimeError

# Part 2: Output and sort files based on metadata
print('\n\n\n\033[H\033[J\001\033[0;92m\002All the metadata for the music is ready.\n\001\033[0m\002')
# Get valid output directory
while 1:
  outputdirectory = input('Enter output folder directory: ')
  if os.path.isdir(outputdirectory):
    if outputdirectory[-1] == '/':
      outputdirectory = outputdirectory[:-1]
    break
  else:
    print('\nSorry, that is not a valid directory.\nYou could use "music" as your output directory.\n')
for file in files:
  artist = artists[files.index(file)]
  album = albums[files.index(file)]
  tracknumber = tracknumbers[files.index(file)]
  title = titles[files.index(file)]
  format = formats[files.index(file)]
  os.renames(file, f'{outputdirectory}/{artist}/{album}/{tracknumber} - {title}.{format}')
print('\033[H\033[J\001\033[0;92m\002Success!\nAll the music is in "' + outputdirectory + '", all sorted.\n\001\033[0m\002')
