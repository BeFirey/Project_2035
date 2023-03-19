import tkinter
from tkinter import messagebox

def average(entry, label):
    label['text'] = 'Среднее арифметическое: '
    a = list(map(float,entry.get().split()))
    av = sum(a)/len(a)
    label['text'] += ' ' * 10
    if '.' in str(av):
        m = str(av).find('.')
        label['text'] += str(av)[:m + 5]
    else:
        label['text'] += str(av)

def median(entry, label):
    label['text'] = 'Медиана:'
    a = list(map(float,entry.get().split()))
    a.sort()
    n = len(a)
    if n % 2 == 1:
        med = a[n // 2]
    else:
        med = (a[n // 2] + a[n // 2 - 1]) / 2
    label['text'] += ' ' * 10
    label['text'] += str(med)

def maxim(entry, label):
    label['text'] = 'Максимальное значение: '
    a = list(map(float,entry.get().split()))
    label['text'] += ' ' * 10
    label['text'] += str(max(a))

def minim(entry, label):
    label['text'] = 'Минимальное значение: '
    a = list(map(float,entry.get().split()))
    label['text'] += ' ' * 10
    label['text'] += str(min(a))

def summ(entry, label):
    label['text'] = 'Сумма чисел: '
    a = list(map(float, entry.get().split()))
    label['text'] += ' ' * 10
    s = 0
    for i in range(len(a)):
        s += a[i]
    label['text'] += str(s)

def multip(entry, label):
    label['text'] = 'Произведение чисел: '
    a = list(map(float, entry.get().split()))
    label['text'] += ' ' * 10
    mult = 1
    for i in range(len(a)):
        mult *= a[i]
    label['text'] += str(mult)

def clear(entry, label1, label2, label3, label4, label5, label6):
    entry.delete(0, tkinter.END)
    label1['text'] = 'Среднее арифметическое: '
    label2['text'] = 'Медиана: '
    label3['text'] = 'Максимальное число: '
    label4['text'] = 'Минимальное число: '
    label5['text'] = 'Сумма чисел : '
    label6['text'] = 'Произведение чисел : '


