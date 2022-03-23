# Subtitle Renamer
rename subtitle file to match video file name

## How To Use
⚠️subtitle and video files should put at the same folder⚠️

⚠️only match `SXXEXX` (eg. `S10E03`) currently
```
python subtitle_renamer.py -filPath path/to/your/files
```

## Arguments
 -h, --help : show this help message and exit

  -filePath, -fP : file path to subtitle files and video files(they should locate at the same path)

  -language, -L  : subtitle language (default is chi for chinese) is defined by the [ISO-639-1 (2-letter)](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) or [ISO-639-2/B (3-letter)](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes) standard

## Subtitle Format Supported List
`ass` and `ssa`

`srt`

`vtt`

## Enjoy the Script !