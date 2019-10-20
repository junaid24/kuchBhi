from tkinter import *
import os
root = Tk()


label1 = Label( root, text="Enter Info")
E1 = Entry(root, bd =5)

def run1():
    cmd = "python get_dormant_users_info.py 1 " + E1.get()
    os.system(cmd)
	cmd2 = "python Analyze_Build_NF.py"
    os.system(cmd2)
def run2():
    cmd = "python get_dormant_users_info.py 2" + E1.get()
    os.system(cmd)
	cmd2 = "python Analyze_Build_NF.py"
    os.system(cmd2)
def run3():
    cmd = "python get_dormant_users_info.py 3 " + E1.get()
    os.system(cmd)
	cmd2 = "python Analyze_Build_NF.py"
    os.system(cmd2)

submit = Button(root, text="Send every user", bg="black", fg="white", command= run1)


btn2 = Button(root, text="Send to specific user", bg="black", fg="white", command=run2)
# btn2.grid(column=1, row=5)
#
btn3 = Button(root, text="Send to dormant user", bg="black", fg="white", command=run3)
# btn3.grid(column=2, row=5)
label1.pack()
E1.pack()
submit.pack(side =BOTTOM)
btn2.pack(side =BOTTOM)
btn3.pack(side =BOTTOM)
root.mainloop()