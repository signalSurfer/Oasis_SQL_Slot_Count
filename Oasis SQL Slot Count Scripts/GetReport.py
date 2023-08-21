import webbrowser
import datetime
import os
import time
import subprocess
import requests
import json
from requests_ntlm import HttpNtlmAuth

#load a config file with creds
with open('config.json') as config_file:
    config = json.load(config_file)
username = config['username']
password = config['password']
workdir = config['workdir']

#get datetime and extract to separate variables:
currentDt = datetime.datetime.now()
cDate = currentDt.date()
cYear = currentDt.date().year
cMon = currentDt.date().month
cDay = currentDt.date().day
cTime = currentDt.time().hour
countMachines = f'{workdir}\\countMachines.py'

url = f"http://oasisSqlServerIp/ReportServer/Pages/ReportViewer.aspx?%2fBlackBart%2fActive+Slots+Floor+Configuration&rs:Command=Render&AuditDate={cDate}&CasinoCode=-1&rs:Format=CSV"

response = requests.get(url,auth=HttpNtlmAuth(username,password))

if response.status_code == 200:
    # Determine the filename from the URL or headers (if available)
    filename = "Active Slots Floor Configuration.csv"  # Default filename

    content_disposition = response.headers.get('content-disposition')
    if content_disposition:
        filename = content_disposition.split("filename=")[-1].strip('"')

    # Save the content to a file
    with open(filename, 'wb') as csv_file:
        csv_file.write(response.content)

    print(f"CSV file '{filename}' downloaded successfully.")
else:
    print("Download failed with status code:", response.status_code)

#Give the CSV a chance to download:
time.sleep(10)

#optionally start the countmachines script in subprocess, uncomment line:
#subprocess.Popen(['python', countMachines])
