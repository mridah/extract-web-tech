'''
    File        : run.py
    Description : Iterate a urls file and output a csv file of all website platform info  that can be extracted
    Author      : Mridul Ahuja
'''

import os,sys
import subprocess
import json

def get_info(url):
    return subprocess.getoutput('wad -u ' + url)

def printable_info(url, data):
    str = url + ','
    for each_item in data:
        str = str + each_item['app'] + ','

    return str


if __name__=="__main__":
    with open('data.csv', 'a') as fo:

        file1 = open('urls.txt', 'r')
        lines = file1.readlines()

        # Strips the newline character
        for line in lines:
            url = line.strip()
            print('Fetching ' + url)

            try:
                output = get_info('http://' + url)

                output_json = json.loads(output)
                for key in output_json.keys():
                    res = printable_info(url, output_json[key])

                fo.write(res + '\n')

            except Exception as e:
                print(str(e))
