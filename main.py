import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#applicaiton de calculatrice

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.resizable(width=True, height=True)
        self.geometry('500x500')
        self.frames = {}
        self.create_frames()
        self.create_buttons()
        self.create_entries()
        self.create_labels()
        self.create_key_bindings()
        self.bind('<Key>', self.key_press)
        self.bind('<KeyRelease>', self.key_release)
        self.bind('<Return>', self.key_press)
        self.bind('<Escape>', self.key_press)
        self.bind('<Delete>', self.key_press)
        self.bind('<BackSpace>', self.key_press)
        self.bind('<KP_Enter>', self.key_press)
        self.bind('<KP_Add>', self.key_press)
        self.bind('<KP_Subtract>', self.key_press)
        self.bind('<KP_Multiply>', self.key_press)
        self.bind('<KP_Divide>', self.key_press)
        self.bind('<KP_Decimal>', self.key_press)
        self.bind('<KP_0>', self.key_press)
        self.bind('<KP_1>', self.key_press)
        self.bind('<KP_2>', self.key_press)
        self.bind('<KP_3>', self.key_press)
        self.bind('<KP_4>', self.key_press)
        self.bind('<KP_5>', self.key_press)
        self.bind('<KP_6>', self.key_press)
        self.bind('<KP_7>', self.key_press)
        self.bind('<KP_8>', self.key_press)
        self.bind('<KP_9>', self.key_press)
        self.function = None

    def create_frames(self):
        self.frames['display_frame'] = ttk.Frame(self)
        self.frames['display_frame'].pack(side='top', fill='both', expand=True)
        self.frames['button_frame'] = ttk.Frame(self)
        self.frames['button_frame'].pack(side='top', fill='both', expand=True)

    def create_buttons(self):
        self.buttons = {}
        self.buttons['1'] = ttk.Button(self.frames['button_frame'], text='1', command=lambda: self.button_press('1'))
        self.buttons['1'].grid(row=0, column=0, sticky='nsew')
        self.buttons['2'] = ttk.Button(self.frames['button_frame'], text='2', command=lambda: self.button_press('2'))
        self.buttons['2'].grid(row=0, column=1, sticky='nsew')
        self.buttons['3'] = ttk.Button(self.frames['button_frame'], text='3', command=lambda: self.button_press('3'))
        self.buttons['3'].grid(row=0, column=2, sticky='nsew')
        self.buttons['4'] = ttk.Button(self.frames['button_frame'], text='4', command=lambda: self.button_press('4'))
        self.buttons['4'].grid(row=1, column=0, sticky='nsew')
        self.buttons['5'] = ttk.Button(self.frames['button_frame'], text='5', command=lambda: self.button_press('5'))
        self.buttons['5'].grid(row=1, column=1, sticky='nsew')
        self.buttons['6'] = ttk.Button(self.frames['button_frame'], text='6', command=lambda: self.button_press('6'))
        self.buttons['6'].grid(row=1, column=2, sticky='nsew')
        self.buttons['7'] = ttk.Button(self.frames['button_frame'], text='7', command=lambda: self.button_press('7'))
        self.buttons['7'].grid(row=2, column=0, sticky='nsew')
        self.buttons['8'] = ttk.Button(self.frames['button_frame'], text='8', command=lambda: self.button_press('8'))
        self.buttons['8'].grid(row=2, column=1, sticky='nsew')
        self.buttons['9'] = ttk.Button(self.frames['button_frame'], text='9', command=lambda: self.button_press('9'))
        self.buttons['9'].grid(row=2, column=2, sticky='nsew')
        self.buttons['0'] = ttk.Button(self.frames['button_frame'], text='0', command=lambda: self.button_press('0'))
        self.buttons['0'].grid(row=3, column=1, sticky='nsew')

        # make buttons fit the frame
        for x in range(3):
            self.frames['button_frame'].columnconfigure(x, weight=1)
        for y in range(4):
            self.frames['button_frame'].rowconfigure(y, weight=1)
    def create_entries(self):
        self.entries = {}
        self.entries['display_entry'] = ttk.Entry(self.frames['display_frame'], justify='right')
        self.entries['display_entry'].pack(side='top', fill='both', expand=True)
        #make the font adjust to the window size
        self.entries['display_entry'].config(font=('Helvetica', 20))

    def create_labels(self):
        self.labels = {}
        self.labels['memory_label'] = ttk.Label(self.frames['display_frame'], anchor='e')
        self.labels['memory_label'].pack(side='top', fill='both', expand=True)

    def create_key_bindings(self):
        self.bind('<Key>', self.key_press)
        self.bind('<KeyRelease>', self.key_release)
        self.bind('<Return>', self.key_press)
        self.bind('<Escape>', self.key_press)
        self.bind('<Delete>', self.key_press)
        self.bind('<BackSpace>', self.key_press)
        self.bind('<KP_Enter>', self.key_press)
        self.bind('<KP_Add>', self.key_press)
        self.bind('<KP_Subtract>', self.key_press)
        self.bind('<KP_Multiply>', self.key_press)
        self.bind('<KP_Divide>', self.key_press)
        self.bind('<KP_Decimal>', self.key_press)
        self.bind('<KP_0>', self.key_press)
        self.bind('<KP_1>', self.key_press)
        self.bind('<KP_2>', self.key_press)
        self.bind('<KP_3>', self.key_press)
        self.bind('<KP_4>', self.key_press)
        self.bind('<KP_5>', self.key_press)
        self.bind('<KP_6>', self.key_press)
        self.bind('<KP_7>', self.key_press)
        self.bind('<KP_8>', self.key_press)
        self.bind('<KP_9>', self.key_press)

    def key_press(self, event):
        self.key_pressed = event.keysym
        print(self.key_pressed)
        self.button_press(self.key_pressed)

    def key_release(self, event):
        self.key_pressed = None

    def button_press(self, button):
        if button == 'Escape':
            self.clear()
        elif button == 'BackSpace':
            self.backspace()
        elif button == 'Delete':
            self.clear()
        elif button == 'Return':
            self.equals()
        elif button == 'equal':
            self.equals()
        elif button == 'plus':
            self.add()
        elif button == 'minus':
            self.subtract()
        elif button == 'asterisk':
            self.multiply()
        elif button == 'slash':
            self.divide()
        elif button == 'period':
            self.decimal()
        elif button == 'KP_Insert':
            self.memory_store()


        elif button == '0':
            self.number_press('0')
        elif button == '1':
            self.number_press('1')
        elif button == '2':
            self.number_press('2')
        elif button == '3':
            self.number_press('3')
        elif button == '4':
            self.number_press('4')
        elif button == '5':
            self.number_press('5')
        elif button == '6':
            self.number_press('6')
        elif button == '7':
            self.number_press('7')
        elif button == '8':
            self.number_press('8')
        elif button == '9':
            self.number_press('9')

    def number_press(self, value):
        entry_value = self.entries['display_entry'].get()
        entry_value += value
        self.entries['display_entry'].delete(0, 'end')
        self.entries['display_entry'].insert(0, entry_value)

    def clear(self):
        self.entries['display_entry'].delete(0, 'end')
        self.entries['display_entry'].insert(0, '')
        self.labels['memory_label'].config(text='')
        self.first_number = None
        self.second_number = None
        self.function = None
        self.result = None

    def backspace(self):
        entry_value = self.entries['display_entry'].get()
        entry_value = entry_value[:-1]
        self.entries['display_entry'].delete(0, 'end')
        self.entries['display_entry'].insert(0, entry_value)

    def add(self):
        self.first_number = self.entries['display_entry'].get()
        self.function = 'add'
        self.entries['display_entry'].delete(0, 'end')
        self.labels['memory_label'].config(text=self.first_number + ' +')

    def subtract(self):
        self.first_number = self.entries['display_entry'].get()
        self.function = 'subtract'
        self.entries['display_entry'].delete(0, 'end')
        self.labels['memory_label'].config(text=self.first_number + ' -')

    def multiply(self):
        self.first_number = self.entries['display_entry'].get()
        self.function = 'multiply'
        self.entries['display_entry'].delete(0, 'end')
        self.labels['memory_label'].config(text=self.first_number + ' x')

    def divide(self):
        self.first_number = self.entries['display_entry'].get()
        self.function = 'divide'
        self.entries['display_entry'].delete(0, 'end')
        self.labels['memory_label'].config(text=self.first_number + ' /')

    def equals(self):

        self.second_number = self.entries['display_entry'].get()
        self.entries['display_entry'].delete(0, 'end')
        self.labels['memory_label'].config(text='')
        if self.function == 'add':
            self.result = float(self.first_number) + float(self.second_number)
        elif self.function == 'subtract':
            self.result = float(self.first_number) - float(self.second_number)
        elif self.function == 'multiply':
            self.result = float(self.first_number) * float(self.second_number)
        elif self.function == 'divide':
            self.result = float(self.first_number) / float(self.second_number)
        self.entries['display_entry'].insert(0, str(self.result))
        self.first_number = None
        self.second_number = None
        self.function = None
        self.result = None

    def decimal(self):
        entry_value = self.entries['display_entry'].get()
        entry_value += '.'
        self.entries['display_entry'].delete(0, 'end')
        self.entries['display_entry'].insert(0, entry_value)

    def memory_store(self):
        self.memory = self.entries['display_entry'].get()
        self.labels['memory_label'].config(text='M')








if __name__ == '__main__':
    root = Calculator()
    root.mainloop()

