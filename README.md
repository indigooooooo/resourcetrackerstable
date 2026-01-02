Resource Tracker - (C) 2025 Tanner Lucier

Licensed under GPLv3 - see LICENSE file for details

==================================================================================================================================

Built this more for myself as an aid to my FrameKeep project (which is on my github)
to see how the program reacted with my system over the day and across various tasks.
However I see how people could use this.

Simple script that logs the resource use of a certain process, by a user given PID

==================================================================================================================================

The default path for log folders is "C:\Users\YOU\Documents\Resource Tracker Logs"

Instructions for .exe users:

1. Download the .zip file for the repo, and extract it where you would like it to sit for
   its lifetime.

2. Double click ResourceTrackerStable.exe to open it, look through the list for your
   program (or find its PID in Task Manager details), type in the process's PID, and
   after you hit enter it'll start logging the process. You can do Ctrl+P in the console 
   and paste your files path to change the path that logs go to. Thats it! Feel free to 
   delete this readme, and every file besides .exe after figuring the application out.

Instructions for Python users:

Follow Step 1 above, and run the dependencies.bat file

1. Opening with the terminal is easy as right clicking the folder the script is in, 
   clicking "Open in Terminal", and pasting this line of code;
    
    "python ResourceTrackerv1.1.0-stable.py"

    You can also open any terminal instance, type; 
    
    "cd c:\Users\you\yourfolder\resourcetrackerstable-main"

    Following with the same line earlier;

    "python ResourceTrackerv1.1.0-stable.py"

==================================================================================================================================

Customization for Python users:

The only customization in this script is how often the script grabs your 
process's information, and where the logs save to.

To change the path file to where the logs go to, do Ctrl+P in the console 
and paste your files path to change the path that logs go to. You can hit 
enter to revert to the default path. Thats it!

Change the parameter in ResourceTrackerv1.1.0-stable.py, under "LOG_INTERVAL", 
and enter how many seconds you want in between logs.

==================================================================================================================================

Average Disk Usage Statistics @ Log/5s
- Average Disk Usage/hr ≈ 60.62 KB/hr
- Average Disk Usage/24hr ≈ 1.4 MB/24hr

==================================================================================================================================

Dependencies explained:

psutil - Cross-platform library for retrieving information on running processes and system utilization.