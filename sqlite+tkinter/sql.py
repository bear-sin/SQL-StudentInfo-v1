import tkinter
import tkinter.messagebox
import tkinter.ttk
import sqlite3

# 创建tkinter应用程序
from tkinter import ttk

root = tkinter.Tk()
# 设置窗口标题
root.title("学生信息管理系统V1.0")
# 定义窗口初始大小
root["height"] = 500
root["width"] = 370

# 在窗口上创建标签组件
labelId = tkinter.Label(root, text="编号:", justify=tkinter.RIGHT, width=50)
labelId.place(x=15, y=5, width=50, height=20)

varId = tkinter.StringVar(root, value="")
entryId = tkinter.Entry(root, width=120, textvariable=varId)
entryId.place(x=90, y=5, width=120, height=20)

# 在窗口上创建标签组件
labelName = tkinter.Label(root, text="姓名:", justify=tkinter.RIGHT, width=50)
labelName.place(x=15, y=35, width=50, height=20)

varName = tkinter.StringVar(root, value="")
entryName = tkinter.Entry(root, width=120, textvariable=varName)
entryName.place(x=90, y=35, width=120, height=20)


# 在窗口上创建标签组件
labelSex = tkinter.Label(root, text="性别:", justify=tkinter.RIGHT, width=50)
labelSex.place(x=15, y=70, width=50, height=20)

varSex = tkinter.StringVar(root, value="")
entrySex = tkinter.Entry(root, width=120, textvariable=varSex)
entrySex.place(x=90, y=70, width=120, height=20)

# 在窗口上创建标签组件
labelPython = tkinter.Label(root, text="python成绩:", justify=tkinter.RIGHT, width=50)
labelPython.place(x=10, y=105, width=80, height=20)

varPython = tkinter.StringVar(root, value="")
entryPython = tkinter.Entry(root, width=120, textvariable=varPython)
entryPython.place(x=90, y=105, width=120, height=20)

# 在窗口上创建标签组件
labeldatabase = tkinter.Label(root, text="数据库成绩:", justify=tkinter.RIGHT, width=50)
labeldatabase.place(x=10, y=140, width=80, height=20)

vardatabase = tkinter.StringVar(root, value="")
entrydatabase = tkinter.Entry(root, width=120, textvariable=vardatabase)
entrydatabase.place(x=90, y=140, width=120, height=20)

# 在窗口上创建标签组件
labelClanguage = tkinter.Label(root, text="C语言:", justify=tkinter.RIGHT, width=50)
labelClanguage.place(x=15, y=175, width=50, height=20)

varClanguage = tkinter.StringVar(root, value="")
entryClanguage = tkinter.Entry(root, width=120, textvariable=varClanguage)
entryClanguage.place(x=90, y=175, width=120, height=20)

# 数据库位置
database = "F:/pythonCode/SQL/sqlite+tkinter/test1.db"

# 创建表
conn = sqlite3.connect(database)
print("数据库打开成功")

c = conn.cursor()
listOfTables = c.execute(
    """SELECT name FROM sqlite_master WHERE type='table'
  AND name='student'; """
).fetchall()

if listOfTables == []:
    print("Table not found!")
    c.execute(
        """CREATE TABLE student
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       SEX           TEXT    NOT NULL,
       Python            INT     NOT NULL,
       Database            INT     NOT NULL,
       language            INT     NOT NULL);"""
    )

    print("数据表创建成功")


else:
    print("Table found!")


conn.commit()
conn.close()


# 显示函数
def showAllInfo():
    # 先删除显示列表
    x = dataTreeview.get_children()
    for item in x:
        dataTreeview.delete(item)
    # 连接数据库
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute("select * from student")
    lst = cur.fetchall()
    for item in lst:
        dataTreeview.insert("", 1, text="line1", values=item)
    cur.close()
    con.close()


# 添加函数
def addInfo():
    if (
        entryId.get()
        and entryName.get()
        and entrySex.get()
        and entryPython.get()
        and entrydatabase.get()
        and entryClanguage.get()
    ):
        x = dataTreeview.get_children()
        for item in x:
            dataTreeview.delete(item)
        values = (
            entryId.get(),
            entryName.get(),
            entrySex.get(),
            entryPython.get(),
            entrydatabase.get(),
            entryClanguage.get(),
        )
        con = sqlite3.connect(database)
        cur = con.cursor()
        cur.execute("insert into student values(?,?,?,?,?,?)", values)
        con.commit()
        cur.execute("select * from student")
        lst = cur.fetchall()
        for item in lst:
            dataTreeview.insert("", 1, text="line1", values=item)
        cur.close()
        con.close()
    else:
        tkinter.messagebox.showerror(title="提示", message="输入不能为空")


# 删除函数
def deleteSelection():
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute("select * from student")
    studentList = cur.fetchall()
    cur.close()
    con.close()
    print(studentList)

    id = entryName.get()
    flag = 0
    for i in range(len(studentList)):
        for item in studentList[i]:
            if id == item:
                flag = 1
                con = sqlite3.connect(database)
                cur = con.cursor()
                cur.execute("delete from student where name = ?", (id,))
                con.commit()
                cur.close()
                con.close()
                break
    if flag == 1:
        tkinter.messagebox.showinfo(title="提示", message="删除成功！")
    else:
        tkinter.messagebox.showerror(title="提示", message="删除失败")

    # 删除列表框节点
    x = dataTreeview.get_children()
    for item in x:
        dataTreeview.delete(item)

    # 连接数据库打印显示
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute("select * from student")
    lst = cur.fetchall()
    for item in lst:
        dataTreeview.insert("", 1, text="line1", values=item)
    cur.close()
    con.close()


# 添加组件
tkinter.Button(root, text="添加", width=40, command=addInfo).place(
    x=20, y=210, width=40, height=20
)
tkinter.Button(root, text="删除已选", width=100, command=deleteSelection).place(
    x=80, y=210, width=100, height=20
)
tkinter.Button(root, text="查询", width=40, command=showAllInfo).place(
    x=200, y=210, width=40, height=20
)

# 数据列表显示模块
dataTreeview = ttk.Treeview(
    root,
    show="headings",
    column=("id", "name", "sex", "python_score", "database_score", "c_language_score"),
)
dataTreeview.column("id", width=15, anchor="center")
dataTreeview.column("name", width=20, anchor="center")
dataTreeview.column("sex", width=20, anchor="center")
dataTreeview.column("python_score", width=60, anchor="center")
dataTreeview.column("database_score", width=60, anchor="center")
dataTreeview.column("c_language_score", width=40, anchor="center")

# 头显示
dataTreeview.heading("id", text="编号")
dataTreeview.heading("name", text="姓名")
dataTreeview.heading("sex", text="性别")
dataTreeview.heading("python_score", text="Python成绩")
dataTreeview.heading("database_score", text="数据库成绩")
dataTreeview.heading("c_language_score", text="C成绩")
dataTreeview.place(x=10, y=245, width=350, height=250)

# 创建列表框组件
sb = tkinter.Scrollbar(dataTreeview, command=dataTreeview.yview)
sb.pack(side="right", fill="y")
dataTreeview.config(yscrollcommand=sb.set)
root.mainloop()
