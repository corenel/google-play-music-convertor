import argparse
import subprocess
import json
import os
import glob


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

    print("--- end  ---")
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
    filepath = glob.glob(os.path.join("**", filename), recursive=True)
    if filename:
        return os.path.abspath(os.path.join(dirname, filepath[0]))
    else:
        return ''


def check_dir(dirpath):
    """Check directory and create one if it not exists.

    :dirpath: path for directory to check

    """
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)


def convert_music(filepath, outdir, dry_run=False):
    """Convert music into ALAC format with CD quality.

    :filepath: path for music file to be converted
    :outpath: path for output directory

    """
    if os.path.exists(filepath):
        filename = os.path.basename(filepath)
        outpath = os.path.join(outdir, filename)
        # check if already converted
        if os.path.exists(outpath):
            print('pass')
            return
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
            if output or errors:
                print('[output]:\n{}'.format(
                    output.decode('utf-8') + errors.decode('utf-8')))

        else:
            print('[command]:\n{}'.format(command))
