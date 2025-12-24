Built this more for myself as an aid to my FrameKeep project (which is on my github)
to see how the program reacted with my system over the day and across various tasks.
However I see how people could use this.

Simple script that logs the resource use of a certain process, by a user given PID

Instructions:

1. Download the .zip file for the repo, and extract it where you would like it to sit for
   its lifetime. The tracker will upload the log to whatever folder the .exe file is at,
   so I would recommend just leaving it in the folder it comes in.

2. Double click ResourceTrackerStable.exe to open it, look through the list for your
   program (or find its PID in Task Manager details), type in the process's PID, and
   after you hit enter it'll start logging the process. Thats it!

Future fixes:

Nothing needs to be "fixed" right now, however I would like to eventually add the option
to monitor more than one process at a time.

Dependencies explained:

psutil → sees what your program is doing.
time → waits between checks.
os → saves files in the right place.
datetime → writes when the check happened.
uuid → makes every log file unique.