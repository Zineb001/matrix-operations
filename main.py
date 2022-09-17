import tkinter as tk
import random
from builtins import print

import config
from matrix_operation import MatrixOperation

COLUMN_WITH = 6
global win_button


def generate_err_matrix(nrows, ncols):
    ans = []
    if config.operation == "i":
        for i in range(nrows):  # Rows
            l = []
            for j in range(ncols):  # Columns
                l.append(round(random.uniform(0, 100), 3))
            ans.append(l)
        return ans
    if config.operation == "v":
        for i in range(nrows):  # Rows
            l = []
            for j in range(ncols):  # Columns
                l.append(round(random.uniform(0, 100), 3))
            ans.append(l)
        return ans
    if config.operation == "e":
        for i in range(nrows):  # Rows
            l = []
            for j in range(ncols):  # Columns
                l.append(round(random.uniform(0, 100), 3))
            ans.append(l)
        return ans
    if config.operation == "s":
        for i in range(nrows):  # Rows
            l = []
            for j in range(ncols):  # Columns
                l.append(round(random.uniform(0, 100), 3))
            ans.append(l)
        return ans
    else:
        for i in range(nrows):  # Rows
            l = []
            for j in range(ncols):  # Columns
                l.append(random.randint(0, 100))
            ans.append(l)
        return ans


def generate_for_edit(nrows, ncols):
    ans = []
    for i in range(nrows):  # Rows
        l = []
        for j in range(ncols):  # Columns
            l.append(1)
        ans.append(l)
    return ans


def print_matix(x, y, matrix_data, matrix_title, matrix_name, matrix_type):
    if matrix_type == "IN":
        tk.Label(root, text=matrix_title, width=COLUMN_WITH).grid(row=y, column=x)
    if matrix_type == "OUT":
        tk.Button(root, text=matrix_title, width=COLUMN_WITH, command=lambda m=matrix_title: onChoice(m)).grid(row=y,
                                                                                                              column=x)
    nrows = len(matrix_data)
    ncols = len(matrix_data[0])
    for i in range(nrows):  # Rows
        for j in range(ncols):  # Columns
            if config.mode == "w":
                wn = matrix_name + str(i) + str(j)
                b = tk.Text(root, height=1, width=COLUMN_WITH, relief="groove", name=wn)
                b.insert(1.0, matrix_data[i][j])
            else:
                b = tk.Label(root, text=matrix_data[i][j], width=COLUMN_WITH, relief="groove")
            b.grid(row=i + y + 1, column=j + x)


def insert_label(x, y, label_text):
    b = tk.Label(root, text=label_text, width=COLUMN_WITH)
    b.grid(row=y, column=x)


def insert_text(x, y):
    b = tk.Text(root, height=1, width=COLUMN_WITH)
    b.grid(row=y, column=x)
    return b


def publish(oper_type, a, b, r1, r2, r3, r4):
    init_root()
    print_matix(0, 0, a, "Matrix A", "a", "IN")
    nrows = len(a)
    ncols = len(a[0])
    if len(b) > 0:
        insert_label(ncols + 1, round((nrows + 1) / 2), oper_type)
        print_matix(ncols + 2, 0, b, "Matrix B", "b", "IN")
    insert_label(0, nrows + 1, "")
    if len(r1) > 0:
        button_name = "Choice 1"
        if config.mode == "w":
            button_name = "Check"
        print_matix(0, nrows + 2, r1, button_name, "r1", "OUT")
    if len(r2) > 0:
        print_matix(ncols + 2, nrows + 2, r2, "Choice 2", "r2", "OUT")
    if len(r3) > 0:
        print_matix(0, 2 * nrows + 3, r3, "Choice 3", "r3", "OUT")
    if len(r4) > 0:
        print_matix(ncols + 2, 2 * nrows + 3, r4, "Choice 4", "r4", "OUT")


def is_win():
    a = []
    b = []
    for i in range(int(config.dim_rows)):
        row = []
        for j in range(int(config.dim_cols)):
            wn = "a"+str(i)+str(j)
            v = root.children[wn].get("1.0", 'end-1c')
            row.append(int(v))
        a.append(row)
    if config.operation == "*":
        for i in range(int(config.dim_cols)):
            row = []
            for j in range(int(config.dim_rows)):
                wn = "b" + str(i) + str(j)
                v = root.children[wn].get("1.0", 'end-1c')
                row.append(int(v))
            b.append(row)
    if config.operation == "+":
        for i in range(int(config.dim_rows)):
            row = []
            for j in range(int(config.dim_cols)):
                wn = "b" + str(i) + str(j)
                v = root.children[wn].get("1.0", 'end-1c')
                row.append(int(v))
            b.append(row)
    if config.operation == "s":
        for i in range(int(config.dim_rows)):
            row = []
            wn = "b" + str(i)+"0"
            v = root.children[wn].get("1.0", 'end-1c')
            row.append(int(v))
            b.append(row)
    mo = MatrixOperation(int(config.dim_rows), int(config.dim_cols), config.operation)
    mo.a = a
    mo.b = b
    if config.operation == "*":
        mo.multiplication()
    if config.operation == "+":
        mo.addition()
    if config.operation == "d":
        mo.determinant()
    if config.operation == "s":
        mo.solve()
    if config.operation == "i":
        mo.inverse()
    if config.operation == "e":
        mo.eigenValues()
    if config.operation == "v":
        mo.eigenVectors()
    print(mo.result)
    r_rows = len(mo.result)
    r_cols = len(mo.result[0])
    for i in range(r_rows):
        row = []
        for j in range(r_cols):
            wn = "r1"+str(i)+str(j)
            v = root.children[wn].get("1.0", 'end-1c')
            if float(v) != float(mo.result[i][j]):
                print(float(v), "==", mo.result[i][j])
                return False
    return True


def onChoice(button_name):
    if config.mode == "w":
        if is_win():
            setMessage(False)
        else:
            setMessage(True)
    else:
        print(button_name,"==",win_button)
        if button_name == win_button:
            setMessage(False)
        else:
            setMessage(True)


def setMessage(err):
    x = 2 * 6
    y = 3 * 12
    if err:
        tk.Label(root, text="ERROR", width=10, fg="red", font='Helvetica 18 bold').grid(row=y, column=x)
    else:
        tk.Label(root, text="SUCCESS", width=10, fg="green", font='Helvetica 18 bold').grid(row=y, column=x)
    tk.Button(root, text="NEXT", width=10, font='Helvetica 18 bold', command=set_next).grid(row=y + 1, column=x)


def set_next():
    init_root()
    if config.mode == "w":
        onManuelOperation(config.operation)
    else:
        onAutoOperation(config.operation)


def setConfig(r, c, m):
    config.dim_rows = r
    config.dim_cols = c
    config.mode = m
    init_root()


def onAutoOperation(type_oper):
    init_root()
    if config.dim_rows == "":
        return
    if config.dim_cols == "":
        return
    mo = MatrixOperation(int(config.dim_rows), int(config.dim_cols), type_oper)
    mo.generate_values(True)
    if type_oper == "*":
        mo.multiplication()
    if type_oper == "+":
        mo.addition()
    if type_oper == "d":
        mo.determinant()
    if type_oper == "s":
        mo.solve()
    if type_oper == "i":
        mo.inverse()
    if type_oper == "e":
        mo.eigenValues()
    if type_oper == "v":
        mo.eigenVectors()
    nrows = len(mo.result)
    ncols = len(mo.result[0])
    print(mo.result)
    rn = random.randint(1, 4)
    print(rn)
    global win_button
    win_button = "Choice " + str(rn)
    r1 = generate_err_matrix(nrows, ncols)
    r2 = generate_err_matrix(nrows, ncols)
    r3 = generate_err_matrix(nrows, ncols)
    r4 = generate_err_matrix(nrows, ncols)
    if rn == 1:
        r1 = mo.result
    if rn == 2:
        r2 = mo.result
    if rn == 3:
        r3 = mo.result
    if rn == 4:
        r4 = mo.result
    publish(type_oper, mo.a, mo.b, r1, r2, r3, r4)


def onManuelOperation(type_oper):
    init_root()
    if config.dim_rows == "":
        return
    if config.dim_cols == "":
        return
    mo = MatrixOperation(int(config.dim_rows), int(config.dim_cols), type_oper)
    mo.generate_values(True)
    if type_oper == "*":
        mo.multiplication()
    if type_oper == "+":
        mo.addition()
    if type_oper == "d":
        mo.determinant()
    if type_oper == "s":
        mo.solve()
    if type_oper == "i":
        mo.inverse()
    if type_oper == "e":
        mo.eigenValues()
    if type_oper == "v":
        mo.eigenVectors()
    nrows = len(mo.result)
    ncols = len(mo.result[0])
    global win_button
    win_button = ""
    r1 = generate_for_edit(nrows, ncols)
    r2 = []
    r3 = []
    r4 = []
    publish(type_oper, mo.a, mo.b, r1, r2, r3, r4)


def initConfig():
    init_root()
    insert_label(0, 0, "N Rows")
    r = insert_text(2, 0)
    r.insert(1.0, config.dim_rows)
    insert_label(0, 1, "N Cols")
    c = insert_text(2, 1)
    c.insert(1.0, config.dim_cols)
    insert_label(0, 2, "Mode")
    m = insert_text(2, 2)
    m.insert(1.0, config.mode)
    tk.Button(root, text="set", width=COLUMN_WITH,
              command=lambda: setConfig(r.get("1.0", 'end-1c'), c.get("1.0", 'end-1c'), m.get("1.0", 'end-1c'))).grid(
        row=4, column=0)


def onMultiplication():
    config.operation = "*"
    if config.mode == "w":
        onManuelOperation("*")
    else:
        onAutoOperation("*")


def onAddition():
    config.operation = "+"
    if config.mode == "w":
        onManuelOperation("+")
    else:
        onAutoOperation("+")


def onDeterminant():
    config.operation = "d"
    if config.mode == "w":
        onManuelOperation("d")
    else:
        onAutoOperation("d")


def onSolve():
    config.operation = "s"
    if config.mode == "w":
        onManuelOperation("s")
    else:
        onAutoOperation("s")


def onInverse():
    config.operation = "i"
    if config.mode == "w":
        onManuelOperation("i")
    else:
        onAutoOperation("i")


def onEigenValues():
    config.operation = "e"
    if config.mode == "w":
        onManuelOperation("e")
    else:
        onAutoOperation("e")


def onEigenVectors():
    config.operation = "v"
    if config.mode == "w":
        onManuelOperation("v")
    else:
        onAutoOperation("v")


def init_root():
    for widget in root.winfo_children():
        widget.destroy()

    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar)
    filemenu.add_command(label="Change dimensions", command=initConfig)
    filemenu.add_command(label="Multiplication", command=onMultiplication)
    filemenu.add_command(label="Addition", command=onAddition)
    filemenu.add_command(label="Determinant", command=onDeterminant)
    filemenu.add_command(label="Solve", command=onSolve)
    filemenu.add_command(label="Inverse", command=onInverse)
    filemenu.add_command(label="Eigen Values", command=onEigenValues)
    filemenu.add_command(label="Eugen Vectors", command=onEigenVectors)
    menubar.add_cascade(label="Operations", menu=filemenu)
    root.config(menu=menubar)


root = tk.Tk()
root.geometry("800x600")
root.title("Matrix Operations")
init_root()

tk.mainloop()
