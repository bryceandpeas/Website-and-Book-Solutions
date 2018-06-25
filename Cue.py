'''
Git-Cue 
Commit and Push files from local directory to remote, if not already present on remote, daily from one year prior to the current date.
[CLI V 1.0 - Python 3]
'''

from datetime import datetime, timedelta
import itertools
import json
import math
import os
import random
import subprocess
import time
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

root = 'C:\\Users\\bryce\\Desktop\\Website-Solutions'

print(os.getcwd())

file_list = []
date_list = []
commit_list = []
today = datetime.today()
date = datetime.today() - timedelta(days=260)
weekday = datetime.weekday(date)

while weekday < 6:
	date = date + timedelta(1)
	weekday = datetime.weekday(date)

exclude = set(['.git'])
for path, subdirs, files in os.walk(root):
	subdirs[:] = [d for d in subdirs if d not in exclude]
	for name in files:
		if name.endswith(".gitignore") or name.endswith(".md"):
			continue
		else:
			file_list.append(os.path.join(path, name))

for file in file_list:
	date_list.append(date)
	rand_hour = random.randint(18, 23)
	rand_minute = random.randint(00, 59)
	rand_second = random.randint(00, 59)
	date += timedelta(days=1)
	date = date.replace(hour=rand_hour, minute=rand_minute, second=rand_second)

count = 0

for file in file_list:
	filename = str(file).rsplit('\\', 1)[1]
	commit_message = 'Add {0} solution'.format(filename)
	os.environ["GIT_COMMITTER_DATE"] = "{0}".format(date_list[count])
	print('Set commiter date to: ')
	#print(subprocess.Popen(["set", "GIT_COMMITTER_DATE",], stdout=subprocess.PIPE))
	os.environ["GIT_AUTHOR_DATE"] = "{0}".format(date_list[count])
	print('Set author date to: ')
	#print(subprocess.Popen(["set", "GIT_AUTHOR_DATE"], stdout=subprocess.PIPE))
	subprocess.Popen(["git", "add", "{0}".format(file)], stdout=subprocess.PIPE)
	print('Added: {0}'.format(file))
	subprocess.Popen(["git", "commit", "--allow-empty", "-m" "{0}".format(commit_message)], stdout=subprocess.PIPE)
	print('Commit message: "' + commit_message+ '"')
	subprocess.Popen(["git", "push", "origin", "master"], stdout=subprocess.PIPE)
	print('Pushed')
	count += 1
	print('Sleep 20')
	time.sleep(20)

print('Processed {0} files'.format(count))