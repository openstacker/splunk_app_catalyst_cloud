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

import splunk.admin as admin


class ConfigApp(admin.MConfigHandler):
    def setup(self):
        if self.requestedAction == admin.ACTION_EDIT:
            for arg in ['baseurl', 'tenant']:
                self.supportedArgs.addOptArg(arg)

    def handleList(self, confInfo):
        confDict = self.readConf("myconf")
        if confDict:
            for stanza, settings in confDict.items():
                for key, val in settings.items():
                    if key in ['baseurl', 'tenant'] and not val:
                        val = ''
                    confInfo[stanza].append(key, val)

    def handleEdit(self, confInfo):
        name = self.callerArgs.id
        args = self.callerArgs  
        self.writeConf('myconf', 'userinfo', self.callerArgs.data)


admin.init(ConfigApp, admin.CONTEXT_NONE)
