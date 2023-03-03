import json
import os

def convert_to_lrc(json_str):
    try:
        json_obj = json.loads(json_str)
        lyrics_obj = json_obj['lyrics']
        lines_array = lyrics_obj['lines']
        lrc_string = ""

        for line in lines_array:
            start_time_ms = int(line['startTimeMs'])
            end_time_ms = int(line['endTimeMs'])
            words = line['words']
            time = millis_to_minutes_and_seconds(start_time_ms) + " " + words
            lrc_string += time + "\n"

        return lrc_string
    except ValueError:
        return "Invalid JSON input"

def millis_to_minutes_and_seconds(millis):
    minutes = int(millis / 60000)
    seconds = round((millis % 60000) / 1000, 3)
    return "[" + str(minutes).zfill(2) + ":" + str(seconds).zfill(6) + "]"

# Get JSON input from the user
json_input = input("Enter JSON string: ")

os.system('cls' if os.name == 'nt' else 'clear')

# Convert to LRC format
lrc_output = convert_to_lrc(json_input)

# Print the output
print("LRC output:")
print(lrc_output)

# Ask user if they want to export the file
export_file = input("Do you want to export the LRC file? (y/n): ")
if export_file.lower() == "y":
    # Ask user for file name
    file_name = input("Enter a name for the LRC file: ")
    with open(file_name + ".lrc", "w", encoding="utf-8") as f:
        f.write(lrc_output)
        print("File exported successfully!")
else:
    print("Exiting program.")