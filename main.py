from utils import parse_arg, parse_music_list


def main():
    """Main sciprt."""
    args = parse_arg()
    music_list = parse_music_list(args.filepath)
    print(len(music_list))


if __name__ == "__main__":
    collect_types.init_types_collection()
    collect_types.resume()
    main()
    collect_types.pause()
    collect_types.dump_stats('type_info.json')
