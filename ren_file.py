import uuid
import os
import time
 
#DIR = '/dir/i/dont/care/about'
DIR = '/home/amit/try'

CREATE_FILE = "YES"
iteration=50
num_of_files=1000


if CREATE_FILE == "YES":
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    for _ in range(num_of_files):
        open(os.path.join(DIR, str(uuid.uuid1())), 'a').close()
    print ("File creation complete. Created %d" %num_of_files)
 
for _ in range(iteration):
    for filename in os.listdir(DIR):
        os.rename(os.path.join(DIR, filename), os.path.join(DIR, str(uuid.uuid1())))
        time.sleep(0.01)
    print _
