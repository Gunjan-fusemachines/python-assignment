# creating search log function
def search_log(log_file, search_keyword):
    try:
        # Open the log file in read mode
        with open(log_file, 'r') as file:
            for line in file:
                # Check if the search keyword is present in the line
                if search_keyword in line:
                    print(line.strip())  # Print the line (strip newline character)
    except FileNotFoundError:
        print("File not found:", log_file)
    except Exception as e:
        print("Error:", str(e))

# Sample log file name
log_filename = "sample.log"

# Sample search keyword
keyword_to_search = "error"

# Sample log data in the file
sample_log_data = """
[2023-08-03 10:23:15] INFO: Application started
[2023-08-03 10:24:32] WARNING: Database connection lost
[2023-08-03 10:25:01] ERROR: Disk space low
[2023-08-03 10:27:55] INFO: Task completed
"""

# Write the sample log data to the file
with open(log_filename, 'w') as file:
    file.write(sample_log_data)

# Call the function to search for the keyword in the log file
search_log(log_filename, keyword_to_search)
