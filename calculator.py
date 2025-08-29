import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator 3.13.7")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Create custom font
        self.entry_font = font.Font(size=16, weight="bold")
        self.button_font = font.Font(size=14)
        
        # Initialize variables
        self.current_input = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        # Create UI
        self.create_widgets()
    
    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root)
        display_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Entry widget for display
        entry = tk.Entry(
            display_frame, 
            textvariable=self.result_var, 
            font=self.entry_font, 
            bd=0, 
            justify="right", 
            state="readonly",
            readonlybackground="white"
        )
        entry.pack(expand=True, fill="both", ipady=10)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Button layout
        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['00', '0', '.', '=']
        ]
        
        # Create buttons
        for i, row in enumerate(buttons):
            buttons_frame.rowconfigure(i, weight=1)
            for j, button_text in enumerate(row):
                buttons_frame.columnconfigure(j, weight=1)
                button = tk.Button(
                    buttons_frame, 
                    text=button_text, 
                    font=self.button_font,
                    command=lambda txt=button_text: self.on_button_click(txt)
                )
                button.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
                
                # Color special buttons
                if button_text in ['C', '⌫']:
                    button.config(bg="#ff6666", fg="white")
                elif button_text in ['/', '*', '-', '+', '=']:
                    button.config(bg="#4682B4", fg="white")
                elif button_text == '%':
                    button.config(bg="#DAA520", fg="white")
    
    def on_button_click(self, button_text):
        if button_text == 'C':
            self.current_input = ""
            self.result_var.set("0")
        elif button_text == '⌫':
            self.current_input = self.current_input[:-1]
            self.result_var.set(self.current_input or "0")
        elif button_text == '=':
            try:
                # Evaluate the expression safely
                result = str(eval(self.current_input))
                self.result_var.set(result)
                self.current_input = result
            except:
                self.result_var.set("Error")
                self.current_input = ""
        elif button_text == '%':
            try:
                # Calculate percentage
                result = str(eval(self.current_input) / 100)
                self.result_var.set(result)
                self.current_input = result
            except:
                self.result_var.set("Error")
                self.current_input = ""
        else:
            # Handle multiple decimal points
            if button_text == '.':
                # Check if the last number already has a decimal point
                parts = self.current_input.split()
                if parts and '.' in parts[-1]:
                    return
            
            self.current_input += button_text
            self.result_var.set(self.current_input)

def main():
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()