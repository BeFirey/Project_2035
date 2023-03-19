import tkinter
from Дополнительный import *

def main():
    try:
        average(entry, label_average)
        median(entry, label_median)
        maxim(entry, label_max)
        minim(entry, label_min)
        summ(entry, label_sum)
        multip(entry, label_multiplication)
    except ZeroDivisionError:
        messagebox.showerror('Ошибка', 'Некоректный ввод! Пустая строка!')
        entry.delete(0, tkinter.END)
    except ValueError:
        messagebox.showerror('Ошибка', 'Некоректный ввод')
        entry.delete(0, tkinter.END)

def main_clear():
    clear(entry, label_average, label_median, label_max, label_min, label_sum, label_multiplication)

window = tkinter.Tk()
window.title('Работа с массивами')
window.geometry('400x380')
window.resizable(False, False)

main_label = tkinter.Label(text='Введи числа через пробел', font=('Arial',15), fg='Black')
main_label.pack(pady=5)

entry = tkinter.Entry(width= 45)
entry.pack(pady= 10)

button = tkinter.Button(text= 'Вычислить', font=20, bg='grey', fg='black', command=main)
button_clear = tkinter.Button(text= ' Очистить', font=20, bg='grey',fg='black', command=main_clear)
button.pack(pady=2)
button_clear.pack(pady=8)

label_median = tkinter.Label(text='Медиана: ', font=('Arial', 12), bg= 'yellow')
label_sum = tkinter.Label(text='Сумма чисел: ', font=('Arial', 12), bg='cyan')
label_min = tkinter.Label(text='Минимальное число: ', font=('Arial', 12), bg='yellow')
label_max = tkinter.Label(text='Максимальное число: ', font=('Arial', 12), bg='cyan')
label_multiplication = tkinter.Label(text='Произведение чисел: ', font=('Arial', 12), bg= 'yellow')
label_average = tkinter.Label(text='Среднее арифметическое: ', font=('Arial', 12), bg='cyan')

label_median.pack(anchor='w', pady=5, padx=5)
label_sum.pack(anchor='w', pady=5, padx=5)
label_min.pack(anchor='w', pady=5, padx=5)
label_max.pack(anchor='w', pady=5, padx=5)
label_multiplication.pack(anchor='w', pady=5, padx=5)
label_average.pack(anchor='w', pady=5, padx=5)

window.mainloop()