# import psutil
#
# print(psutil.cpu_count())  # 逻辑CPU个数
# print(psutil.cpu_count(logical=False))  # 物理CPU个数
# print(psutil.cpu_percent(interval=1))  # CPU利用率
# print(psutil.pids())
# # print(psutil.Process(39304).name())
# print(psutil.virtual_memory())
# print(psutil.disk_usage('C:/'))
# print(psutil.disk_io_counters())
# print(psutil.net_io_counters())
# print(psutil.net_io_counters(pernic=True))
# import json
#
# res = psutil.net_io_counters(pernic=True)
# print(json.dumps(res))
# print(json.dumps(res, ensure_ascii=False))
# print(json.dumps(res, ensure_ascii=False, indent=2))


# import psutil
# import time
# while True:
#     s1 = psutil.net_io_counters().bytes_recv
#     time.sleep(1)
#     s2 = psutil.net_io_counters().bytes_recv
#     print(f'{(s2 - s1) / 1024:.2f}Kb/s')
#     # if input() == 'q':
#     #     break


# import time
# import tkinter as tk
#
# # button1 = tk.Button(root, text="嗨嗨嗨", command=change_label1())
#
#
# root = tk.Tk()
# root.geometry("300x200")
# root.title("嘎嘎牛逼")
# root.iconbitmap("speed3.ico")
# label_text = tk.StringVar(value="嗨嗨嗨啊哈我阿hi阿hiHIA")
# lable = tk.Label(root, text="speed", font=("Arial", 20, "bold"), bg="green", fg="red", padx=10, pady=10)
# lable.pack()
# lable.config(textvariable=label_text)
#
#
# def change_label1():
#     label_text.set(time.strftime("%H:%M:%S"))
#     root.after(1000, change_label1)
#
#
# # button1 = tk.Button(root, text="别动", font=("Arial", 20, "bold"), bg="yellow", fg="pink", command=change_label1())
# button1 = tk.Button(root, text="别动", font=("Arial", 20, "bold"), command=change_label1())
# button1.pack()
# root.mainloop()


# import time
# import tkinter as tk
#
# root = tk.Tk()
# root.geometry("300x200")
# root.title("嘎嘎牛逼")
# root.iconbitmap("speed3.ico")
# tk.Label(root, text="标签1", font=("Arial", 20, "bold"), bg="blue").pack(anchor=tk.W, fill=tk.BOTH, expand=True)
# tk.Label(root, text="标签2", font=("Arial", 20, "bold"), bg="red").pack(anchor=tk.W)
# tk.Label(root, text="标签3", font=("Arial", 20, "bold"), bg="green").pack(anchor=tk.W)
#
# root.mainloop()


# import tkinter as tk
# import time
# import psutil
#
#
# def change_label1(pre_data):
#     cur_data = psutil.net_io_counters().bytes_recv
#     var.set(f'{(cur_data - pre_data) / 1024:.1f}kb/s')
#     root.after(1000, change_label1, cur_data)
#
#
# root = tk.Tk()
# root.geometry("300x100")
#
# var = tk.StringVar(value=time.strftime("%H:%M:%S"))
# label1 = tk.Label(root, textvariable=var, font=('Arial', 50, 'bold'))  # 标签
# label1.pack()  # 布局
#
# change_label1(psutil.net_io_counters().bytes_recv)
# root.mainloop()


import psutil
import tkinter as tk

root = tk.Tk()
root.geometry("300x150")
root.iconbitmap("./speed.ico")
root.title("网速监测工具")
root.config(background="#008c8c")
tk.Label(root,
         text='网络速度',
         background="#008c8c",
         font=('宋体', 25, 'bold'),
         fg="#4198b9"
         ).pack(pady=15)

speed_var = tk.StringVar(value="")
tk.Label(root,
         textvariable=speed_var,
         background="#ffffff",
         font=('Arial', 20, 'bold'),
         fg="#6bb3c0"
         ).pack()


def speed_test(pre_data):
    cur_data = psutil.net_io_counters().bytes_recv
    data = (cur_data - pre_data) / 1024
    speed_var.set(f'{data:.1f}K/s' if data < 900 else f'{data / 1024:.1f}M/s')
    root.after(1000, speed_test, cur_data)


speed_test(psutil.net_io_counters().bytes_recv)
root.mainloop()
