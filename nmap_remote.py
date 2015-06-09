__author__ = 'ben'

"""
Nmap_remote is a python script to automate the execution and delivery of your nmap scans.

This tool is written by Ben Finke (@benfinke) and is designed for use by the thousands
of network defenders who are charged with defending networks without enough tools, time,
or assistance.

Set up this script in the config file (config.py) and execute as a cron job or scheduled task.

Available at GitHub:

June 2015 - Ben Finke - @benfinke - ben@benfinke.com
"""

import nmap
import config


scanner = nmap.PortScanner()

