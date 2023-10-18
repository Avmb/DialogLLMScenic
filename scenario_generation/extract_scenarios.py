#! /usr/bin/env python3

import sys
import os
import argparse
import json
import tokenize
from io import BytesIO
import ast

def convert_file(in_file_name, output_dir):
    base_file_name = os.path.splitext(os.path.basename(in_file_name))[0]
    out_file_name = os.path.join(output_dir, base_file_name + ".json")
    with open(in_file_name) as in_fs:
        lines = in_fs.readlines()
    text_str = "".join(lines)
    tokens = list(tokenize.tokenize(BytesIO(text_str.encode('utf-8')).readline))
    if tokens[1].type == 3: # docstring token
        docstring_token = tokens[1]
        docstring = ast.literal_eval(docstring_token.string).strip()
        body_lines = lines[docstring_token.end[0]+1:]
    else:
        docstring=None
        body_lines = lines

    out_dict = {"docstring" : docstring,
                "has_docstring" : (docstring is not None),
                "body" : "".join(body_lines).strip()}
    with open(out_file_name, "w") as out_fs:
        json.dump(out_dict, out_fs, indent=2)


def main():
    arg_parser = argparse.ArgumentParser(description = 'Collect Scenic scenarios and encode them as json files')
    arg_parser.add_argument("files", type=str, nargs='+',
                            help=".scenic files to be converted")
    arg_parser.add_argument("-d", "--output-dir", type=str, required=False, default="./",
                            help="Output directory (default: ./)")

    args = arg_parser.parse_args()
    for in_file_name in args.files:
        convert_file(in_file_name, args.output_dir)

if __name__ == "__main__":
    main()

