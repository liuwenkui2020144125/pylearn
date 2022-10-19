import datetime
import time
import tkinter
import threading

app = tkinter.Tk()
app. overrideredirect (True)
app. attributes('-alpha', 0.7)
app. attributes('-topmost', 1)
app. geometry('500x500+700+400')

labelDateTime = tkinter. Label( app, width=130)   #显示日期时间的标签
labelDateTime. pack(fill=tkinter . BOTH, expand=tkinter. YES)
labelDateTime. configure(bg = 'pink')
X = tkinter . IntVar(value=0)     #记录鼠标左键按下的位置
Y = tkinter. IntVar(value=0)

canMove = tkinter . IntVar(value=0)    #窗口是否可拖动
still = tkinter . IntVar(value=1)

labelDateTime = tkinter. Label( app, width=130)   #显示日期时间的标签
labelDateTime. pack(fill=tkinter . BOTH, expand=tkinter. YES)
labelDateTime. configure(bg = 'pink')

def nowDateTime():
    while still.get()==1:
        s = str(datetime.datetime.now())[:19]
        labelDateTime[ 'text'] = s     #显示当前时间
        time . sleep(0.2)

t = threading.Thread(target=nowDateTime)
t. daemon = True
t.start()

app.mainloop()
