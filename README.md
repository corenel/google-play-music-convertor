# A converting script for Google Play Music
Since Google Play Music doesn't support Hi-Res, this script is useful to:

1. Read ‘Unable to load these files’ list in your Google Play Music Settings.
2. Convert Hi-Res music files into ALAC format with CD quality.
3. Then you can try again to upload your files.

## Usage
1. open your [Google Play Music Setting Page](https://play.google.com/music/listen?u=0#/accountsettings) in Chrome.
2. run 'save_list.js' in Chrome Develop Tool:
  - copy and paste code into console and press `Enter`;
  - or save code in to snippets and run.
3. save `music_list.json` in local disk.
4. run `python3 main.py [-o output] [-d dir] [--dry-run] [filepath]`:

```shell
usage: main.py [-h] [--output OUTPUT] [--dir DIR] [--dry-run] filepath

demo project

positional arguments:
  filepath              path for input file

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        path for output result
  --dir DIR, -d DIR     path for music folder
  --dry-run             dry run mode
```
