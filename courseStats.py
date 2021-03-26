import subprocess
import time
import glob
import os
import natsort

def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

list_of_files = natsort.natsorted(glob.glob('**/*.mp4'))
last = max(list_of_files, key=os.path.getatime)

print("Last Video Accessed: "+last)

counter=0
for i in range(0,list_of_files.index(last)):
	counter+=(get_length(list_of_files[i]))
print("Finished:"+ str(round(counter/3600,2))+" hours")
done=counter

counter=0
for i in range(list_of_files.index(last),len(list_of_files)):
	counter+=(get_length(list_of_files[i]))
print("Left:"+ str(round(counter/3600,2))+" hours")
print()
print("Percentage:"+ str(round((100*(done/counter)),2)))