# Veeam-Software-QA-test

Solved test task for Veeam Software from Gulyan Konstantin. 


## Task: 

Implement a program that synchronizes two folders: source and replica. The program should maintain a
full, identical copy of source folder at replica folder.
Solve the test task by writing a program in one of these programming languages (solved with Python)


Requirements:
Synchronization must be one-way: after the synchronization content of the replica folder should
be modified to exactly match content of the source folder;

Synchronization should be performed periodically

File creation/copying/removal operations should be logged to a file and to the console output;

Folder paths, synchronization interval and log file path should be provided using the command
line arguments;

It is undesirable to use third-party libraries that implement folder synchronization;

It is allowed (and recommended) to use external libraries implementing other well-known
algorithms. For example, there is no point in implementing yet another function that calculates
MD5 if you need it for the task – it is perfectly acceptable to use a third-party (or built-in)
library.


## Quick start: 

> python3 sync_script.py arg1 arg2 arg3 arg4 

where: 

arg1 = main folder path

arg2 = backup folder path

arg3 = log file path

arg4 = time sync interval in ms