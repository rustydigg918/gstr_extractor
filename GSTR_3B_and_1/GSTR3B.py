# importing Necessary libraries
import camelot as cm
import pandas as pd
# Some base library
import re,os


#TKINTER START
from tkinter import filedialog
from tkinter import *
root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
# print(folder_selected)



#Setting the path directory
os.chdir(folder_selected)

# Implementing the Stream flovor to get the names
tot = os.listdir()
# Implementing the Stream flovor to get the names
# tot = os.listdir()
file_name = os.getcwd().split('\\')[-1]

Sheet1 = "outward & reverse_charge"
Sheet2 = "Inter-state supplies"
Sheet3 = "Eligible ITC"
Sheet4 = "Exempt, nil and Non GST"
Sheet5 = "Interest and Late fee"
Sheet6 = "Payment of tax"
Sheet7 = "TDS TCS Credit"

df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()
df5 = pd.DataFrame()
df6 = pd.DataFrame()
df7 = pd.DataFrame()

for i in tot:
    if i.endswith(".pdf"):
        tables = cm.read_pdf(i, flavor='stream',  table_areas = ['490,510,670,450', '5,450,760,400'])
        tabs = cm.read_pdf(i,pages='1,2,3',strip_text='\n', flag_size=True)
        y = tables[0].df
        z = tables[1].df
        z.loc[0,0] = z.loc[0,0].split('.')[1]
        z.loc[1,0] = z.loc[1,0].split('.')[1]
#         z_t = z.T
#         y_t = y.T

        if tabs[0].df.loc[0,0] == "Nature of Supplies":
        
            post = pd.concat([z.T,y.T] , ignore_index=True,axis =1)

            fn = (str(z.at[1,1])+"_"+str(y.at[0,1])+"_"+str(y.at[1,1])+"_"+str(z.at[0,1]))


        # Lattice starts from here
#             tabs = cm.read_pdf(i,pages='1,2,3',strip_text='\n', flag_size=True)

            df_ft = pd.concat([tabs[0].df,post], ignore_index=True,axis =1)
            df1 = pd.concat([df1, df_ft], ignore_index=True,axis =0)

            df_sd = pd.concat([tabs[1].df,post], ignore_index=True,axis =1)
            df2 = pd.concat([df2, df_sd], ignore_index=True,axis =0)

            df_td = pd.concat([tabs[2].df,post], ignore_index=True,axis =1)
            df3 = pd.concat([df3, df_td], ignore_index=True,axis =0)

            df_fh = pd.concat([tabs[3].df,post], ignore_index=True,axis =1)
            df4 = pd.concat([df4, df_fh], ignore_index=True,axis =0)

            df_fif = pd.concat([tabs[4].df,post], ignore_index=True,axis =1)
            df5 = pd.concat([df5, df_fif], ignore_index=True,axis =0)

            df_sh = pd.concat([tabs[5].df,post], ignore_index=True,axis =1)
            df6 = pd.concat([df6, df_sh], ignore_index=True,axis =0)

            df_sev = pd.concat([tabs[6].df,post], ignore_index=True,axis =1)
            df7 = pd.concat([df7, df_sev], ignore_index=True,axis =0)
            # The other type of file to be handled
        else:
            
            post = pd.concat([tabs[0].df.T,y.T] , ignore_index=True,axis =1)
            
            df_ft = pd.concat([tabs[1].df,post], ignore_index=True,axis =1)
            df1 = pd.concat([df1, df_ft], ignore_index=True,axis =0)

            df_sd = pd.concat([tabs[2].df,post], ignore_index=True,axis =1)
            df2 = pd.concat([df2, df_sd], ignore_index=True,axis =0)

            df_td = pd.concat([tabs[3].df,post], ignore_index=True,axis =1)
            df3 = pd.concat([df3, df_td], ignore_index=True,axis =0)

            df_fh = pd.concat([tabs[4].df,post], ignore_index=True,axis =1)
            df4 = pd.concat([df4, df_fh], ignore_index=True,axis =0)

            df_fif = pd.concat([tabs[5].df,post], ignore_index=True,axis =1)
            df5 = pd.concat([df5, df_fif], ignore_index=True,axis =0)

            df_sh = pd.concat([tabs[6].df,post], ignore_index=True,axis =1)
            df6 = pd.concat([df6, df_sh], ignore_index=True,axis =0)

            df_sev = pd.concat([tabs[7].df,post], ignore_index=True,axis =1)
            df7 = pd.concat([df7, df_sev], ignore_index=True,axis =0)
    

writer = pd.ExcelWriter(f'{file_name}.xlsx'.format(fn), engine='xlsxwriter')

# Write each dataframe to a different worksheet.
df1.to_excel(writer, sheet_name=Sheet1)
df2.to_excel(writer, sheet_name=Sheet2)
df3.to_excel(writer, sheet_name=Sheet3)
df4.to_excel(writer, sheet_name=Sheet4)
df5.to_excel(writer, sheet_name=Sheet5)
df6.to_excel(writer, sheet_name=Sheet6)
df7.to_excel(writer, sheet_name=Sheet7)

# Close the Pandas Excel writer and output the Excel file.
writer.save()


# print("Index Error occured with these following files"+ str([x for x in excp]))
