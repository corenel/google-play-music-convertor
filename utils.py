import argparse
import subprocess
import json
import os
import glob
import unicodedata


def parse_arg():
    """Parse arguments."""

    # define arguments
    parser = argparse.ArgumentParser(description='demo project')
    parser.add_argument('filepath', type=str, help='path for input file')
    parser.add_argument(
        '--output',
        '-o',
        type=str,
        default='/Volumes/Backup/Music/Converted/',
        help='path for output result')
    parser.add_argument(
        '--dir',
        '-d',
        type=str,
        default='/Volumes/Backup/iTunes/iTunes Media/',
        help='path for music folder')
    parser.add_argument('--dry-run', action='store_true', help='dry run mode')

    # parse arguments
    args = parser.parse_args()

    # print arguments
    args_dict = vars(args)
    print("--- args ---")
    for k, v in args_dict.items():
        print("[{}]: {}".format(str(k), str(v)))

    return args


def parse_music_list(filepath):
    """Parse raw music list from Google Play Music.

    :filepath: path for json file
    :returns: parsed dict of music list

    """
    with open(filepath, 'r') as f:
        music_list = json.load(f)
        return music_list


def find_music(filename, dirname):
    """Find file in given directory.

    :filename: name of file to be found
    :dirname: directory to find file
    :returns: absolute path of file

    """
    os.chdir(dirname)
    filename = fix_unicode_kana(filename)
    filepath = glob.glob(os.path.join('**', filename), recursive=True)
    if filepath:
        return os.path.abspath(os.path.join(dirname, filepath[0]))
    else:
        return ''


def check_dir(dirpath):
    """Check directory and create one if it not exists.

    :dirpath: path for directory to check

    """
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)


def check_error(error):
    """Check error of Google Play Music.

    :error: error message
    :returns: if the error is Unsupported ALAC file.

    """
    return error == 'Unsupported ALAC file'


def get_outpath(filename, outdir):
    """Get output filepath.

    :filename: name of music file
    :outdir: path of output directory
    :returns: path of converted music file

    """
    outname = '{}.mp3'.format(os.path.splitext(filename)[0])
    outpath = os.path.join(outdir, outname)
    return outpath


def fix_unicode_kana(s):
    """Fix katakana-hiragana voiced sound mark '\u3099' and '\u309a' in string.

    :filepath: string to be fixed
    :returns: refined string

    """
    if '\u3099' in s or '\u309a' in s:
        return ascii(unicodedata.normalize('NFC', s))
    else:
        return s


def convert_music(filepath, outdir, dry_run=False):
    """Convert music into ALAC format with CD quality.

    :filepath: path for music file to be converted
    :outpath: path for output directory

    """
    if os.path.exists(filepath):
        filename = os.path.basename(filepath)
        outpath = get_outpath(filename, outdir)
        # command line for xld
        command = 'xld -f mp3 --profile mp3_320 -o "{}" "{}"'.format(
            outpath, filepath)
        # dey run or real
        if not dry_run:
            p = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
            output, errors = p.communicate()
            if p.returncode == 0:
                print('saved to {}'.format(outpath))
            else:
                print('[output]:\n{}'.format(
                    output.decode('utf-8') + errors.decode('utf-8')))
                print('[command]:\n{}'.format(command))

        else:
            print('[command]:\n{}'.format(command))
