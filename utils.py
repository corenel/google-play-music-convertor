import argparse
import json
import glob
from argparse import Namespace
from typing import Dict
from typing import List


def parse_arg():
    # type: () -> Namespace
    """Parse arguments."""

    # define arguments
    parser = argparse.ArgumentParser(description='demo project')
    parser.add_argument('filepath', type=str, help='path for input file')
    parser.add_argument(
        '--output',
        '-o',
        type=str,
        default=None,
        help='path for output result')

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
    # type: (str) -> List[Dict[str, str]]
    """Parse raw music list from Google Play Music.

    :filepath: path for json file
    :returns: parsed dict of music list

    """
    with open(filepath, 'r') as f:
        music_list = json.load(f)
        return music_list


def find_music_file(filename, dirname):
    """Find file in given directory

    :filename: name of file to be found
    :dirname: directory to find file
    :returns: absolute path of file

    """
    pass
