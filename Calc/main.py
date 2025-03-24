import tkinter as tk
import tkinter.ttk as ttk

Window = tk.Tk()
Window.title('Калькулятор')
Window.geometry("400x450+700+100")

entry = ttk.Entry(width=15, font=('', 18))
entry_style = ttk.Style()
entry_style.configure('TEntry', background='#4f4f4f', foreground='#4f4f4f')
button_style = ttk.Style()
button_style.configure('TButton', background='#f66009', foreground='#4f4f4f')


def clear():
    entry.delete(0, tk.constants.END)


def insert(symbol):
    entry.insert(tk.constants.END, string=symbol)


def show_error_message():
    clear()
    entry.insert(0, 'Введите 1 простую операцию!')
    Window.after(3000, clear)
    entry.config(font=18)


def calc():
    txt = entry.get()
    try:
        if '+' in txt:
            txt = txt.split('+')
            first = float(txt[0])
            second = float(txt[1])
            clear()
            insert(first + second)
        if '-' in txt:
            txt = txt.split('-')
            first = float(txt[0])
            second = float(txt[1])
            clear()
            insert(first - second)
        if 'x' in txt:
            txt = txt.split('x')
            first = float(txt[0])
            second = float(txt[1])
            clear()
            insert(first * second)
        if '/' in txt:
            txt = txt.split('/')
            first = float(txt[0])
            second = float(txt[1])
            clear()
            insert(first / second)
        if '%' in txt:
            txt = txt.split('%')
            first = float(txt[0])
            second = float(txt[1])
            clear()
            insert(first / 100 * second)
        if '^' in txt:
            txt = txt.split('^')
            first = float(txt[0])
            second = float(txt[1])
            clear()
            insert(first ** second)
    except:
        show_error_message()


if True:
    # Button Creation
    if True:
        button_1 = ttk.Button(text="1", command=lambda: insert(1))
        button_2 = ttk.Button(text="2", command=lambda: insert(2))
        button_3 = ttk.Button(text="3", command=lambda: insert(3))
        button_4 = ttk.Button(text="4", command=lambda: insert(4))
        button_5 = ttk.Button(text="5", command=lambda: insert(5))
        button_6 = ttk.Button(text="6", command=lambda: insert(6))
        button_7 = ttk.Button(text="7", command=lambda: insert(7))
        button_8 = ttk.Button(text="8", command=lambda: insert(8))
        button_9 = ttk.Button(text="9", command=lambda: insert(9))
        button_0 = ttk.Button(text="0", command=lambda: insert(0))
        factorial_button = ttk.Button(text='WIP')
        dot_button = ttk.Button(text='.', command=lambda: insert("."))
        power_button = ttk.Button(text='^', command=lambda: insert("^"))
        total_button = ttk.Button(text="=", command=calc)
        plus_button = ttk.Button(text="+", command=lambda: insert("+"))
        minus_button = ttk.Button(text="-", command=lambda: insert("-"))
        multiple_button = ttk.Button(text="x", command=lambda: insert("x"))
        divide_button = ttk.Button(text="/", command=lambda: insert("/"))
        percent_button = ttk.Button(text="%", command=lambda: insert("%"))
        clear_button = ttk.Button(text="C", command=clear)

    # Text Field
    entry.place(x=100, y=0, width=200, height=50)

    # 1 Button Row
    if True:
        clear_button.place(x=100, y=50, width=50, height=50)
        power_button.place(x=150, y=50, width=50, height=50)
        percent_button.place(x=200, y=50, width=50, height=50)
        divide_button.place(x=250, y=50, width=50, height=50)

    # 2 Button Row
    if True:
        button_7.place(x=100, y=100, width=50, height=50)
        button_8.place(x=150, y=100, width=50, height=50)
        button_9.place(x=200, y=100, width=50, height=50)
        multiple_button.place(x=250, y=100, width=50, height=50)

    # 3 Button Row
    if True:
        button_4.place(x=100, y=150, width=50, height=50)
        button_5.place(x=150, y=150, width=50, height=50)
        button_6.place(x=200, y=150, width=50, height=50)
        minus_button.place(x=250, y=150, width=50, height=50)

    # 4 Button Row
    if True:
        button_1.place(x=100, y=200, width=50, height=50)
        button_2.place(x=150, y=200, width=50, height=50)
        button_3.place(x=200, y=200, width=50, height=50)
        plus_button.place(x=250, y=200, width=50, height=50)

    # 5 Button Row
    if True:
        factorial_button.place(x=100, y=250, width=50, height=50)
        button_0.place(x=150, y=250, width=50, height=50)
        dot_button.place(x=200, y=250, width=50, height=50)
        total_button.place(x=250, y=250, width=50, height=50)

Window.mainloop()
