from pathlib import Path as P
import json

def merge_json_save(input_folder_path):
    input_dir = P(input_folder_path)

    compile_dict = {} 
    
    for file_path in input_dir.glob("*.json"):
        with open(file_path, "r", encoding = "utf-8") as f:
                input_file = json.load(f)
        
        results = input_file["results"][0]

        name = results["card_info"]["name"]

        compile_dict[name] = results
    
    final = {
         "type": "CardCollection",
         "cards" : [
            {
                 "type" : "Card",
                 "results" : d
            } for d in compile_dict.values()
         ]
    }

    file_name = "etl/compiled.json"

    with open(file_name, mode = "w", encoding = "utf-8") as f:
         json.dump(final, f, indent = 2)

def merge_json_return(input_folder_path):
    input_dir = P(input_folder_path)

    compile_dict = {} 
    
    for file_path in input_dir.glob("*.json"):
        with open(file_path, "r", encoding = "utf-8") as f:
                input_file = json.load(f)
        
        results = input_file["results"][0]

        name = results["card_info"]["name"]

        compile_dict[name] = results
    
    final = {
         "type": "CardCollection",
         "cards" : [
            {
                 "type" : "Card",
                 "results" : d
            } for d in compile_dict.values()
         ]
    }

    return final