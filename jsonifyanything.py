#!/usr/bin/env python3
import json

def write_json(data):
    with open("data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


def main(*args, **kwargs):
    return (args, kwargs)

if __name__ == "__main__":
    try:
        json_response = main(123, 5, j="g")
        write_json(json_response)
        print(json_response)

    except Exception as e:
        raise Exception(f"An error occurred in the main script: {e}") from e
