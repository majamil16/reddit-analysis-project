import json
from datetime import datetime, timezone

def load_valid_json(f):
    """
    Reads JSON file containing 1 dict per line into an list of all the dicts.
    If the file is malformed, ignore it.
    """
    # dump the json file -> make it into a dictionary
    # read lines into array (each one is a dictionary)
    # go through each dictionary and check...
        # "title" or "title_text" -> if "title_text" rename to title
        # standardize createdAt times

    dicts = [] # store the json dicts (one on each line)
    i=0
    with open(f, "r") as json_file:# open the file in read mode
        for json_dict in json_file: # iterate through each line in the file (is a json dict)
            try:
                d = json.loads(json_dict) # load a string version of the filei
            except Exception as e:
                print("Malformed json", e, i)
                i+=1
                continue
            dicts.append(d) # append the json to the dicts []
            i+=1


    #print(dicts)
    #print(len(dicts))
    return dicts # returns all the lines in the file that are a VALID JSON formatted dictionary.

def has_title(dict_list):
    """Checks whether the list of dicts all have valid titles.
    If an entry doesn't have title or title_text, it's removed
    If it has "title_text", changes it to "title"


    Returns: good_dicts (list of valid title-containg dictionaries :))
    """

    good_dicts = []
    for cur_dict in dict_list:
        if "title_text" in cur_dict.keys(): # if the dictionary has "title_text" change it to title
            cur_dict["title"] = cur_dict.pop("title_text")

        if "title" in cur_dict.keys(): # now, check if "title" is in the keys
            good_dicts.append(cur_dict) # if so, append it to the good_dicts. if it doesnt have a title, it will be removed from the dataset.

    return good_dicts

def std_datetime(dict_list, verbose=False):
    """
    Converts datetimes to UTC timezone.

    If a time is invalid (cannot be converted) that entry is invalid -> removed.
    """
    good_dicts = []
    bad_dicts = []
    for i, cur_dict in enumerate(dict_list):
        if "createdAt" in cur_dict.keys(): # if it has the createdAt attribute
            try:
                in_time = cur_dict['createdAt']
                parsed = datetime.strptime(in_time, '%Y-%m-%dT%H:%M:%S%z')


                TZ = parsed.utcoffset() # get the UTC offset of the string (the timezone)
                TZ_name = parsed.tzname()
                parsed_sub = parsed - TZ
                parsed_utc = parsed_sub.astimezone(tz=timezone.utc)
                cur_dict['createdAt'] = parsed_utc.strftime('%Y-%m-%dT%H:%M:%S%z')
                if(verbose):
                    print("Input time: ", in_time, "Output time: ", parsed_utc)
            except Exception as e:
                print(i, e, " Not a valid date: ", in_time)
                bad_dicts.append(cur_dict) # just for testing
                continue

        good_dicts.append(cur_dict) # if it passes, append to the good_dicts

    return good_dicts # return 

