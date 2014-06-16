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
# Date: 2014/6/15                                                 #
# Count distribution of number of activities for each time period.#
###################################################################

import sys, csv, json, argparse, datetime
import numpy as np
from collections import defaultdict

with open("../SETTINGS.json") as fp:
    settings = json.loads(fp.read())
dt = datetime.datetime.now()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str, action='store',
            dest='data_num', help='choose which data set to use')
    if len(sys.argv) != 3:
        print 'Command e.g.: python segmentData.py -d 1(11,12,...)'
        sys.exit(1)

    para = parser.parse_args()
    if para.data_num == "1":
        datain_path = settings["ROOT_PATH"] + settings["SRC_DATA_FILE1_1"]
        trainout_path = settings["ROOT_PATH"] + settings["DATA1_TRAIN"]
        valiout_path = settings["ROOT_PATH"] + settings["DATA1_VALIDATION"]
        testout_path = settings["ROOT_PATH"] + settings["DATA1_TEST"]
    elif para.data_num == "11":
        datain_path = settings["ROOT_PATH"] + settings["SRC_DATA_FILE1_CITY1"]
        trainout_path = settings["ROOT_PATH"] + settings["DATA1_CITY1_TRAIN"]
        valiout_path = settings["ROOT_PATH"] + settings["DATA1_CITY1_VALIDATION"]
        testout_path = settings["ROOT_PATH"] + settings["DATA1_CITY1_TEST"]
    elif para.data_num == "12":
        datain_path = settings["ROOT_PATH"] + settings["SRC_DATA_FILE1_CITY2"]
        trainout_path = settings["ROOT_PATH"] + settings["DATA1_CITY2_TRAIN"]
        valiout_path = settings["ROOT_PATH"] + settings["DATA1_CITY2_VALIDATION"]
        testout_path = settings["ROOT_PATH"] + settings["DATA1_CITY2_TEST"]
    else:
        print 'Invalid choice of dataset'
        sys.exit(1)

    time_list = []
    for line in open(datain_path):
        time_str = line.strip("\r\t\n").split(",")[8]
        time_list.append(time_str)
    time_list = sorted(time_list)
    total_entry_num = len(time_list)
    train_entry_num = int(total_entry_num*settings["TRAIN_RATIO"])
    vali_entry_num  = int(total_entry_num*settings["VALI_RATIO"])
    test_entry_num  = total_entry_num - train_entry_num - vali_entry_num

    trseg_time = time_list[train_entry_num]
    vaseg_time = time_list[train_entry_num + vali_entry_num]

    tr_wfd = open(trainout_path, "w")
    va_wfd = open(valiout_path, "w")
    te_wfd = open(testout_path, "w")
    for line in open(datain_path):
        time_str = line.strip("\r\t\n").split(",")[8]
        if time_str < trseg_time:
            tr_wfd.write(line)
        elif time_str < vaseg_time:
            va_wfd.write(line)
        else:
            te_wfd.write(line)
    tr_wfd.close()
    va_wfd.close()
    te_wfd.close()

if __name__ == "__main__":
    main()

