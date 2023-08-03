# task-7 file handling

# data.csv and adult.csv
import csv

def filter_adults(input_file, output_file):
    try:
        with open(input_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            adults = [row for row in reader if int(row['Age']) >= 18]

        with open(output_file, mode='w', newline='') as csvfile:
            fieldnames = ['Name', 'Age']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(adults)

        print(f"Filtered data saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError:
        print("Error: Invalid age format in the 'data.csv' file.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_file = "file_i_o\data.csv"
output_file = "adults.csv"
filter_adults(input_file, output_file)