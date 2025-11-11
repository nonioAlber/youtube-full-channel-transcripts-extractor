thonimport json

def export_to_json(data, filename):
    """
    Exports the data to a JSON file.
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)