import json
from pathlib import Path

def json_reader(path:Path):
    """

    Read current Json File.

    """
    file = Path(path)

    if not file.exists():
        return []
    
    with open(file,"r",encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as err:
            print("Something Went Wrong About JSON File... errcode: "+err)
            return []
        
        return data


def json_writer(path:Path,data:list):
    """
    Write content to JSON file
    """
    try:
        with open(path,"w",encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)
    except json.JSONDecodeError as err:
        print("Something Went Wrong About JSON File... errcode: "+err)
