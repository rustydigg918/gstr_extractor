# importing Necessary libraries
import camelot as cm
import pandas as pd
import os
# Some base library
#West_Bengal_Electronic_Cash_Ledger.pdf
path = r"C:\Users\pushkar\Downloads\Bharat(varasity)\GST Cash & Credit Ledgers\Cash & Credit Ledgers"
os.chdir(path)
retv = os.getcwd()
print(retv)
# t = cm.read_pdf('Andhra_Pradesh_Electronic_Cash_Ledger.pdf', pages = '1-end', flavor='stream')
# t[0].df
# cm.plot(t[0], kind='textedge').show()
