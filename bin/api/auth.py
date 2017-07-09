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

import argparse
import sys
import io
import json
import os
import requests
import ConfigParser
import splunk.entity as entity


def get_credential(session_key):
    app_name = "splunk_app_catalyst_cloud"

    try:
       entities = entity.getEntities(['admin', 'passwords'], namespace=app_name, 
                                     owner='nobody', sessionKey=session_key) 
    except Exception as e:
       raise Exception("Failed get %s credentials from splunk. Error: %s" 
                       % (app_name, str(e)))

    user = entities[entities.keys()[0]]
    return user['username'], user['clear_password']


def get_token(session_key):
    username, password = get_credential(session_key)
    headers = {'content-type': 'application/json'}

    Config = ConfigParser.ConfigParser()
    PATH = os.path.dirname(os.path.realpath(__file__))
    with io.open(PATH+"/./../../local/myconf.conf", 'r',
                 encoding='utf_8_sig') as fp:
        Config.readfp(fp)

    if 'userinfo' in Config.sections():
        base_url = Config.get("userinfo", 'baseurl')
        tenant = Config.get("userinfo", 'tenant')

    token = None
    auth_catalog = None
    try:
        auth_body = { "auth": {"identity":
                               {"methods": ["password"],
                                "password": {"user": {"name": username,
                                                      "domain": { "id":
                                                                 "default"},
                                                      "password": password}
                                             }
                                },
                               "scope": {"project": {"name": tenant,
                                                     "domain": {"id": "default"
                                                                }
                                                     }
                                         }
                               }
                     }
        resp = requests.post(base_url + '/auth/tokens',
                             data=json.dumps(auth_body),
                             headers=headers)
        auth_catalog = resp.json()
        token = resp.headers["x-subject-token"]
        if not auth_catalog['token']['user']['id']:  
            raise Exception("Authentication failed. Failed to get auth token.")
    except Exception as e:
        print('CRITICAL: Athentication failed for tenant %s and user %s' %
              (tenant, user_name) + '\nException: ' + str(e))

    return token, auth_catalog


def get_baseURL(serviceName, auth_catalog):
    for service in auth_catalog['token']['catalog']:
        if serviceName in service['name']:
            return service['endpoints'][0]['url']


if __name__ == "__main__":
    pass
