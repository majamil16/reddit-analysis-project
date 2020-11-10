import json 
import argparse
#from datetime import datetime, timezone
import os
from hw5.parse_json import load_valid_json, has_title, std_datetime



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Input filepath to be cleaned.", required=True)
    parser.add_argument("-o", help="Name for your output file.")
    parser.add_argument('-v', help="Verbosity; to print all the input and output times")

    args = parser.parse_args()
    
    valid_json_dicts = load_valid_json(args.i) # read in the json file, get all the valid lines
    json_with_correct_titles  = has_title(valid_json_dicts)
    corrected_datetimes = std_datetime(json_with_correct_titles, args.v)
    

    if args.o is not None: # if  they input an output name
        out_file = open(args.o, "w") 
        for post in corrected_datetimes:
            #json.dumps(corrected_datetimes, out_file)
            json.dump(post, out_file)
            out_file.write('\n')

        out_file.close()
    
    

if __name__ == "__main__":
    main()
