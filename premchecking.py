from base import *
import config

debug = True
headers = {
        "Name": ["Name", "Insured Name", ],
        "DOB": ["DOB", "Date of Birth", ],
        "Gender": ["Gender", "Sex"]
    }
def checkHeader(df):
    col_names = df.columns.values
    result_df = pd.DataFrame()

    for header in headers:
        if set(col_names).intersection(headers[header]):
            for col in col_names:
                if col in headers[header]:
                    result_df[header] = df[col]
                    break
        else:
            if debug: print("checkHeader failed: " + header)
            return False
    return result_df



loc = input("Please input the file location. \n")

filetype = loc[-3:]
if filetype == 'csv':
    raw_df = pd.read_csv(loc)
    df = checkHeader(raw_df)
    print(df)
    # transform_dat/Users/JasonWan/Desktop/premiume(df)
    # df["c_date"] = df['eff_date'] - df['dob']

else:
    print("Please input a valid file type (csv, xls, xlsx)")

# if filety
#
# writer = pd.ExcelWriter(config.PREMCHECK_REPORT_DIR + "output.xlsx")
# df.to_excel(writer, "sheet1")
