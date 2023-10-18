#! /usr/bin/env python3

import sys
import os
import argparse
import json
import re

def main():
    arg_parser = argparse.ArgumentParser(description = 'Simplify and fix scenarios in a JSON collection format')
    arg_parser.add_argument("json_in_file", type=str,
                            help="input .json file to be converted")
    arg_parser.add_argument("json_out_file", type=str,
                            help="output .json file to save the scenarios to")
    arg_parser.add_argument("-p", "--remove-local-path", action="store_true",
                            help="Removes the local-path directive (it needs to be re-added in order to execute the scenarios) (default: disabled)")

    args = arg_parser.parse_args()
    with open(args.json_in_file, "r") as in_fs:
        scenario_list = json.load(in_fs)

    rv = []
    for i, scenario in enumerate(scenario_list):
        scenario_str = scenario['body']
        if args.remove_local_path:
            scenario_str = re.sub(r'^[\s\S]*localPath[^\n]*\n', "", scenario_str, flags=re.MULTILINE)
        scenario_str = re.sub(r'^\s*#[^\n]*$', "", scenario_str, flags=re.MULTILINE) # Remove whole-line comments
        scenario_str = re.sub(r'^\s*\n', "", scenario_str, flags=re.MULTILINE) # Remove empty lines
        scenario_str = re.sub(r'^(\s*)model scenic.[\S]*', r'\1model scenic.simulators.carla.model', scenario_str, flags=re.MULTILINE) # Fix incorrect model name
        scenario_str = re.sub(r'vehicle.lincoln.mkz2017', 'vehicle.lincoln.mkz_2017', scenario_str) # Fix broken vehicle name
        scenario['body'] = scenario_str
        rv.append(scenario)

    with open(args.json_out_file, "w") as out_fs:
        json.dump(rv, out_fs, indent=2)

if __name__ == "__main__":
    main()


