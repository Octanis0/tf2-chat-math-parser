import time
import re
import argparse


FILENAME="D:/Steam/steamapps/common/Team Fortress 2/tf/test.log"
SLEEPTIME=1
EXECFILE="D:/Steam/steamapps/common/Team Fortress 2/tf/cfg/parseout.cfg"


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action='store_true')
arg = parser.parse_args()
if arg.verbose:
	print("\nStarting log parser. Target file is", FILENAME)
	print("Set con_logfile to this file to maintain a reading stream.")
with open(FILENAME, 'r', errors='ignore') as f:
	end = False
	try:
		while True:
			logline = f.readline()
			if logline == "":
				if not end and arg.verbose:
					end = True
					print("End of line reached. Will check for more output every", SLEEPTIME, "seconds.")
				time.sleep(SLEEPTIME)
			else:
				if re.search(r"^\[Math\] \d+ . \d+", logline):
					if arg.verbose:
						print("Found a match!")
						print(logline.strip())
					mathline = logline.split()
					result = None
					match mathline[2]:
						case '+':
							result = int(mathline[1])+int(mathline[3])
						case '-':
							result = int(mathline[1])-int(mathline[3])
						case '*':
							result = int(mathline[1])*int(mathline[3])
						case '/':
							result = int(mathline[1])//int(mathline[3])
					if result is not None:
						print(mathline[1], mathline[2], mathline[3])
						print(result, "\n")
						with open(EXECFILE, 'w') as auto_f:
							auto_f.write('say ' + str(result))
	except KeyboardInterrupt:
		print("Program close. Remember to clean your con_logfile.")
		with open(EXECFILE, 'w') as auto_f:
			auto_f.write('')