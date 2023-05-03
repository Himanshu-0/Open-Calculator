# Project3: Making a program that creates a Calculator
from tkinter import*
calculator = Tk()
calculator.title('Open Calculator')
calculator.geometry('600x700+500+50')
calculator.resizable(False,False)
calculator.configure(bg='#000000')

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_clearone():
    global expression
    expression = ""
    input_text.set(input_text.get()[0:-1])
    
def btn_equal():
    global expression
    result = str(eval(expression)) 
    input_text.set(result)
    expression = ""
expression = ""

input_text = StringVar()
input_field = Entry(calculator, font=('arial', 30, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

Button(calculator,text='AC',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#ff9966',bg='#b30000',command = lambda: btn_clear()).place(x=15,y=200)
Button(calculator,text='c',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#b30000',bg='#ccffff',command = lambda: btn_clearone()).place(x=160,y=200)
Button(calculator,text='%',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#000000',bg='#ccffff',command = lambda: btn_click("%")).place(x=305,y=200)
Button(calculator,text='/',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#000000',bg='#ccffff',command = lambda: btn_click("/")).place(x=450,y=200)

Button(calculator,text='7',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#000000',bg='#ff9966',command = lambda: btn_click(7)).place(x=15,y=300)
Button(calculator,text='8',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#000000',bg='#ff9966',command = lambda: btn_click(8)).place(x=160,y=300)
Button(calculator,text='9',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#000000',bg='#ff9966',command = lambda: btn_click(9)).place(x=305,y=300)
Button(calculator,text='*',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#000000',bg='#ccffff',command = lambda: btn_click("*")).place(x=450,y=300)

Button(calculator,text='4',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#000000',bg='#ff9966',command = lambda: btn_click(4)).place(x=15,y=400)
Button(calculator,text='5',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#000000',bg='#ff9966',command = lambda: btn_click(5)).place(x=160,y=400)
Button(calculator,text='6',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#000000',bg='#ff9966',command = lambda: btn_click(6)).place(x=305,y=400)
Button(calculator,text='-',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#000000',bg='#ccffff',command = lambda: btn_click("-")).place(x=450,y=400)

Button(calculator,text='1',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#000000',bg='#ff9966',command = lambda: btn_click(1)).place(x=15,y=500)
Button(calculator,text='2',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#000000',bg='#ff9966',command = lambda: btn_click(2)).place(x=160,y=500)
Button(calculator,text='3',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#000000',bg='#ff9966',command = lambda: btn_click(3)).place(x=305,y=500)
Button(calculator,text='+',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#000000',bg='#ccffff',command = lambda: btn_click("+")).place(x=450,y=500)

# Button(calculator,text='+\-',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#ff9966',bg='#b30000',command=clear()).place(x=15,y=600)
Button(calculator,text='0',width=11,height =1,font=('arial',30,'bold'),bd=5,fg='#000000',bg='#ff9966',command = lambda: btn_click(0)).place(x=15,y=600)
Button(calculator,text='.',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#000000',bg='#ff9966',command = lambda: btn_click(".")).place(x=305,y=600)
Button(calculator,text='=',width=5,height =1,font=('arial',30,'bold'),bd=5,fg='#000000',bg='#ccffff',command = lambda: btn_equal()).place(x=450,y=600)


calculator.mainloop()