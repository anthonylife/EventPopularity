#!/usr/bin/env python
#encoding=utf8

#Copyright [2014] [Wei Zhang]

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#http://www.apache.org/licenses/LICENSE-2.0
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

###################################################################
# Date: 2014/6/16                                                 #
# Extract titles of activities                                    #
###################################################################

import csv, json, sys
from collections import defaultdict

with open("../SETTINGS.json") as fp:
    settings = json.loads(fp.read())


def main():
    eventinfo_path = settings["ROOT_PATH"] + settings["SRC_DATA_FILE1_1"]
    eventtitle_path = "./eventTitle.csv"

    wfd = open(eventtitle_path, "w")
    for i, line in enumerate(open(eventinfo_path)):
        event_id = line.strip("\r\t\n").split(",")[0]
        title = line.strip("\r\t\n").split(",")[4]
        location = line.strip("\r\t\n").split(",")[2]
        wfd.write("%s,%s,%s\n" % (event_id, title, location))
    wfd.close()

if __name__ == "__main__":
    main()
