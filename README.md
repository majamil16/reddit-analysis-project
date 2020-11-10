# reddit-analysis

scripts
-------

collect.py
----------
Collects 100 newest posts from the list of subreddits entered by the user (in main function). Writes the collected posts to json files in ./data 
Optional --test to run through a subset of subreddits for testing functionality.
usage: python3 collect.py --test 


clean.py
--------
Script to clean JSON files containing "title" or "title_date" (where each json dict. represents a reddit post.)
usage: python3 clean.py -i <input_file> -o <output_file>



check2ifvalid.sh
----------------
this goes through each line of the obtained file and checks if it's a valid JSON format. 


compute_title_lengths.py
-------------------------
computes the average title length of posts from each collection of subreddits collected. (when given a .json file of dicts of posts, one post per line, obtained from collect.py, returns the average of all these title lengths.)
