#
#  calculate.py
#  Calculate By JIN
#
#  Created by THANAKORN CHAREONLERTKAMOL (JIN) on 18/2/2564 BE.
#

import tkinter as tk
window = tk.Tk()
window.title('Calculate By JIN')
def clear():
   global expression
   global label_show
   result='0'
   expression=''
   label_show.set(result)

def press(number):
   global expression
   global label_show
   expression=expression+number
   label_show.set(expression)

def equal():
   try:
       global expression
       global label_show
       result=str(eval(expression))
       label_show.set(result)
   except:
       result='ERROR'
       expression=''
   label_show.set(result)
   
label_show=tk.StringVar()
expression=''
label_show.set(expression)
label_show.set(0)

label=tk.Label(window,textvariable=label_show).grid(row=0,column=0,columnspan=4,sticky='news')

button=tk.Button(window,text='CLEAR',command=clear).grid(row=1,column=0,columnspan=2)

button=tk.Button(window,text='7',command=lambda :press('7')).grid(row=2,column=0,sticky='news')
button=tk.Button(window,text='8',command=lambda :press('8')).grid(row=2,column=1,sticky='news')
button=tk.Button(window,text='9',command=lambda :press('9')).grid(row=2,column=2,sticky='news')
button=tk.Button(window,text='+',command=lambda :press('+')).grid(row=2,column=3,sticky='news')

button=tk.Button(window,text='4',command=lambda :press('4')).grid(row=3,column=0,sticky='news')
button=tk.Button(window,text='5',command=lambda :press('5')).grid(row=3,column=1,sticky='news')
button=tk.Button(window,text='6',command=lambda :press('6')).grid(row=3,column=2,sticky='news')
button=tk.Button(window,text='-',command=lambda :press('-')).grid(row=3,column=3,sticky='news')

button=tk.Button(window,text='1',command=lambda :press('1')).grid(row=4,column=0,sticky='news')
button=tk.Button(window,text='2',command=lambda :press('2')).grid(row=4,column=1,sticky='news')
button=tk.Button(window,text='3',command=lambda :press('3')).grid(row=4,column=2,sticky='news')
button=tk.Button(window,text='*',command=lambda :press('*')).grid(row=4,column=3,sticky='news')

button=tk.Button(window,text='.',command=lambda :press('.')).grid(row=10,column=0,sticky='news')
button=tk.Button(window,text='0',command=lambda :press('0')).grid(row=10,column=1,sticky='news')
button=tk.Button(window,text='00',command=lambda :press('00')).grid(row=10,column=2,sticky='news')
button=tk.Button(window,text='/',command=lambda :press('/')).grid(row=10,column=3,sticky='news')

button=tk.Button(window,text='=',command=equal).grid(row=6,column=0,columnspan=4,sticky='news')
window.mainloop()