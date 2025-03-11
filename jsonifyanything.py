#!/usr/bin/env python3
from collections.abc import Iterable
import json

win = "Data written"
fail = "Data not written."

def is_json_serializable(obj):
    """
    Check if an object is JSON serializable.
    """
    try:
        json.dumps(obj)
        return True
    except (TypeError, OverflowError):
        return False

def clean_data(data):
    """
    Recursively replace non-serializable data with a placeholder.
    """
    if isinstance(data, dict):  # Handle dictionaries
        return {key: clean_data(value) for key, value in data.items()}
    
    elif isinstance(data, list):  # Handle lists
        return [clean_data(item) for item in data]
    
    elif isinstance(data, set):  # Convert sets to lists
        return [clean_data(item) for item in data]
    
    elif isinstance(data, tuple):  # Convert tuples to lists
        return [clean_data(item) for item in data]

    elif is_json_serializable(data):
        return data
    
    else:
        return "placeholder"

def write_json(data):
    """
    Writes data to a JSON file, ensuring it's serializable.
    """
    try:
        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        return win  # Success
    except Exception:
        cleaned_data = clean_data(data)
        with open("data.json", "w") as json_file:
            json.dump(cleaned_data, json_file, indent=4)
        return fail  # Partial failure

def main(*args, **kwargs):
    """
    Accepts any wildcard input and processes it for JSON writing.
    """
    data = {"args": args, "kwargs": kwargs}

    return write_json(data)

if __name__ == "__main__":
    try:
        # Example wildcard inputs
        wild_values = [
            {"name": "Alice", "age": 30},
            [1, 2, 3],
            set([5, 6, 7]),  # Set will be converted
            lambda x: x,  # Function will be replaced
            (8, 9, 10)  # Tuple will be converted
        ]

        json_response = main(*wild_values, key1="value1", key2=set(["x", "y"]))
        print(json_response)

    except Exception as e:
        raise Exception(f"An error occurred in the main script: {e}") from e
