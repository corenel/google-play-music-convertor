from utils import (parse_arg, parse_music_list, find_music, convert_music,
                   check_dir)


def main():
    """Main sciprt."""
    args = parse_arg()
    music_list = parse_music_list(args.filepath)
    for idx, music in enumerate(music_list):
        filename = music['filename']
        print('--- processing [{}/{}] {} ---'.format(
            idx + 1, len(music_list), filename))
        # find music file
        filepath = find_music(filename, args.dir)
        print('[original path]: {}'.format(filepath))
        # convert music file
        check_dir(args.output)
        convert_music(filepath, args.output, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
