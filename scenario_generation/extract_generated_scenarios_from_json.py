#! /usr/bin/env python3

import sys
import os
import argparse
import json
import re

def main():
    arg_parser = argparse.ArgumentParser(description = 'Extract generated scenario from a JSON file.')
    arg_parser.add_argument("json_file", type=str,
                            help="input .json file to be converted")
    arg_parser.add_argument("-d", "--output-dir", type=str, required=False, default="./",
                            help="Output directory (default: ./)")
    arg_parser.add_argument("-p", "--fix-local-path", type=str, required=False, default="",
                            help="Fix relative asset paths specified by localPath(), making it point to the specified directory (default: disabled)")
    arg_parser.add_argument("-m", "--add-map-path", type=str, required=False, default="",
                            help="Add map path if not specified in the code, making it point to the specified directory (default: disabled)")
    arg_parser.add_argument("-i", "--initial-index", type=int, default=1,
                            help="Index of the first scenario to use in the file names (default: 1)")

    args = arg_parser.parse_args()
    with open(args.json_file, "r") as in_fs:
        scenario_list = json.load(in_fs)

    for i, scenario_str in enumerate(scenario_list):
        scenario_id = i + args.initial_index
        out_filename = os.path.join(args.output_dir, ("scenario_%s.scenic" % (scenario_id)))

        if args.fix_local_path != "":
            scenic_dir = args.fix_local_path + "/" if (args.fix_local_path[-1] != "/") else args.fix_local_path
            scenario_str = re.sub("localPath\('(../)+", ("localPath('%s" % scenic_dir), scenario_str)
            scenario_str = re.sub("localPath\(\"(../)+", ("localPath(\"%s" % scenic_dir), scenario_str)

        if args.add_map_path != "":
            map_dir = args.add_map_path + "/" if (args.add_map_path[-1] != "/") else args.add_map_path
            if not re.search("param(?:\s+)map(?:\s*)=", scenario_str): # map path not specified in the code
                carla_map_match = re.search("param(?:\s+)carla_map(?:\s*)=(?:\s*)['\"](\S+)['\"]", scenario_str) # CARLA map name
                if carla_map_match:
                    carla_map = carla_map_match.group(1)
                    map_str = "param map = localPath('%s')" % (map_dir + carla_map + ".xodr")
                    scenario_str = re.sub('"""\n', ('"""\n\n%s\n' % map_str), scenario_str, count=1) # add after the docstring

        with open(out_filename, "w") as out_fs:
            print('"""', file=out_fs)
            print(scenario_str, file=out_fs)

if __name__ == "__main__":
    main()


