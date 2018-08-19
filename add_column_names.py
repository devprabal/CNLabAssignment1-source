#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 02:20:06 2018
for CN assignment
@author: devp
"""
import csv

# Change the file name accordingly for other files

with open(r'data_host5_packet_variation.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open(r'data_host5_packet_variation.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['name',
                'IP address',
                '% packet loss',
                'rtt min',
                'rtt avg',
                'rtt max',
                'rtt mdev',
                'time of day',
                'packet_size'])
    w.writerows(data)

