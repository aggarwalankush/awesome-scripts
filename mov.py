import datetime
import subprocess
import sys
from time import time

if len(sys.argv) < 2:
    print("DUDE!! Give 'mov' file name to convert to 'mp4'")
    exit()

command = 'ffmpeg -i $1 -preset ultrafast $2'
# command = 'ffmpeg -i $1 -preset ultrafast -codec:v libx264 -pix_fmt yuv420p -b:v 1000k -minrate 500k -maxrate 2000k -bufsize 2000k -vf scale=854:480 $2'

inputFileName = str(sys.argv[1]).split(".")[0] + '.mov'

if len(sys.argv) > 2:
    outputFileName = str(sys.argv[2]).split(".")[0] + '.mp4'
else:
    outputFileName = str(sys.argv[1]).split(".")[0] + '.mp4'

command = command.replace("$1", inputFileName).replace("$2", outputFileName)

print("running command - ", command)

# os.system(command)
t1 = time()
startTime = datetime.datetime.now()
print('Start time - ', startTime)
try:
    subprocess.call(command, shell=True)
except:
    print('Failed')
    pass
t2 = time()
print('Start time - ', startTime)
print('End time - ', datetime.datetime.now())
print('Elapsed time is ', datetime.timedelta(seconds=(t2 - t1)))
