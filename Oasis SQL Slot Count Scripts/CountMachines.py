import pandas as pd
import datetime
import os
import csv
import shutil

#load the config file and get working directory
with open('config.json') as config_file:
    config = json.load(config_file)
workdir = config['workdir']
#Get Date and Hour:
currentDt = datetime.datetime.now()
cDate = currentDt.date()
cYear = currentDt.date().year
cMon = currentDt.date().month
cDay = currentDt.date().day
cTime = currentDt.time().hour

#locations of files:
numOverTimeCsvPath = f'{workdir}\\{cYear}\\{cMon}'
dlfilePath = f'{workdir}\\Active Slots Floor Configuration.csv'
numOverTimeCsvFile= os.path.join(numOverTimeCsvPath, f'hourly_machine_count_{cMon}_{cDay}.csv')

#ready dataframe from report:
dFrame = pd.read_csv(dlfilePath)

#prep headers and check if we need to write dirs and a new csv:
headers = ['Count','Date','Time']

if not os.path.exists(numOverTimeCsvPath):
    os.makedirs(numOverTimeCsvPath)    
    print(f"Created {numOverTimeCsvPath}...")
    
else:
    print("Directory Exists, continuing.")

if not os.path.exists(numOverTimeCsvFile):
    with open(numOverTimeCsvFile, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(headers)
    print(f"Created hourly_machine_count_{cMon}_{cDay}.csv...")
else:
    print("CSV exists, appending data.")

machineCount = dFrame.SlotEpromID.count()
#append the machine count to the CSV tagged with the hour:
appendThis = {'Count':[machineCount], 'Date':[cDate], 'Time':[cTime]}
prepDfToAppend = pd.DataFrame(appendThis)
prepDfToAppend.to_csv(numOverTimeCsvFile, mode='a', header=False, index=False)

#yay! now let's move the csv out of the way for the next run:

numOverTimeCsvFileMove = os.path.join(numOverTimeCsvPath, f'machine_Report_{cMon}_{cDay}.csv')
shutil.move(dlfilePath, numOverTimeCsvFileMove)
print(f"CSV moved from {dlfilePath} to {numOverTimeCsvFileMove}")