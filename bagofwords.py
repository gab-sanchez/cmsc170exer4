from Tkinter import *
import time
import copy
import tkFileDialog
import re
window=Tk()
window.title("bag of words")
window.minsize(600,400)

dicsizetxt=IntVar()
totalwordstxt=IntVar()

dictionary={}

def load():
  words=[]
  wordcount=0
  totalwordcount=0

  data=tkFileDialog.askopenfile(parent=window,title='Choose file')
  file=data.read()
  print file
  #for lines in file:
    #for characters in lines:
    #print lines
  wordsinline=file.split(" ")
  for items in wordsinline:
    lowercaseitems=items.lower()
    normalizedwords=re.sub(r'[\W_]+', '', lowercaseitems)#only inludes a-z, A-Z, 0-9
    #for w in normalizedwords:
    words.append(normalizedwords)
  #words.append(wordsinline)
  print words
  dicsizetxt.set(len(words))
  totalwordstxt.set(len(words))      



browsebutton=Button(window,text="Browse",command=load).grid(row=0,column=1)
label1=Label(window,text="Dictionary Size: ").grid(row=1,column=0)
dictionarysize=Label(window,textvariable=dicsizetxt).grid(row=1,column=1)
dicsizetxt.set(0)
label2=Label(window,text="Total Words: ").grid(row=2,column=0)
totalwords=Label(window,textvariable=totalwordstxt).grid(row=2,column=1)
totalwordstxt.set(0)


window.mainloop()