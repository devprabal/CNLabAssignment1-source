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

#list_of_host_name = []
#list_of_ip = []
#list_of_packet_loss = []
#list_of_rtt_min = []
#list_of_rtt_avg = []
#list_of_rtt_max = []
#list_of_rtt_mdev = []
#list_of_time_now = []

browser = webdriver.Firefox()
#browser.get('https://www.google.com')
#search_field = browser.find_element_by_name('q')
#search_field.send_keys('apu-ping-utility')
#search_button = browser.find_element_by_name('btnK')
#search_button.click()
#
#WebDriverWait(browser, 10).until(
#                                EC.presence_of_element_located((By.ID, "resultStats"))
#                                )
#browser.find_element_by_link_text("Apu - Ping Utility").click()

#browser.get('http://www.spfld.com/ping.html')
#WebDriverWait(browser, 10).until(
#                                EC.presence_of_element_located((By.NAME, "remote_host"))
#                                )
#search_field_apu = browser.find_element_by_name("remote_host")
#search_field_apu.send_keys(host_name)
#search_field_apu.send_keys(Keys.RETURN)

host_name = "lb-192-30-253-113-iad.github.com"

packet_size = str(64)
'''packet sizes are 64, 128, 256, 512, 1024 and 2048 bytes'''

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
#    print(mo_ip.group(1))
#    list_of_host_name.append(host_name)
#    list_of_ip.append(mo_ip.group(1))
    
    pingregex_loss = re.compile(r'(\d+\%) packet loss')
    mo_loss = pingregex_loss.search(copy_string)
#    print(mo_loss.group(1))
#    list_of_packet_loss.append(mo_loss.group(1))
    
    if mo_loss != 100:
        pingregex_stats = re.compile(r'mdev = (\d+\.?\d+)\/(\d+\.?\d+)\/(\d+\.?\d+)\/(\d+\.?\d+)')
        mo_stats = pingregex_stats.search(copy_string)
    #    print(mo_stats.group(1))
    #    list_of_rtt_min.append(mo_stats.group(1))
    #    print(mo_stats.group(2))
    #    list_of_rtt_avg.append(mo_stats.group(2))
    #    print(mo_stats.group(3))
    #    list_of_rtt_max.append(mo_stats.group(3))
    #    print(mo_stats.group(4))
    #    list_of_rtt_mdev.append(mo_stats.group(4))
        
        time_now = datetime.datetime.now()
    #    list_of_time_now.append(time_now.hour)
        
        
        
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
    else:
        time_now = datetime.datetime.now()
    #    list_of_time_now.append(time_now.hour)
        dict_ping_details = {'name':host_name,
                          'IP address':mo_ip.group(1),
                          '% packet loss':mo_loss.group(1),                
                          'rtt min':float('NaN'),
                          'rtt avg':float('NaN'),
                          'rtt max':float('NaN'),
                          'rtt mdev':float('NaN'),
                          'time of day':time_now.hour,
                          'packet_size':packet_size
                          }
    
    
    with open(r'data_host5_packet_variation.csv', 'a', newline='') as csvfile:
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

#import csv
#with open('data_host1.csv',newline='') as f:
#    r = csv.reader(f)
#    data = [line for line in r]
#with open('data_host1.csv','w',newline='') as f:
#    w = csv.writer(f)
#    w.writerow(['name',
#                'IP address',
#                '% packet loss',
#                'rtt avg',
#                'rtt max',
#                'rtt mdev',
#                'time of day'])
#    w.writerows(data)
