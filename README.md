##🎵 **JSON to LRC Converter**##

This is a simple Python script that converts lyrics data from a JSON format (such as those used in transcription or lyrics APIs) into LRC format—a common format for timestamped lyrics used in karaoke players and media applications.
###📦 **Features**###

  - Converts JSON-based lyrics to LRC format

  - Supports millisecond-precision timestamps

  - Clears terminal screen for a clean user interface

  - Option to export the LRC output as a .lrc file

###🛠 **Requirements**###

    Python 3.x


###🚀 **Usage**###

Run the script:

    python main.py

Enter the JSON string when prompted. Example format:

    {
      "lyrics": {
        "lines": [
          {"startTimeMs": "1000", "endTimeMs": "4000", "words": "Hello world"},
          {"startTimeMs": "5000", "endTimeMs": "8000", "words": "How are you?"}
        ]
      }
    }


The script will convert this to LRC format:

    [00:01.000] Hello world
    [00:05.000] How are you?

    Choose whether to export the result as an .lrc file.

###🧠 **How It Works**###

  convert_to_lrc(json_str): Parses the input JSON, extracts line-by-line lyrics and their timestamps, then formats them into the LRC structure.

  millis_to_minutes_and_seconds(millis): Converts milliseconds into [mm:ss.SSS] format required by LRC.

  The script interacts with the user via the command line and offers an export option.

###📁 **Output**###

If you choose to export, an .lrc file will be created in the same directory as the script using your provided filename.

###❗ **Notes**###

  - Input JSON must be properly formatted, including valid numeric strings for "startTimeMs" and "endTimeMs".

  - This script does not validate overlapping timestamps or incorrect logical sequences in lyrics lines.

###📝 **License**###

This project is open for any use and modification. No license required.
