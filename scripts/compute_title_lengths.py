import json
import argparse


def count_title_words(input_file):
    total_title_length = 0
    total_num_posts = 0
    with open(input_file) as f:
        for line in f:
            cur_dict = json.loads(line)
            #print(type(cur_dict))
            #print(cur_dict.keys())
            title = cur_dict['data']['title']
            title_length = len(title)
            total_title_length += title_length
            total_num_posts += 1
    
    avg_title_length = total_title_length/total_num_posts
    avg_title_length = round(avg_title_length, 2)
    #print(avg_title_length)
    return avg_title_length


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to the input file of JSON dicts to compute average post title.")
    args = parser.parse_args()
    avg_title_length = count_title_words(args.input_file)
    print(avg_title_length) 

if __name__ == "__main__":
    main()
