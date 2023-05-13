# import tkinter as tk
# from tkinter import messagebox, filedialog
# from utils import create_scrollbar, get_files, filter_files
#
#
# class Application(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         # 窗口配置
#         self.title('everything')
#         self.geometry('600x300')
#         self.iconbitmap('F:/altext/Python project/2303/lulu.ico')
#
#         # 创建控件
#         self.search_frame = SearchFrame(self)
#         self.result_list_box = ResultListBos(self)
#         create_scrollbar(self, self.result_list_box)
#         # 绑定函数
#         self.search_frame \
#             .button_config_search(self.result_list_box)
#         # result_list_box.bind('<Double-Button-1>', click_file)
#
#
# class SearchFrame(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)
#         self.pack(side=tk.TOP)
#         # 关键字的标签和输入
#         tk.Label(self, text="关键字:").pack(side=tk.LEFT, padx=10, pady=10)
#         self.key_entry = tk.Entry(self)
#         self.key_entry.pack(side=tk.LEFT, padx=10, pady=10)
#         # 文件类型的标签和输入
#         tk.Label(self, text="文件类型:").pack(side=tk.LEFT, padx=10, pady=10)
#         self.filetype_entry = tk.Entry(self)
#         self.filetype_entry.pack(side=tk.LEFT, padx=10, pady=10)
#         # 搜索按钮
#         self.search_button = tk.Button(self, text='就上ta')
#         self.search_button.pack(side=tk.LEFT, padx=10, pady=10)
#
#     def button_bind_search(self, result_list_box):
#         self.search_button.config(command=self.search(result_list_box))
#
#     def get_search_data(self):
#         keyword = self.key_entry.get()
#         if not keyword:
#             print("请输入关键字")
#             messagebox.showinfo(message='请输入关键字')
#             return
#         file_type = self.filetype_entry.get()
#         if not file_type:
#             print("请输入文件类型")
#             messagebox.showinfo(message='请输入文件类型')
#             return
#         filepath = filedialog.askdirectory()
#         print(f"关键字:{keyword},文件类型:{file_type},文件路径:{filepath}")
#         # return {
#         #     "keyword": "a",
#         #     "file_type": ".py",
#         #     "filepath": filepath
#         # }
#
#         return {
#             "keyword": keyword,
#             "file_type": file_type,
#             "filepath": filepath
#         }
#
#     def search(self, result_list_box):
#         def func():
#             print('慢慢进去，好嘛！')
#             # 点击按钮获取输入的数据
#             search_data = self.get_search_data()
#             if not search_data:
#                 return
#             files = filter_files(
#                 files=get_files(search_data["filepath"]),
#                 file_type=search_data["file_type"],
#                 keyword=search_data["keyword"]
#             )
#
#             # 文件名填入列表框
#             result_list_box.delete(0, tk.END)
#             result_list_box.insert(tk.END, *files)
#             print("嗖，插进去了！")
#
#         return func
#
#     def button_config_search(self, result_list_box):
#         pass
#
#
# class ResultListBos(tk.Listbox):
#     def __init__(self, master):
#         super().__init__(master)
#         self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#
#     def bind_double_click(self):
#         self.bind('<Double-Button-1>', self.click_file)
#
#     def click_file(self, event):
#         file_path = self.get(self.curselection()[0])
#         ViewWindow().insert_file(file_path)
#
#
# class ViewWindow(tk.Toplevel):
#     def __init__(self):
#         super().__init__()
#         # 窗口配置
#         self.title("查看文件内容")
#         self.geometry("800x600")
#         self.iconbitmap("F:/altext/Python project/2303/R-C.ico")
#         # 创建控件
#         self.file_text = tk.Text(self)
#         self.file_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#         create_scrollbar(self, self.file_text)
#
#     def insert_file(self, file_path):
#         with open(file_path, mode='r', encoding='utf-8-sig') as f:
#             self.file_text.insert(tk.END, f.read())
import tkinter as tk
from tkinter import messagebox, filedialog
from utils import get_files, filter_files, create_scrollbar
from config import *


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        # 窗口配置
        self.title(APP_TITLE)
        self.geometry(APP_SIZE)
        self.iconbitmap(APP_ICON_PATH)

        # 创建控件
        self.search_frame = SearchFrame(self)
        self.result_list_box = ResultListBox(self)
        create_scrollbar(self, self.result_list_box)

        # 绑定函数
        self.search_frame \
            .button_config_search(self.result_list_box)
        self.result_list_box.bind_double_click()


class SearchFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side=tk.TOP)

        # 关键字的标签和输入
        tk.Label(self, text='关键字：').pack(LABEL_PACK)
        self.key_entry = tk.Entry(self)
        self.key_entry.pack(LABEL_PACK)

        # 文件类型的标签和输入
        tk.Label(self, text='文件类型：').pack(LABEL_PACK)
        self.type_entry = tk.Entry(self)
        self.type_entry.pack(LABEL_PACK)

        # 搜索按钮
        self.search_button = tk.Button(self, text='搜索')
        self.search_button.pack(LABEL_PACK)

    def button_config_search(self, result_list_box):
        self.search_button.config(
            command=self.search(result_list_box))

    def get_search_data(self):
        keyword = self.key_entry.get()
        if not keyword:
            print("请输入关键字")
            messagebox.showinfo(message="请输入关键字")
            return
        filetype = self.type_entry.get()
        if not filetype:
            print("请输入文件类型")
            messagebox.showinfo(message="请输入文件类型")
            return
        filepath = filedialog.askdirectory()
        print(f"关键字：{keyword}, 文件类型：{filetype}, 文件路径：{filepath}")
        return {
            "keyword": keyword,
            "filetype": filetype,
            "filepath": filepath
        }

    def search(self, result_list_box):
        def func():
            print("开始搜索文件")
            search_data = self.get_search_data()
            if not search_data:
                return

            files = filter_files(
                files=get_files(search_data["filepath"]),
                filetype=search_data["filetype"],
                keyword=search_data["keyword"]
            )

            # 文件名填入列表框
            result_list_box.delete(0, tk.END)
            result_list_box.insert(tk.END, *files)
            print("文件插入到列表框完成")

        return func


class ViewWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("查看内容")
        self.iconbitmap('F:/altext/Python project/2303/R-C.ico')
        self.file_text = tk.Text(self)
        self.file_text.pack(side=tk.LEFT)
        create_scrollbar(self, self.file_text)

    def insert_file(self, file_path):
        print("读取文件内容，并插入到文本框")
        with open(file_path, 'r', encoding='utf-8 ') as f:
            self.file_text.insert(tk.END, f.read())
        print("插入完毕")


class ResultListBox(tk.Listbox):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def bind_double_click(self):
        self.bind('<Double-Button-1>', self.click_file)

    def click_file(self, event):
        print('点击选择文件')
        # 获取列表框被选中的文件路径
        file_path = self.get(self.curselection()[0])
        print('选择的文件路径为：', file_path)

        # 新的窗口展示文件内容
        ViewWindow().insert_file(file_path)
