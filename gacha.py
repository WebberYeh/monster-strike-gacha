import tkinter as tk
from tkinter import scrolledtext
import requests
import pandas as pd
from playsound import playsound

root = tk.Tk()
root.title('怪物彈珠轉蛋5星機率')
root.geometry('450x150')
textw = tk.Text(root, width=30, height=10, spacing1=25)
textw.grid(column=0, row=0)
textw.config(font='微軟正黑體 20 bold')


def get_chance(c=0):

    url = "http://monstgacha-yosou.xyz/linemulti/"
    hs = {
        "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36",
    }
    res = requests.get(url, headers=hs)

    tables = pd.read_html(res.text)
    df = tables[0]
    df.columns = ["時間", "機率"]
    txt = "5分鐘內的5星機率為: {}".format(df.loc[2]["機率"])
    textw.delete('1.0', 'end')
    textw.insert('end', txt)
    textw.tag_configure("center", justify='center')
    textw.tag_add("center", 1.0, "end")
    

#####################################################################################################
#                BLOCK 1.  see README.md and change the path of playsound below                     #
#               or  add # to each line in this block if you don't want the sound.                   #
#####################################################################################################
    newc = int(float(df.loc[2]["機率"].split("％")[0]))
    threshold = 15
    if newc != c and newc > threshold:
        for i in range(0, newc-threshold):
            playsound(r'C:\\Users\\gacha\\皮卡.wav')
        playsound(r'C:\\Users\\gacha\\丘.wav')
    c= newc
#####################################################################################################
#                                           BLOCK 1.                                                #
#####################################################################################################    
    root.after(10000, lambda: get_chance(c))
    


button1 = tk.Button(root, text='開始', bg='light grey', width=10, font='微軟正黑體 12 bold', relief='raised', bd=5,
          command=get_chance)
button2 = tk.Button(root, text='結束', bg='light grey', width=10, font='微軟正黑體 12 bold', relief='raised', bd=5,
          command=root.destroy)

button1.place(relx=0.35, rely=0.8, anchor="center")
button2.place(relx=0.65, rely=0.8, anchor="center")


root.mainloop()