__author__ = 'ben'

"""
Config file for nmap_remote.py

Populate this config file to fully leverage the nmap_remote script
"""

import datetime

#pull current date for scan info
scan_time = datetime.date.today()

# Enter your scan target networks here in a list.
scan_targets = ['192.168.20.0/24','172.16.191.0/24']

scan_type = '-sV'

scan_output = '-oA'

scan_output_prefix = 'nmap_remote-%s' % scan_time.isoformat()


# Set up email of results - all output files will be sent as an attachment with a summary of scan
email_report = True

smtp_server = "mail.eiblackops.com"

subject = "Nmap Scan results for %s" % scan_time.isoformat()
message = "The nmap scan for %s completed and the results are attached." % scan_time.isoformat()

# Check in nmap results to code repo of your choice - nmap_remote uses git
checkin_scan_data = True

checkin_url = 'https://code.eiblackops.com/network_inventory.git'
checkin_user = "ben"
checkin_pass = "password"

# Operating system customizing

nmap_path = "/usr/local/bin/nmap"

working_dir = "./"

# Database options

database_type = "sqlite"