#!/usr/bin/python

import sys
import argparse
import requests
from pprint import pprint
import json
import os
import random


def main():
    available_volume_count = random.randint(1, 100)
    inuse_volume_count = random.randint(1, 100)
    available_volume_size = random.randint(1, 100)
    inuse_volume_size = random.randint(1, 100)
          
    #Print console line with volumes stats information
    print "available_volume_count="+str(available_volume_count)+",inuse_volume_count="+str(inuse_volume_count)+",inuse_volume_size="+str(inuse_volume_size)+",available_volume_size="+str(available_volume_size)

if __name__ == "__main__":
    main()
