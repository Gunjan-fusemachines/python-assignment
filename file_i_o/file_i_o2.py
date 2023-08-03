# creating add to json function
import json

def add_to_json(filename, new_data):
    try:
        # Read existing JSON data from the file
        with open(filename, 'r') as file:
            existing_data = json.load(file)

        # Append the new dictionary to the existing data
        existing_data.append(new_data)

        # Write the updated data back to the same file as JSON
        with open(filename, 'w') as file:
            json.dump(existing_data, file)

        print("Data added successfully to", filename)
    except FileNotFoundError:
        print("File not found:", filename)
    except json.JSONDecodeError:
        print("Error decoding JSON data from the file.")
    except Exception as e:
        print("Error:", str(e))

# Sample JSON data
existing_json_data = [
    {
        "name": "Ram",
        "age": 30
    },
    {
        "name": "Sita",
        "age": 25
    }
]

# Sample new data to add to the JSON
new_data = {
    "name": "Lakshman",
    "age": 28
}

# Name of the JSON file
json_filename = "file_i_o/data.json"

# Write the sample JSON data to the file
with open(json_filename, 'w') as file:
    json.dump(existing_json_data, file)

# Call the function to add the new data to the JSON file
add_to_json(json_filename, new_data)
