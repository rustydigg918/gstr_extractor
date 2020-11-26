# importing Necessary libraries
import camelot as cm
import pandas as pd
# Some base library
import re,os
from tkinter import filedialog
from tkinter import *

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
columns = ['Transaction Details', 'Transaction status:', "Employer's Code No:",
       "Employer's Name:", 'Challan Period:', 'Challan Number :',
       'Challan Created Date', 'Challan Submitted Date', 'Amount Paid:',
       'Transaction Number:']

df = pd.DataFrame()
for i in tot:
	if i.endswith("pdf"):
		pdf_data = cm.read_pdf(i, flavor='stream', pages='1', edge_tol=500)
		pdf_data_iter = pdf_data[0].df.T
		pdf_data_iter[10] = i

		df = df.append(pdf_data_iter).drop_duplicates(keep='first',subset =[0,1,2,3,4,5,6,7,8,9])
		df.iloc[0,10] = "Filename"
	else:
		pass
df.to_csv("test.csv",header=None,index=False)


"""


# Implementing the Stream flovor to get the names
tot = os.listdir()
df = pd.DataFrame()
for i in tot:
	if i.endswith("pdf"):
		pdf_data = cm.read_pdf(i,flavor='stream', pages='1', edge_tol=500)
		pdf_data_iter = pdf_data[0].df.T
		pdf_data_iter[10] = i

		df = df.append(pdf_data_iter).drop_duplicates(keep='first',subset =[0,1,2,3,4,5,6,7,8,9])
		df.iloc[0,10] = "Filename"
	else:
# Print the message
		print("There isn't any PDF file in the directory provided...Please provide the correct directory path")
df.to_excel(extn+'_ESI_Extracted_data.xlsx', index = False)
print("The ESI data has been extracted!!")
