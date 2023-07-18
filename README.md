# `scannable.py`
## What is this?
This projects aims to generate simple Spotify codes that are scannable throught the official Spotify app on Android/iOS. Generated scannables will be outputted to the `out/` directory with the Spotify UID as name.

## Usage
```
usage: scannable.py [-h] [-f FORMAT] [-b BACKGROUND] [-t TEXT] [-s SIZE] link

Generate Spotify scannable code through a Python script.

positional arguments:
  link                  Spotify link to generate a scannable image from

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        file format for the scannable output
  -b BACKGROUND, --background BACKGROUND
                        background color for the scannable output
  -t TEXT, --text TEXT  text color for the scannable output
  -s SIZE, --size SIZE  size of the scannable output
```

### Informations
 * For the `--format` parameter, you are supposed to choose a format file from `png`, `jpeg` and `svg`;
 * for the `--background` parameter, you are supposed to insert a HEX code;
 * for the `--text` parameter, you are supposed to insert either `white` or `black`;
 * for the `--size` parameter, you are supposed to insert a value between `256` and `2047`.

## Licensing 
```
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
  ```