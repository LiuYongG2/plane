# import tkinter as tk
#
# root = tk.Tk()
# root.geometry("600x800")
# tk.Label(root, text="用户名").pack(side=tk.LEFT)
# username_enter = tk.Entry(root)
# username_enter.pack(side=tk.LEFT)
# tk.Label(root, text="密码").pack(side=tk.LEFT)
# password_enter = tk.Entry(root)
# password_enter.pack(side=tk.LEFT)
#
#
# def push():
#     print("用户名:", username_enter.get())
#
#
# tk.Button(root, command=push,text="hhhh").pack(side=tk.LEFT)
# root.mainloop()

# import tkinter as tk
#
# root = tk.Tk()
# root.geometry("500x200")
# text = tk.Text(root)
# text.pack()
# text.insert(tk.INSERT, "adsjhahjkdahjkjkdahjk\n")
# text.insert(tk.INSERT, "root = tk.Tk()\n")
# text.insert(tk.END, "ajkldkadjajsakljasdlkasjl\n")
# print(text.get(0.0, 1.6))
# print(text.get(0.0, tk.END))
# text.delete(0.0, tk.END)
# text.window_create(tk.INSERT, window=tk.Button(text, text="wahhhhh"))
#
# root.mainloop()

# import tkinter as tk
#
# root = tk.Tk()
# root.geometry("500x200")
#
# listbox1 = tk.Listbox(root)
# listbox1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#
# # for item in range(20):
# #     listbox1.insert(tk.END, item)
# listbox1.insert(tk.END, *range(10100))
# sb1 = tk.Scrollbar(root, command=listbox1.yview)
# sb1.pack(side=tk.LEFT, fill=tk.Y)
# listbox1.config(yscrollcommand=sb1.set)
# root.mainloop()

# import tkinter as tk
#
# root = tk.Tk()
# root.geometry("280x100")
# name_frame = tk.Frame(root)
# name_frame.pack(anchor=tk.W, padx=10)
# username_lable = tk.Label(name_frame, text="用户名")
# username_lable.pack(side=tk.LEFT)
# username_enter = tk.Entry(name_frame)
# username_enter.pack(side=tk.LEFT)
#
# passwd_frame = tk.Frame(root)
# passwd_frame.pack(anchor=tk.W, padx=10)
# passwd_lable = tk.Label(passwd_frame, text="密   码")
# passwd_lable.pack(side=tk.LEFT)
# password_enter = tk.Entry(passwd_frame, show="*")
# password_enter.pack(side=tk.LEFT)
#
#
# def push():
#     print("用户名:", username_enter.get())
#     top = tk.Toplevel()
#     top.title("啊哈哈哈哈哈哈")
#     top.geometry("1000x1000")
#     tk.Label(top, text="红红火火恍或或或或或或或或或或或或或或或或或或或或", font=("宋体", 30)).pack()
#
#
# tk.Button(root, command=push, text="hhhh").pack(side=tk.RIGHT, padx=10)
# root.mainloop()


# import tkinter as tk
# from tkinter import filedialog, colorchooser, messagebox
#
# root = tk.Tk()
# root.geometry("280x100")
#
#
# def select_file():
#     # print(filedialog.askdirectory())
#     # print(colorchooser.askcolor())
#     print(messagebox.askretrycancel(title="提示信息", message="嗨嗨嗨"))
#     print(messagebox.askokcancel(title="提示信息", message="嗨嗨嗨"))
#     print(messagebox.askquestion(title="提示信息", message="嗨嗨嗨"))
#     print(messagebox.askyesno(title="提示信息", message="嗨嗨嗨"))
#     print(messagebox.showerror(title="提示信息", message="嗨嗨嗨"))
#     print(messagebox.showinfo(title="提示信息", message="嗨嗨嗨"))
#     print(messagebox.showwarning(title="提示信息", message="嗨嗨嗨"))
#
#
# tk.Button(root, text="选择文件夹", command=select_file).pack()
# root.mainloop()


# import tkinter as tk
# from tkinter import filedialog, colorchooser, messagebox
#
# root = tk.Tk()
# root.geometry("400x400")
# label1 = tk.Label(root, text="哇哈哈哈哈")
# label1.pack()
#
#
# def enter_lable(event):
#     label1.config(text="niubi")
#
#
# def leave_lable(event):
#     label1.config(text="gunba")
#
#
# def key_lable(event):
#     label1.config(text=event.keysym)
#
#
# label1.bind('<Enter>', enter_lable)
# label1.bind('<Leave>', leave_lable)
# label1.bind('<Key>', key_lable)
# label1.focus_set()
#
# root.mainloop()

# name_frame = tk.Frame(root)
# # name_frame.pack(anchor=tk.W, padx=10)
# name_frame.pack(side=tk.TOP, padx=10)
# username_lable = tk.Label(name_frame, text="关键字：")
# username_lable.pack(side=tk.LEFT)
# username_enter = tk.Entry(name_frame)
# # username_enter.pack(side=tk.LEFT)
# username_enter.pack()
#
# passwd_frame = tk.Frame(root)
# # passwd_frame.pack(anchor=tk.W, padx=10)
# passwd_frame.pack(side=tk.TOP, padx=10)
# passwd_lable = tk.Label(passwd_frame, text="文件类型：")
# passwd_lable.pack(side=tk.LEFT)
# password_enter = tk.Entry(passwd_frame, show="*")
# # password_enter.pack(side=tk.LEFT)
# password_enter.pack()


# import tkinter as tk
# from tkinter import filedialog, colorchooser, messagebox
# import os
#
#
# def get_files(filepath):
#     return [
#         os.path.join(dir_path.replace('/', '\\'), filename)
#         for dir_path, _, filenames in os.walk(filepath)
#         for filename in filenames
#     ]
#
#
# def search():
#     print("达咩")
#     keyword = keyword_entry.get()
#     if not keyword:
#         messagebox.showinfo(message="请输入关键字")
#         return
#     filetype = filetype_entry.get()
#     if not filetype:
#         messagebox.showinfo(message="请输入文件类型")
#         return
#     filepath = filedialog.askdirectory()
#     result_list_box.delete(0, tk.END)
#     for dir_path, dir_name, filenames in os.walk(filepath):
#         for filename in filenames:
#             _file = os.path.join(dir_path.replace('/', '\\'), filename)
#             if filetype and not _file.endswith(filetype):
#                 continue
#             if keyword:
#                 with open(_file, mode="r", encoding="utf-8-sig") as f:
#                     if keyword not in f.read():
#                         continue
#             result_list_box.insert(tk.END, _file)
#     print("插进去了")
#
#
# root = tk.Tk()
# root.geometry("600x400")
# root.title("select")
# root.iconbitmap("./R-C.bmp")
#
# # 搜索区域容器
# search_frame = tk.Frame(root)
# search_frame.pack(anchor=tk.W, fill=tk.X)
# tk.Label(search_frame, text="关键字：").pack(side=tk.LEFT, padx=10, pady=10, expand=True, )
# keyword_entry = tk.Entry(search_frame)
# keyword_entry.pack(side=tk.LEFT)
#
# tk.Label(search_frame, text="文件类型：").pack(side=tk.LEFT, padx=10, pady=10, expand=True)
# filetype_entry = tk.Entry(search_frame)
# filetype_entry.pack(side=tk.LEFT)
#
# search_button = tk.Button(search_frame, text="哇哈哈哈", command=search)
# search_button.pack(side=tk.LEFT, padx=30, pady=10, expand=True)
#
# result_list_box = tk.Listbox(root)
# result_list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#
# sb1 = tk.Scrollbar(root, command=result_list_box.yview)
# sb1.pack(side=tk.RIGHT, fill=tk.Y)
# result_list_box.config(yscrollcommand=sb1.set)
#
# root.mainloop()

import tkinter as tk
from tkinter import messagebox, filedialog
import os
import re


# def get_search_data():
#     keyword = key_entry.get()
#     if not keyword:
#         messagebox.showinfo(message='请输入关键字')
#         return
#     file_type = filetype_entry.get()
#     if not file_type:
#         messagebox.showinfo(message='请输入文件类型')
#         return
#     return keyword, file_type


def get_search_data():
    # keyword = key_entry.get()
    # if not keyword:
    #     messagebox.showinfo(message='请输入关键字')
    #     return
    # file_type = filetype_entry.get()
    # if not file_type:
    #     messagebox.showinfo(message='请输入文件类型')
    #     return
    filepath = filedialog.askdirectory()
    # print(f"关键字:{keyword},文件类型:{file_type},文件路径:{filepath}")
    return {
        "keyword": "a",
        "file_type": ".py",
        "filepath": filepath
    }

    # return {
    #     "keyword": keyword,
    #     "file_type": file_type,
    #     "filepath": filepath
    # }


def get_files(filepath):
    return [
        os.path.join(dir_path.replace('/', '\\'), filename)
        for dir_path, _, filenames in os.walk(filepath)
        for filename in filenames
    ]
    # files = []
    # # for dir_path, dir_names, filenames in os.walk(filepath):
    # for dir_path, _, filenames in os.walk(filepath):
    #     # 路径 目录名 文件名
    #     for filename in filenames:
    #         files.append(os.path.join(dir_path.replace('/', '\\'), filename))
    # return files


def filter_files(files, file_type=None, keyword=None):
    print("秘密加载中...")
    new_files = []
    for _file in files:
        if file_type and not _file.endswith(file_type):
            continue
        if keyword:
            with open(_file, mode='r', encoding='utf-8-sig') as f:
                if keyword not in f.read():
                    continue
        new_files.append(_file)
    return new_files


# def search():
#     print('点击搜索按钮')
#     # 点击按钮获取输入的数据
#     res = get_search_data()
#     if not res:
#         return
#     keyword, file_type = res
#
#     # 通过文件对话框选择要搜索的路径
#     filepath = filedialog.askdirectory()
#     print('要搜索的路径为：', filepath)
#
#     # 获取文件并过滤
#     files = get_files(filepath)
#     files = filter_files(files, file_type, keyword)
#     # files = filter_files(get_files(filepath), file_type, keyword)
#
#     # 文件名填入列表框
#     result_list_box.delete(0, tk.END)
#     for _file in files:
#         result_list_box.insert(tk.END, _file)
#     print("插进去了")
def search():
    print('慢慢进去，好嘛！')
    # 点击按钮获取输入的数据
    search_data = get_search_data()
    if not search_data:
        return
    files = filter_files(
        files=get_files(search_data["filepath"]),
        file_type=search_data["file_type"],
        keyword=search_data["keyword"]
    )

    # 文件名填入列表框
    result_list_box.delete(0, tk.END)
    result_list_box.insert(tk.END, *files)
    print("嗖，插进去了！")


def create_scrollbar(master, target):
    sb = tk.Scrollbar(master, command=target.yview)
    sb.pack(side=tk.RIGHT, fill=tk.Y)
    target.config(yscrollcommand=sb.set)


def click_file(event):
    print('额，快一点')
    # 获取列表框被选中的文件路径
    file_path = result_list_box.get(result_list_box.curselection()[0])
    print('插入的地方：', file_path)

    # 新的窗口展示文件内容
    top = tk.Toplevel()
    top.title("你要看看嘛？宝贝！")
    top.iconbitmap('./R-C.ico')

    # 文本框
    file_text = tk.Text(top)
    file_text.pack(side=tk.LEFT)
    create_scrollbar(top, file_text)
    keyword = key_entry.get()
    with open(file_path, mode='r', encoding='utf-8-sig') as f:
        for i, line in enumerate(f.readlines()):
            file_text.insert(tk.END, line)
            if keyword not in line:
                continue
            for item in re.finditer(keyword, line):
                file_text.tag_add(
                    "tag",
                    str(i + 1) + '.' + str(item.start()),
                    str(i + 1) + '.' + str(item.end())
                )
            file_text.tag_config("tag", background="orange")

    # 文件内容插入文本框
    with open(file_path, mode='r', encoding='utf-8-sig') as f:
        file_text.insert(tk.END, f.read())


root = tk.Tk()
root.title('everything')
root.geometry('600x300')
root.iconbitmap('./lulu.ico')

search_frame = tk.Frame()
search_frame.pack()

tk.Label(search_frame, text="选那个妞:").pack(side=tk.LEFT, padx=10, pady=10)
key_entry = tk.Entry(search_frame)
key_entry.pack(side=tk.LEFT, padx=10, pady=10)

tk.Label(search_frame, text="妞的类型:").pack(side=tk.LEFT, padx=10, pady=10)
filetype_entry = tk.Entry(search_frame)
filetype_entry.pack(side=tk.LEFT, padx=10, pady=10)

search_button = tk.Button(search_frame, text='就上ta', command=search)
search_button.pack(side=tk.LEFT, padx=10, pady=10)

result_list_box = tk.Listbox(root)
result_list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
sb1 = tk.Scrollbar(root, command=result_list_box.yview)
sb1.pack(side=tk.RIGHT, fill=tk.Y)
result_list_box.config(yscrollcommand=sb1.set)
result_list_box.bind('<Double-Button-1>', click_file)

root.mainloop()
