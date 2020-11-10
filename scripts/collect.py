import json
import requests
from requests import auth
import os
import argparse
PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS = os.path.join(PROJ_DIR,"data", "credentials.json")  # stored login credentials in this file

def get_token():
    """
    Gets the 1000 newest posts from [subreddit_list]
    """

    with open(CREDENTIALS, 'r') as f:
        credentials = json.load(f)

    client_auth = requests.auth.HTTPBasicAuth(credentials['APP_id'], credentials['app_secret']) # authenticate (APP_id, app_secret)


    post_data = {"grant_type": "password", "username": credentials['username'], "password": credentials['password']}


    headers = {"User-Agent": f"RedditPostCollector/0.1 by /u/{credentials['username']}"}
    print(headers)
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)

    token = response.json()['access_token']
    user_agent = headers["User-Agent"]
    return token, user_agent

def get_posts(sub_list):
    """Gets the first 1000 post from all subs in sub_list and stores all in a big list.
    Returns: post_list (list of all the posts.)
    """
    
    token, ua = get_token()
    headers = {"User-Agent": ua, "Authorization": "bearer {}".format(token)}
    print(token)
    post_list=[]
    
    for sub in sub_list:
        #next_pg = None
        cur_num_posts = 0
        cur_sub_post_list = []
        print("Collecting data from {}".format(sub))
        response = requests.get("https://oauth.reddit.com/r/{}/new?limit=100".format(sub), headers=headers) # get the new posts from {} subreddit
        resp_json = response.json()
        posts = resp_json['data']['children'] # this is the posts of the response...
        for post in posts:
            cur_sub_post_list.append(post)
        cur_num_posts += len(cur_sub_post_list)
        print(cur_num_posts)
        post_list.extend(cur_sub_post_list)
    return post_list  # list of all the posts, each element being a dictoinary

def list_to_file(post_list, outfile):
    """Takes the list of posts collected as a list and writes to a json file, one dict (post) per line.
    Input:
    -----
    - post_list : list of posts, in dictionary format, one dictionary = one post. From the Reddit API
    - outfile = the filename for the result to be written to

    Returns:
    -------
    Outputs a file (outfile, likely json) with one dictionary (of post data) per line
    """
    print(PROJ_DIR)
    with open(os.path.join(PROJ_DIR, "data", outfile), 'w') as f: #../data/{}".format(outfile), 'w') as f:
        for post in post_list:
            post_string = json.dumps(post)
            f.write(post_string)
            f.write('\n')
    print("Finished writing {}".format(outfile))
    f.close()



def main():
    """
    Main function which gets all the data..."actual=1' for getting the actual data, set example=1 for getting testing data
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--test",action="store_true", help="To just run the test sample list of subreddits.")
    args = parser.parse_args() 
    if(args.test):
        sample1_subs = ["worldnews"]#, "videos", "todayilearned" ]
        sample2_subs = ["AskReddit"]#, "wallstreetbets","PublicFreakout"]

        sample1_filename = "TEST_sample1_v2.json"
        sample2_filename = "TEST_sample2_v2.json"
                                    #get_posts()

        #sample1_posts = get_posts(sample1_subs)
        #sample2_posts = get_posts(sample2_subs)
        #list_to_file(sample1_posts, sample1_filename)
        #list_to_file(sample2_posts, sample2_filename)

    else:
        print("Running test samples.")
        sample1_subs = ["funny", "AskReddit", "gaming", "aww", "pics", "Music", "science", "worldnews", "videos", "todayilearned" ]
        sample2_subs = ["AskReddit", "memes", "politics", "nfl", "nba", "wallstreetbets", "teenagers", "PublicFreakout", "leagueoflegends", "unpopularopinion"]
    
        sample1_filename = "sample1.json"
        sample2_filename = "sample2.json"
    

    sample1_posts = get_posts(sample1_subs)
    sample2_posts = get_posts(sample2_subs)
    list_to_file(sample1_posts, sample1_filename)
    list_to_file(sample2_posts, sample2_filename)







if __name__=="__main__":
    main()
