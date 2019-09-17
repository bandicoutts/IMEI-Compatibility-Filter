import csv
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

old_dict = {}
new_dict = {}
filtered_dict = {}

def openOldFile(old_file):

    with open(old_file) as f:
      reader = csv.reader(f)
      for row in reader:
        old_dict[row[0]] = 1

def openNewFile(new_file):

    with open(new_file) as m:
      reader = csv.reader(m)
      for row in reader:
        new_dict[row[0]] = row[1], row[2], row[3]

def openOutputFile(output_file):

    for key,value in new_dict.items():
      if key not in old_dict:
        filtered_dict[key] = value[0], (1 if value[1] == "TRUE" else 0), (1 if value[2] == "TRUE" else 0)


    with open(output_file, 'w') as f:
        f.write("%s,%s,%s,%s\n"%("TacCode","MktModel","DeviceBandW850","DeviceBandW2100"))
        for key, value in filtered_dict.items():
            f.write("%s,%s,%s,%s\n"%(key,value[0], value[1], value[2]))


def createGUI():
    top = tk.Tk()
    top.geometry("500x300") # creates a box of a certain size

    def uploadOldFile(event=None):
        old_file = filedialog.askopenfilename()
        openOldFile(old_file)

    def uploadNewFile(event=None):
        new_file = filedialog.askopenfilename()
        openNewFile(new_file)

    def uploadOutputFile(event=None):
        output_file = filedialog.askopenfilename()
        openOutputFile(output_file)


    oldFileText = tk.Label(top, text="Select the old file by clicking below:", fg="black")
    oldFileText.pack()
    oldButton = tk.Button(top, fg='black', text='Select Old File', command=uploadOldFile)
    oldButton.pack()

    newFileText = tk.Label(top, text="Select the new file by clicking below:", fg="black")
    newFileText.pack()
    newButton = tk.Button(top, fg='black', text='Select New File', command=uploadNewFile)
    newButton.pack()

    outputFileText = tk.Label(top, text="Select the output file by clicking below:", fg="black")
    outputFileText.pack()
    outputButton = tk.Button(top, fg='black', text='Select Output File', command=uploadOutputFile)
    outputButton.pack()

    top.mainloop()



createGUI()