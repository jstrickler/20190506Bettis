#!/usr/bin/python3

import os
import os.path

os.environ["COUNT"] = "42"
print("count is",os.environ['COUNT'],"user is",os.environ['USER'])
print("count is",os.environ.get('COUNT'),"user is",os.environ.get('USER'))
user = os.getenv("USER")
count = os.getenv("COUNT")
print("count is",count,"user is",user)
print(os.path.expandvars("count is $COUNT user is $USER"))

