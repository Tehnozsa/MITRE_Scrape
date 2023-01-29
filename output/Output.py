import json
import pandas as pd

NAME_OUTPUT="Scrape_output"

def json_output(dictionary):
    with open(NAME_OUTPUT+".json", "w") as file:
        json.dump(dictionary,file)
    return True

def text_output(dictionary):
    for (name,name_dict) in dictionary.items():
        print("For "+name+":")
        for (ttp_ioc,list_value) in name_dict.items():
            print(ttp_ioc+": "+str(list_value)[1:-1].replace("'",""))
    input()
    return True

def file_output(dictionary):
    with open(NAME_OUTPUT+".txt","w") as file:
        for (name,name_dict) in dictionary.items():
            file.write("For "+name+":\n")
            for (ttp_ioc,list_value) in name_dict.items():
                file.write(ttp_ioc+": "+str(list_value)[1:-1].replace("'","")+"\n")
    return True

# ! TO DO: Improve how to see the data in CSV ! #
def csv_output(dictionary):
    json_obj = json.dumps(dictionary)
    df = pd.read_json(json_obj)
    df.to_csv(NAME_OUTPUT+".csv", encoding="utf-8", index=False)
    return True
