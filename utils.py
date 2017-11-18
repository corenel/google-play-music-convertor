import argparse
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
        return None


def convert_music(filepath, outpath):
    """Convert music into ALAC format with CD quality.

    :filepath: path for music file to be converted
    :outpath: path for output directory

    """
    pass
