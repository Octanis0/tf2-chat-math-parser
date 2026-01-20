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

## parser1 vs parser2
`parser1` will auto calculate the challenge and show it in the terminal.  

`parser2` will do the same, and write it into a .cfg file. Bind a key to execute this .cfg to automatically say the answer in chat.

## Requirements
- TF2
- Python

## Configuration
### parser1
1. Set TF2 to write the console output into a logfile.  
Use `con_logfile` in the console to set a path.
TF2 generates this logfile in the `.../Team Fortress 2/tf` folder.  
For example, `con_logfile test.log` will write into `.../Team Fortress 2/tf/test.log`

1. If using `parser1.py`, change `FILENAME` and `SLEEPTIME` accordingly:  
	- `FILENAME`: Change this to the logfile that TF2 is writing to. Full path expected.  
	- `SLEEPTIME`: This determines how long the script sleeps for (in seconds) before reading for new output.  

### parser2
1. Set TF2 to write the console output into a logfile.  
Use `con_logfile` in the console to set a path.  
TF2 generates this logfile in the `.../Team Fortress 2/tf` folder.  
For example, `con_logfile test.log` will write into `.../Team Fortress 2/tf/test.log`  
Use `bind KEY "exec filename"` in TF2 console.  
For example, `bind KP_END "exec parseout"` will execute the command in `.../Team Fortress 2/tf/cfg/parseout.cfg` when keypad 1 is pressed.  

1. If using `parser2.py`, change `FILENAME`, `SLEEPTIME` and `EXECFILE`:
	- `FILENAME`: Change this to the logfile that TF2 is writing to. Full path expected.  
	- `SLEEPTIME`: This determines how long the script sleeps for (in seconds) before reading for new output. 
	- `EXECFILE`: Change this to the exec .cfg that you want to execute. Full path expected.  


## Run
	python parser1.py
or  

	python parser2.py

## Stop
Ctrl+C to stop.  
For `parser2.py`, the .cfg file will be emptied on exit.  