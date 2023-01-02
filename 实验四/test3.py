from tkinter import *
import threading
import time
from multiprocessing import Process
import os
from aip import AipSpeech
import inspect
import ctypes
import speech_recognition as sr
class type:
    def __init__(self,value):
        self.value=value
def gif(n):
    root = Tk()
    numIdx =15# if的帧数
    # 填充6帧内容到frames
    frames = [PhotoImage(file='fan.gif', format='gif -index %i' %(i)) for i in range(numIdx)]
    def update(idx):  # 定时器函数
        frame = frames[idx]
        if n.value==1:
            idx += 1  # 下一帧的序号：在0,1,2,3,4,5之间循环(共6帧)
        label.configure(image=frame)  # 显示当前帧的图片
        if n.value==2:
            root.after(10,root.destroy())
        root.after(100, update, idx % numIdx)  # 0.1秒(100毫秒)之后继续执行定时器函数(update)
    label = Label(root)
    label.pack()
    root.after(0, update, 0) # 立即启动定时器函数(update)
    root.mainloop()
def fun(n):
    APP_ID = '29384293'
    API_KEY = 'sAP14UGPBUOS11Hyquz4PYQt'
    SECRET_KEY = '0wgnSpVqYOfeQNbGGSSXdrOLCEqZIruD'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=16000) as source:
        while True:
            audio = r.listen(source).get_wav_data()
            response = client.asr(audio, 'wav', 16000, {'dev_pid': 1537, })
            print(response)
            if response['result'][0] in ['关机', "关机。"]:
                n.value=2
                break
            elif response['result'][0] in ['开风扇', "开风扇。"]:
                n.value=1
            elif response['result'][0] in ['关风扇', "关风扇。"]:
                n.value=0
if __name__ == '__main__':
    APP_ID = '29384293'
    API_KEY = 'sAP14UGPBUOS11Hyquz4PYQt'
    SECRET_KEY = ''
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    r = sr.Recognizer()
    while True:
        with sr.Microphone(sample_rate=16000) as source:
            print("请说话")
            audio = r.listen(source).get_wav_data()
            response = client.asr(audio, 'wav', 16000, {'dev_pid': 1537, })
            print(response)
            if response['result'][0] in ['开机',"开机。"]:
                print("开始生成风扇")
                break
    select = type(0)
    t1 = threading.Thread(target=fun, args=(select,))
    t1.start()
    gif(select)

