#Вариант 16
"""
Три цветовода выращивают розы. Определить, какие из известных сортов роз «Анжелика»,
«Виктория», «Гагарин», «Катарина», «Юбилейная», «Южная» имеются у каждого
цветовода, есть хотя бы у одного из цветоводов и каких нет ни у одного из цветоводов.
"""

import tkinter as tk

grower1 = {'Гагарин', 'Виктория', 'Катарина'}
grower2 = {'Гагарин', 'Виктория', 'Южная'}
grower3 = {'Гагарин', 'Юбилейная', 'Южная'}

all_sorts   = {'Анжелика', 'Виктория', 'Гагарин', 'Катарина', 'Юбилейная', 'Южная'}
all_have    = grower1 & grower2 & grower3
atleast_one = grower1 | grower2 | grower3
nobody      = all_sorts - atleast_one

def fmt(s):
    return ', '.join(sorted(s)) if s else '—'

root = tk.Tk()
root.title('Вариант 16')
root.resizable(False, False)

pad = dict(padx=12, pady=4)
F  = ('Helvetica', 11)
FB = ('Helvetica', 11, 'bold')

rows = [
    ('Цветовод 1:', fmt(grower1)),
    ('Цветовод 2:', fmt(grower2)),
    ('Цветовод 3:', fmt(grower3)),
    ('', ''),
    ('Есть у всех (∩):', fmt(all_have)),
    ('Есть хотя бы у одного (∪):', fmt(atleast_one)),
    ('Нет ни у кого (∖):', fmt(nobody)),
]

for i, (label, value) in enumerate(rows):
    if label == '':
        tk.Frame(root, height=1, bg='#cccccc').grid(
            row=i, column=0, columnspan=2, sticky='ew', padx=12, pady=4)
        continue
    tk.Label(root, text=label, font=FB, anchor='w').grid(
        row=i, column=0, sticky='w', **pad)
    tk.Label(root, text=value, font=F, anchor='w', wraplength=320).grid(
        row=i, column=1, sticky='w', **pad)

root.mainloop()