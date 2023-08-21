
# GetReport 🥡
- Checks config for directory and credentials
- Generates a parameterized url to autosave a csv of all machines on the gaming floor
- Optionally starts countmachines.py as subprocess after a 10s timer

# CountMachines 🧮
- Loads config for directory
- Gets and splits date and time for Hour
- Checks for year and month directories, creates them if needed
- Uses Pandas to count values in machine name column
- Places count in a new csv with Number, Date, Hour headers
- Moves the machine report and overwrites as an end of day report

# Config.json 🔐
- Three line config file, mostly for creds safety. 
