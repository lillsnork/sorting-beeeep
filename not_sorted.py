from tkinter import *
import random

window = Tk()
window_w = 800
window_h = 600
canvas = Canvas(window, width=window_w, height=window_h)
canvas.pack()

no_staples = 100
staple_list = [[window_w/no_staples * i+1,(window_h-10)/no_staples * (i+1)]for i in range(0, no_staples)]
staple_list_cp = staple_list


for item in staple_list:
    y = 600
    x,staple_height = item
    staple_width = window_w/no_staples
    canvas.create_rectangle(x, y, x+staple_width, y-staple_height)
    

window.mainloop()
'''

        
    staple_height = r_staple[1]
    x = item[0]

'''
