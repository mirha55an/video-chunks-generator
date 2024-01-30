# Instructions for Use

# File Path

First configure the file path for the videoclip variable.

# Input

Give your input in seconds and make sure it doesn't exceed the length of the original video clip otherwise it will not proceed further and ask you to re-enter the input.

# Save Path

You can configure the path for your save file and name in the "newclip.write_videofile(f"clip{i+1}.mp4")" line or you can leave it at default but make sure you dont remove the "{i}" part otherwise it will only generate a single clip of the last interval and not work.