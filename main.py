from utils import (parse_arg, parse_music_list, find_music, convert_music,
                   check_dir, get_outpath, fix_unicode_kana)
import os


def main():
    """Main sciprt."""
    args = parse_arg()
    check_dir(args.output)
    music_list = parse_music_list(args.filepath)
    for idx, music in enumerate(music_list):
        filename = fix_unicode_kana(music['filename'])
        print('--- processing [{}/{}] {} ---'.format(
            idx + 1, len(music_list), filename))
        if os.path.exists(get_outpath(filename, args.dir)):
            print('pass')
            continue
        # find music file
        filepath = fix_unicode_kana(find_music(filename, args.dir))
        # convert music file
        # if check_error(music['error']):
        convert_music(filepath, args.output, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
