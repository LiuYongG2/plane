import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
import os


def create_scrollbar(master, target):
    sb = tk.Scrollbar(master, command=result_list_box.yview)
    sb.pack(side=tk.RIGHT, fill=tk.Y)
    result_list_box.config(yscrollcommand=sb.set)


root = tk.Tk()
root.title('everything')
root.geometry('600x300')
root.iconbitmap('./lulu.ico')

search_frame = tk.Frame()
search_frame.pack()

tk.Label(search_frame, text="关键字:").pack(side=tk.LEFT, padx=10, pady=10)
key_entry = tk.Entry(search_frame)
key_entry.pack(side=tk.LEFT, padx=10, pady=10)

tk.Label(search_frame, text="文件类型:").pack(side=tk.LEFT, padx=10, pady=10)
type_entry = tk.Entry(search_frame)
type_entry.pack(side=tk.LEFT, padx=10, pady=10)

search_button = tk.Button(search_frame, text='搜索')
search_button.pack(side=tk.LEFT, padx=10, pady=10)

result_list_box = tk.Listbox(root)
result_list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

create_scrollbar(root, result_list_box)


def click_file(event):
    print('ahahah')
    file_path = result_list_box.get(result_list_box.curselection()[0])
    print('文件路径为：', file_path)
    top = tk.Toplevel()
    top.title("filelooking")
    top.geometry("800x600")
    top.iconbitmap("./R-C.ico")

    file_text = tk.Text(top)
    file_text.pack(side=tk.LEFT)
    create_scrollbar(top, file_text)
    with open(file_path, mode="r", encoding="utf-8-sig") as f:
        file_text.insert(tk.END, f.read())


result_list_box.bind('<Double-Button-1>', click_file)


def search():
    print("点击搜索按钮")
    keyword = key_entry.get()
    if not keyword:
        messagebox.showinfo(message="请输入关键字")
        return
    file_type = type_entry.get()
    if not file_type:
        messagebox.showinfo(message="请输入文件类型")
        return
    filepath = filedialog.askdirectory()
    print("要搜索的路径为：{}，关键字：{}，文件类型：{}".format(filepath, keyword, filepath))
    result_list_box.delete(0, tk.END)
    for dir_path, dir_name, filenames in os.walk(filepath):
        for filename in filenames:
            _file = os.path.join(dir_path.replace('/', '\\'), filename)
            if file_type and not _file.endswith(file_type):
                continue
            if keyword:
                with open(_file, mode='r', encoding='utf-8-sig') as f:
                    if keyword not in f.read():
                        continue
                result_list_box.insert(tk.END, _file)
            print("!!!!")


search_button.config(command=search)

root.mainloop()
