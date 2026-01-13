# TF2 Math Challenge autoparser
Reads a TF2 log file and auto-calculates the math challenge  

## Info
Some servers have math challenges in the chat.  
Anything that shows in the chat also shows up in the console.  
TF2 has `con_logfile` which writes console output into a log file.  
This script reads the log file and auto-calculates the result.  
The format of this challenge is assumed to be in this format:  

	[Math] 123 + 456 = ?? >50 credits<

Regex is used to extract the operands, operator and compute accordingly.  
The result is then printed on the terminal.  
The script will continuously pull new output coming from the console.  

## Requirements
- TF2
- Python

## Configuration
1. Set TF2 to write the console output into a logfile.  
Use `con_logfile` in the console to set a path.
TF2 generates this logfile in the `.../Team Fortress 2/tf` folder.  
For example, `con_logfile test.log` will write into `.../Team Fortress 2/tf/test.log`

1. In `parser.py`, change `FILENAME` and `SLEEPTIME` accordingly:  
	- `FILENAME`: Change this to the logfile that TF2 is writing to. Full path expected.  
	- `SLEEPTIME`: This determines how long the script sleeps for (in seconds) before reading for new output.  

## Run
	python parser.py

## Stop
Ctrl+C to stop.  