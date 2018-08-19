#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 02:20:06 2018
for CN assignment
@author: devp
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import datetime
import csv

browser = webdriver.Firefox()

# Change host name here

host_name = "www.google.com"

# Change packet size here
'''packet sizes are 64, 128, 256, 512, 1024 and 2048 bytes'''

packet_size = str(64)

# Do nothing here

url_addr = "http://www.spfld.com/cgi-bin/ping?remote_host="+host_name+"&dns=on&count=10&size="+packet_size

browser.get(url_addr)

for x in range (20):
    WebDriverWait(browser, 30).until(
                                    EC.presence_of_element_located((By.TAG_NAME, "pre"))
                                    )
    text_element = browser.find_element_by_tag_name("pre")
    copy_string = text_element.text
    
    pingregex_ip = re.compile(r'PING.+\((\d+\.\d+\.\d+\.\d+)\)')
    mo_ip = pingregex_ip.search(copy_string)
    
    pingregex_loss = re.compile(r'(\d+\%) packet loss')
    mo_loss = pingregex_loss.search(copy_string)
    
    pingregex_stats = re.compile(r'mdev = (\d+\.?\d+)\/(\d+\.?\d+)\/(\d+\.?\d+)\/(\d+\.?\d+)')
    mo_stats = pingregex_stats.search(copy_string)
    
    time_now = datetime.datetime.now()
    
    dict_ping_details = {'name':host_name,
                      'IP address':mo_ip.group(1),
                      '% packet loss':mo_loss.group(1),                
                      'rtt min':mo_stats.group(1),
                      'rtt avg':mo_stats.group(2),
                      'rtt max':mo_stats.group(3),
                      'rtt mdev':mo_stats.group(4),
                      'time of day':time_now.hour,
                      'packet_size':packet_size
                      }
    # Change the file name to data_host2.csv when pinging to another host
    
    with open(r'data_host1.csv', 'a', newline='') as csvfile:
        fieldnames = ['name',
                      'IP address',
                      '% packet loss',
                      'rtt min',
                      'rtt avg',
                      'rtt max',
                      'rtt mdev',
                      'time of day',
                      'packet_size']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(dict_ping_details)

    browser.refresh()
