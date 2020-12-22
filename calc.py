from tkinter import *

root = Tk()

root.title("Calc")
# root.geometry("300x200")


# entrybox def's
e = Entry(root, width=35, bd=2, borderwidth=5, bg="powder blue")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# func def's
def butt_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def butt_clear():
    e.delete(0, END)


def butt_add():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    e.delete(0, END)


def butt_equal():
    sec_num = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, f_num + int(sec_num))
    if math == "sub":
        e.insert(0, f_num - int(sec_num))
    if math == "mul":
        e.insert(0, f_num * int(sec_num))
    if math == "div":
        e.insert(0, f_num / int(sec_num))


def butt_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_number)
    e.delete(0, END)


def butt_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "mul"
    f_num = int(first_number)
    e.delete(0, END)


def butt_divide():
    first_number = e.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_number)
    e.delete(0, END)


# button def's
butt_1 = Button(root, text="1", padx=30, pady=20,
                bg="powder blue", command=lambda: butt_click(1))
butt_2 = Button(root, text="2", padx=30, pady=20,
                bg="powder blue", command=lambda: butt_click(2))
butt_3 = Button(root, text="3", padx=30, pady=20,
                bg="powder blue", command=lambda: butt_click(3))
butt_4 = Button(root, text="4", padx=30, pady=20,
                bg="powder blue", command=lambda: butt_click(4))
butt_5 = Button(root, text="5", padx=30, pady=20,
                bg="powder blue", command=lambda: butt_click(5))
butt_6 = Button(root, text="6", padx=30, pady=20,
                bg="powder blue", command=lambda: butt_click(6))
butt_7 = Button(root, text="7", padx=30, pady=20,
                bg="powder blue", command=lambda: butt_click(7))
butt_8 = Button(root, text="8", padx=30, pady=20,
                bg="powder blue", command=lambda: butt_click(8))
butt_9 = Button(root, text="9", padx=30, pady=20,
                bg="powder blue", command=lambda: butt_click(9))
butt_0 = Button(root, text="0", padx=30, pady=20,
                bg="powder blue", command=lambda: butt_click(0))


butt_add = Button(root, text="+", padx=29, pady=20, bg="powder blue",
                  command=butt_add)
butt_equ = Button(root, text="=", padx=70, pady=20, bg="powder blue",
                  command=butt_equal)
butt_clr = Button(root, text="clear", padx=61, pady=20, bg="powder blue",
                  command=butt_clear)
butt_sub = Button(root, text="-", padx=30, pady=20, bg="powder blue",
                  command=butt_subtract)
butt_mul = Button(root, text="*", padx=31, pady=20, bg="powder blue",
                  command=butt_multiply)
butt_div = Button(root, text="/", padx=31, pady=20, bg="powder blue",
                  command=butt_divide)


# button location's
butt_1.grid(row=3, column=0)
butt_2.grid(row=3, column=1)
butt_3.grid(row=3, column=2)

butt_4.grid(row=2, column=0)
butt_5.grid(row=2, column=1)
butt_6.grid(row=2, column=2)

butt_7.grid(row=1, column=0)
butt_8.grid(row=1, column=1)
butt_9.grid(row=1, column=2)

butt_0.grid(row=4, column=0)
butt_clr.grid(row=4, column=1, columnspan=2)
butt_add.grid(row=5, column=0)
butt_equ.grid(row=5, column=1, columnspan=2)

butt_sub.grid(row=6, column=0)
butt_mul.grid(row=6, column=1)
butt_div.grid(row=6, column=2)

root.mainloop()
