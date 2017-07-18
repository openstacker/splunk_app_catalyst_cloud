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
import requests
from auth import *

SERVICE_NAME = "glance"
DEBUG = False


def main(username=None, password=None):
    session_key = None
    if not DEBUG:
        session_key = sys.stdin.readline().strip()
    token, auth_catalog = get_token(session_key, username=username,
                                    password=password)
    base_url = get_baseURL(SERVICE_NAME, auth_catalog, "nz-por-1")

    headers = {'content-type': 'application/json', 'X-Auth-Token': token}
    response = requests.get(base_url + '/v2/images', headers=headers).json()
    if DEBUG:
        print(response)
    images_count = len(response["images"])
    print("images_count=%d" % images_count)


if __name__ == "__main__":
    DEBUG = True
    # NOTE(flwang): After setup the app on your splunk, if it doesn't
    # work, then you can run this script directly to debug it. Just
    # simply replace the username and password below to debug the Glance
    # part.
    main(username="", password="")
