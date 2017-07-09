#!/usr/bin/python

# Copyright (c) 2017 Catalyst Cloud Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import argparse
import requests
from pprint import pprint
import json
import os
import random
from auth import *

SERVICE_NAME = "cinder"


def main():
    session_key = sys.stdin.readline().strip()
    token, auth_catalog = get_token(session_key)
    base_url = get_baseURL(SERVICE_NAME, auth_catalog)
    headers = {'content-type': 'application/json','X-Auth-Token':token}
    response = requests.get(base_url + '/volumes', headers=headers).json()
    print("volumes_count=%s" % len(response["volumes"]))

if __name__ == "__main__":
    main()
