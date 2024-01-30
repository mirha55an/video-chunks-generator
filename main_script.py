from moviepy.editor import *

videoclip = VideoFileClip("Enter the path to the video file.")
duration = videoclip.duration
interval = int(input("Enter the length of chunks in seconds :"))
while duration < interval:
    print("Input cannot exceed the length of the video!")
    interval = int(input("Enter the length of chunks in seconds :"))
start = 0
clips = []
while start < duration :
    end = start + interval

    if end > duration:
        end = duration
    
    clip = videoclip.subclip(start,end)
    clips.append(clip)
    start = end
print(clips)

for i in range(len(clips)):
    newclip = clips[i] 
    newclip.write_videofile(f"clip{i+1}.mp4")
    

