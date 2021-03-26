# Bulk Video Progress Tracker
Track folders containing videos to see how much of that TV series/video course have you completed. 

It uses ffprobe to calculate the duration of videos before and after the last accessed video and shows percentage of completed course/TV series that you are watching in current directory. It also scans all the subfolders for courses structured in folder like chapters to see the last file played via access time:

![Demo](https://raw.githubusercontent.com/bytebolt/video-course-tracker/main/screen.png)

Windows users need to download ffprobe binary and place them in the same directory else the will get file not found error.
https://ffbinaries.com/downloads
