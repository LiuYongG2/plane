# import tkinter as tk
# import os
#
#
# def create_scrollbar(master, target):
#     sb = tk.Scrollbar(master, command=target.yview)
#     sb.pack(side=tk.RIGHT, fill=tk.Y)
#     target.config(yscrollcommand=sb.set)
#
#
# def get_files(filepath):
#     return [
#         os.path.join(dir_path.replace('/', '\\'), filename)
#         for dir_path, _, filenames in os.walk(filepath)
#         for filename in filenames
#     ]
#     # files = []
#     # # for dir_path, dir_names, filenames in os.walk(filepath):
#     # for dir_path, _, filenames in os.walk(filepath):
#     #     # 路径 目录名 文件名
#     #     for filename in filenames:
#     #         files.append(os.path.join(dir_path.replace('/', '\\'), filename))
#     # return files
#
#
# def filter_files(files, file_type=None, keyword=None):
#     print("秘密加载中...")
#     new_files = []
#     for _file in files:
#         if file_type and not _file.endswith(file_type):
#             continue
#         if keyword:
#             with open(_file, mode='r', encoding='utf-8-sig') as f:
#                 if keyword not in f.read():
#                     continue
#         new_files.append(_file)
#     return new_files
import tkinter as tk
import os


def create_scrollbar(master, target):
    sb = tk.Scrollbar(master, command=target.yview)
    sb.pack(side=tk.RIGHT, fill=tk.Y)
    target.config(yscrollcommand=sb.set)


def get_files(filepath):
    return [
        os.path.join(dir_path.replace('/', '\\'), filename)
        for dir_path, _, filenames in os.walk(filepath)
        for filename in filenames
    ]


def filter_files(files, filetype, keyword):
    print("过滤文件中。。。")
    new_files = []
    for _file in files:
        if not _file.endswith(filetype):
            continue
        try:
            with open(_file, "r", encoding="utf-8-sig") as f:
                if keyword not in f.read():
                    continue
        except Exception as e:
            print(_file, "打开文件失败：", str(e))
            continue
        new_files.append(_file)
    print("符合的文件如下：", new_files)
    return new_files
