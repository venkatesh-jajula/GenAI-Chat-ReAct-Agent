import json
from pathlib import Path

DATA_DIRECTORY = Path(__file__).parent.parent / "data"
#print(DATA_DIRECTORY)

def load_json_data(file_name):
    path = DATA_DIRECTORY / file_name
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def load_entire_data():
    sushi = load_json_data("sushi.json") 
    parking = load_json_data("parking.json")
    # print(f"✅ Loaded {len(sushi)} sushi entries and {len(parking)} parking entries.")
    return sushi,parking

if __name__ == "__main__":
    sushi,parking = load_entire_data()
