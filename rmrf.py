import os
import shutil
import sys

paths = []
for x in sys.argv[1:]:
	path = x.split(',')[0].replace(' ','\ ')
	print path
	paths.append(path)

confirm = raw_input("confirm delete -> ")
if confirm == 'yes':
	for path in paths:
		command = 'rm -rf ' + path
		print command
		os.system(command)
else:
	print 'no - exiting'