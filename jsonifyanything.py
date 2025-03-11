#!/usr/bin/env python3
from collections.abc import Iterable
import json

win='Data written'
fail='Data not written.'

def is_json_serializable(obj):
    try:
        json.dumps(obj)
        return True
    except (TypeError, OverflowError):
        return False

def clean_data(data):

    if isinstance(data, Iterable):
        clean_data(data)
    
    elif is_json_serializable(data):
        return data
    
    else:
        new_data=f''' Could not convert data below.
            
            {str(data)}
        
        '''
        type(new_data)
        print(new_data)
        return new_data

def write_json(data):
    try:
        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

    except Exception as e:
        clean_data(data)
        
def main(*args, **kwargs):
    if args and kwargs:
        # TODO: make decision
        write_json((args, kwargs))
        return win

    elif args:
        # TODO: make decision
        return fail

    elif kwargs:
        # TODO: make decision
        return fail

    else:
        return win


if __name__ == "__main__":
    try:
        # din=pd.read_csv('data.csv')
        # json_response = main(din, 123, 5, j="g")
        var=set()
        json_response=main(var, v=var)
        print(json_response)

    except Exception as e:
        raise Exception(f"An error occurred in the main script: {e}") from e
