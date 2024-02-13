import tkinter as tk
class MainFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create a label
        label = tk.Label(self, text="Main Page")
        label.pack(side="top", fill="x", pady=10)

        # Create a button
        button1 = tk.Button(self, text="Go to page one",
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack()

        # Create a button
        button2 = tk.Button(self, text="Go to page two",
                            command=lambda: controller.show_frame("PageTwo"))
        button2.pack()

        # Create a button
        button3 = tk.Button(self, text="Go to page three",
                            command=lambda: controller.show_frame("PageThree"))
        button3.pack()

        # Create a button
        button4 = tk.Button(self, text="Go to page four",
                            command=lambda: controller.show_frame("PageFour"))
        button4.pack()

        # Create a button
        button5 = tk.Button(self, text="Go to page five",
                            command=lambda: controller.show_frame("PageFive"))
        button5.pack()

        # Create a button
        button6 = tk.Button(self, text="Go to page six",
                            command=lambda: controller.show_frame("PageSix"))
        button6.pack()

        # Create a button
        button7 = tk.Button(self, text="Go to page seven",
                            command=lambda: controller.show_frame("PageSeven"))
        button7.pack()

        # Create a button
        button8 = tk.Button(self, text="Go to page eight",
                            command=lambda: controller.show_frame("PageEight"))
        button8.pack()

        # Create a button
        button9 = tk.Button(self, text="Go to page nine",
                            command=lambda: controller.show_frame("PageNine"))
        button9.pack()

        # Create a button
        button10 = tk.Button(self, text="Go to page ten",
                            command=lambda: controller.show_frame("PageTen"))
        button10.pack()

        # Create a button
        button11 = tk.Button(self, text="Go to page eleven",
                            command=lambda: controller.show_frame("PageEleven"))
        button11.pack()

        # Create a button
        button12 = tk.Button(self, text="Go to page twelve")