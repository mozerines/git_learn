from tkinter import *

window = Tk()
window.title('Калькулятор')
window.geometry('400x450+700+100')


def input_into_entry(symbol):
    entry.insert(END, symbol)


def clear():
    entry.delete(0, END)


def count_result():
    text = entry.get()
    result = 0
    first = 0
    second = 0
    if "+" in text:
        splitted_text = text.split('+')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first + first
    if "-" in text:
        splitted_text = text.split('-')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first - first
    if "*" in text:
        splitted_text = text.split('*')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first * first
    if "/" in text:
        splitted_text = text.split('/')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first / first
    clear()
    entry.insert(0, result)


entry = Entry(window, width=15, font=('', 18))
entry.place(x=100, y=50)

button1 = Button(window, bg='gray', fg='white', text='1', command=lambda: input_into_entry(1))
button1.place(x=100, y=100, width=50, height=50)
button2 = Button(window, bg='gray', fg='white', text='2', command=lambda: input_into_entry(2))
button2.place(x=150, y=100, width=50, height=50)
button3 = Button(window, bg='gray', fg='white', text='3', command=lambda: input_into_entry(3))
button3.place(x=200, y=100, width=50, height=50)
button4 = Button(window, bg='gray', fg='white', text='4', command=lambda: input_into_entry(4))
button4.place(x=100, y=150, width=50, height=50)
button5 = Button(window, bg='gray', fg='white', text='5', command=lambda: input_into_entry(5))
button5.place(x=150, y=150, width=50, height=50)
button6 = Button(window, bg='gray', fg='white', text='6', command=lambda: input_into_entry(6))
button6.place(x=200, y=150, width=50, height=50)
button7 = Button(window, bg='gray', fg='white', text='7', command=lambda: input_into_entry(7))
button7.place(x=100, y=200, width=50, height=50)
button8 = Button(window, bg='gray', fg='white', text='8', command=lambda: input_into_entry(8))
button8.place(x=150, y=200, width=50, height=50)
button9 = Button(window, bg='gray', fg='white', text='9', command=lambda: input_into_entry(9))
button9.place(x=200, y=200, width=50, height=50)

buttonplus = Button(window, bg='gray', fg='white', text='+', command=lambda: input_into_entry('+'))
buttonplus.place(x=250, y=100, width=50, height=50)

buttonminus = Button(window, bg='gray', fg='white', text='-', command=lambda: input_into_entry('-'))
buttonminus.place(x=250, y=150, width=50, height=50)

buttondvd = Button(window, bg='gray', fg='white', text='/', command=lambda: input_into_entry('/'))
buttondvd.place(x=250, y=200, width=50, height=50)

buttonmulity = Button(window, bg='gray', fg='white', text='*', command=lambda: input_into_entry('*'))
buttonmulity.place(x=250, y=250, width=50, height=50)

buttonrslt = Button(window, bg='gray', fg='white', text='=', command=count_result)
buttonrslt.place(x=200, y=250, width=50, height=50)

buttonclr = Button(window, bg='gray', fg='white', text='C', command=clear)
buttonclr.place(x=150, y=250, width=50, height=50)

buttondot = Button(window, bg='gray', fg='white', text='.', command=lambda: input_into_entry('.'))
buttondot.place(x=100, y=250, width=50, height=50)

window.mainloop()
