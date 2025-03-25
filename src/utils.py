import json
import os


def reader_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):



if __name__ == "__main__":
    raw_data = reader_json("../data/products.json")
    print(type(raw_data))
    print(type(raw_data))