# Dynamix Sprites

This is from the assets Dynamix downloads using "Download all data".

## Downloading

Download a single folder or the whole thing(source code) in the latest [![release](https://img.shields.io/github/v/release/NutchapolSal/dynamixSprites)](https://github.com/NutchapolSal/dynamixSprites/releases)

## The Folders

Folders are named according to the internal asset containers. Some song titles may be romanized or translated so search throughly before making an issue.

Sprites files names are kept as is. Some files have the same name internally so a random number is suffixed to prevent name collisions.

### Avator & Char

Contains character sprites.

`avator` are for older ones while `char` are newer ones. Look in both folders before making an issue complaining that a character doesn't exist.

### Avatorlist

Contains preview images for characters & parts that displays in the character customization panels & the store.

### Background & Bg

Contains background parts (Bottom row in parts panel).

Same deal with `avator` & `char`

### Cover

Contains background images for the songs.

For the store bought songs, The devs only prefixed the names of pack 1 - pack 10 sprite files, and just pack 3 - pack 6 & pack 10 asset containers. Essentially it was organized up to pack 10, then the rest is mixed in with the other files. But I've already organized them into pack 1 - pack 26 so you don't have to.

|pack no.|store name|
|---|---|
|1|Evas|
|2|Chiptune|
|3|Four Horsemen|
|4|Fantasy|
|5|Two Square: Horoscope|
|6|Two Square: Rising|
|7|Piano|
|8|ArcStar Collection #1|
|9|ArcStar Collection #2|
|10|VelecTi Collection|
|11|Z.H.D.|
|12|Teardrops|
|13|Kplecraft Collection|
|14|Vocal|
|15|Rabi-Ribi|
|16|Lovely|
|17|Ace|
|18|ARCAEA|
|19|Pianomatic|
|20|Two Square: Old Year #1|
|21|Stellights Collection|
|22|Electroclassica|
|23|BilliumMoto|
|24|Intruders|
|25|Crossing Delta|
|26|RAVON Collab Pack #1|

### Front

Contains "frontground" parts (Middle row in parts panel).

### Parts & Title

Contains title parts (Top row in parts panel). `parts` only contains sprites for the wave test titles while `title` contains the rest of them.

### SongPackageList

Contains text sprites used in store's package section.

### SongRef

Contains song title & artist text sprites, `sm`all blurry version of the background images (the ones you see while quickly scrolling through the song list) & `thumb`nails for songs that appear in the store.

## Want to do it yourself??

hints:

- No android device? just use emulator.
- it uses Unity
- APK just has the gameplay, ui, etc. The rest is downloaded separately (including non-event songs).
- `/sdcard/Android/data/com.c4cat.dynamix/files/UnityCache/Shared`
- use [AssetStudio](https://github.com/Perfare/AssetStudio)

### the better way

- run wireshark with nox, look for "dynamix" dns query
- look for the file with version number
- get the "Android" asset bundle manifest
- get the list of all bundles inside that with asset studio
- ??
- profit