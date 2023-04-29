import json
from utils.utils import *
from utils.dart_converter import *
import os


def open_json_files_content():
    json_files_content = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_dir = os.path.join(script_dir, "json")
    for file in os.listdir(json_dir):
        if file.endswith(".json"):
            with open(os.path.join(json_dir, file), "r") as json_file:
                json_files_content.append(json_file.read())
    return json_files_content


def write_dart_file(file_name, content):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dart_dir = os.path.join(script_dir, "dart")
    file_path = os.path.join(dart_dir, file_name)
    with open(file_path, "w") as file:
        file.write(content)


def json_to_dart(json_to_convert):
    json_dict_collections = json.loads(json_to_convert)["collections"]
    for json_dict in json_dict_collections:
        class_name = generate_class_name(json_dict)
        dart_content = json_to_dart_string(class_name, json_dict)

        write_dart_file(json_dict["name"].lower() + "_model.dart", dart_content)


def main():
    list_json_files = open_json_files_content()
    for json_file in list_json_files:
        json_to_dart(json_file)


if __name__ == "__main__":
    main()
