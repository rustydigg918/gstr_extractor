# importing Necessary libraries
import camelot as cm
import pandas as pd
# Some base library
import re,os

# The savior


#TKINTER START
from tkinter import filedialog
from tkinter import *
root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
# print(folder_selected)
#Setting the path directory
os.chdir(folder_selected)
extn = os.path.split(os.path.split(folder_selected)[0])[1]

"""
tot = os.listdir()
df = pd.DataFrame()
for i in tot:
	if i.endswith("pdf"):
		pdf_data = cm.read_pdf(i, flavor='stream', pages='1', edge_tol=500)
		pdf_data_iter = pdf_data[0].df.T
# 		pdf_data_iter[10] = i

		df = df.append(pdf_data_iter).drop_duplicates(keep='first')
# 		df.iloc[0,10] = "Filename"
	else:
		pass
# df.to_csv("test.csv",header=None,index=False)
"""

# Implementing the Stream flovor to get the names
df = pd.DataFrame()
tot = os.listdir()
for i in tot:
	if i.endswith("pdf"):
		pdf_data = cm.read_pdf(i, flavor='lattice', pages='1')
		pdf_data_iter = pdf_data[0].df.T
		pdf_data_iter[19] = i

# 		pdf_data_iter[10] = i
# 		cols = list(df.columns.values)
		df = df.append(pdf_data_iter).drop_duplicates(keep='first', subset = [0,1])
		df.iloc[0,19] = "Filename"
	else:
		pass

df.to_csv(extn+'_PF_Extracted_data.csv', index = False)
print("The PF data has been extracted!!")
