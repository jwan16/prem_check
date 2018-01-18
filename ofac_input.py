import base
import pandas as pd
import re
import datetime
import config
count = 0
print(datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d %H:%m"))
# Folders input
folders = []

# Initial
claims_df = pd.DataFrame(columns=config.CLAIMS_HEADERS)
ofac_df = pd.DataFrame(columns=config.OFAC_HEADERS)
premiums_df = pd.DataFrame(columns=config.OFAC_HEADERS)

while True:
    # Initialize input
    dir = ""
    rec_date = ""

    # Ask for directory
    dir = input("Input the folder {0} directory: ".format(count+1))
    if dir == "ok":
        break
    # if not re.match("^J:",dir):
    #     print("Invalid directory. Please input again!")
    #     continue
    while not re.match("^(20|19)\d{6}", rec_date):
        rec_date = input("Input the folder {0} received date (YYYYMMDD): ".format(count+1))
    print('Folder {0} is stored (Type "ok" to complete folder input)'.format(count+1))
    folders.append({"dir": dir, "rec_date": rec_date})
    count += 1

# Scan all folder
df_list = []
for folder in folders:
    files = base.scan_folder(folder['dir'])

    for csv in files['csv']:
        df = pd.read_csv(csv)



def define_df(df):
    set = set(df.columns.values)
    if set.intersection(config.CLAIMS):
        return 'claim'
    else if
