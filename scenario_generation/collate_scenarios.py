#! /usr/bin/env python3

import sys
import os
import argparse
import json

def main():
    arg_parser = argparse.ArgumentParser(description = 'Join Scenic scenarios in json format')
    arg_parser.add_argument("files", type=str, nargs='+',
                            help=".json files to be joined")
    arg_parser.add_argument("-d", "--output-file", type=str, required=True,
                            help="Output .json file")

    args = arg_parser.parse_args()
    acc = []
    for in_file_name in args.files:
        with open(in_file_name) as in_fs:
            scenario_dict = json.load(in_fs)
        base_file_name = os.path.splitext(os.path.basename(in_file_name))[0]
        scenario_dict["name"] = base_file_name
        acc.append(scenario_dict)

    with open(args.output_file, "w") as out_fs:
        json.dump(acc, out_fs, indent=2)

if __name__ == "__main__":
    main()

