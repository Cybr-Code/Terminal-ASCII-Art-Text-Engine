import text_engine
import os
import time
print('This is a simple ASCII Art Text Engine for the Terminal!')
time.sleep(2)
while True:
	entry = input('What would you like to enter? \n')
	os.system('cls' if os.name == 'nt' else 'clear')
	text_engine.write(entry)
	time.sleep(5)
	#os.system('cls' if os.name == 'nt' else 'clear')
	c = input('Continue? \n')
	if c.lower() == 'no':
		break
	os.system('cls' if os.name == 'nt' else 'clear')
