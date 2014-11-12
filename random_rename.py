#!/usr/bin/python

import os
import random

lof = os.listdir('.')
df = [lof.remove(f) for f in lof if f.endswith('.py')]

i = 0
while (i < 150):
	rand_file = random.choice(lof)
	rand_num = random.randint(100000,999999)
	new_name = str(rand_num)+"-file-"+str(rand_num)
	os.rename(rand_file, new_name)
	lof.remove(rand_file)
	i = i + 1
