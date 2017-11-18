from utils import parse_arg, parse_music_list, find_music


def main():
    """Main sciprt."""
    args = parse_arg()
    music_list = parse_music_list(args.filepath)
    for music in music_list:
        music_path = find_music(music['filename'], args.dir)
        print(music_path)
        break


if __name__ == "__main__":
    main()
