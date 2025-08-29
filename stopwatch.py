import tkinter as tk
from tkinter import ttk, font
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Stopwatch")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg='#2c3e50')
        
        # Stopwatch variables
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.lap_times = []
        
        # Create custom fonts
        self.title_font = font.Font(family="Arial", size=16, weight="bold")
        self.time_font = font.Font(family="Courier New", size=32, weight="bold")
        self.button_font = font.Font(family="Arial", size=12, weight="bold")
        self.lap_font = font.Font(family="Arial", size=10)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='#2c3e50', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="PYTHON STOPWATCH", 
            font=self.title_font, 
            fg='#ecf0f1', 
            bg='#2c3e50'
        )
        title_label.pack(pady=(0, 20))
        
        # Time display
        self.time_display = tk.Label(
            main_frame,
            text="00:00:00.00",
            font=self.time_font,
            fg='#27ae60',
            bg='#34495e',
            relief=tk.SUNKEN,
            bd=3,
            padx=20,
            pady=10
        )
        self.time_display.pack(pady=10, fill=tk.X)
        
        # Buttons frame
        button_frame = tk.Frame(main_frame, bg='#2c3e50')
        button_frame.pack(pady=20)
        
        # Start/Stop button
        self.start_stop_button = tk.Button(
            button_frame,
            text="START",
            font=self.button_font,
            bg='#27ae60',
            fg='white',
            width=8,
            height=2,
            command=self.toggle_start_stop
        )
        self.start_stop_button.grid(row=0, column=0, padx=5)
        
        # Lap button
        self.lap_button = tk.Button(
            button_frame,
            text="LAP",
            font=self.button_font,
            bg='#3498db',
            fg='white',
            width=8,
            height=2,
            command=self.record_lap,
            state=tk.DISABLED
        )
        self.lap_button.grid(row=0, column=1, padx=5)
        
        # Reset button
        self.reset_button = tk.Button(
            button_frame,
            text="RESET",
            font=self.button_font,
            bg='#e74c3c',
            fg='white',
            width=8,
            height=2,
            command=self.reset
        )
        self.reset_button.grid(row=0, column=2, padx=5)
        
        # Lap times frame
        lap_frame = tk.Frame(main_frame, bg='#2c3e50')
        lap_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # Lap times label
        lap_label = tk.Label(
            lap_frame,
            text="LAP TIMES:",
            font=self.button_font,
            fg='#ecf0f1',
            bg='#2c3e50',
            anchor='w'
        )
        lap_label.pack(fill=tk.X)
        
        # Lap times listbox with scrollbar
        lap_container = tk.Frame(lap_frame, bg='#2c3e50')
        lap_container.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(lap_container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox for lap times
        self.lap_listbox = tk.Listbox(
            lap_container,
            yscrollcommand=scrollbar.set,
            font=self.lap_font,
            bg='#34495e',
            fg='#ecf0f1',
            selectbackground='#3498db',
            height=8,
            relief=tk.FLAT,
            bd=0
        )
        self.lap_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar.config(command=self.lap_listbox.yview)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg='#34495e',
            fg='#bdc3c7'
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def toggle_start_stop(self):
        if not self.running:
            # Start the stopwatch
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.start_stop_button.config(text="STOP", bg='#e74c3c')
            self.lap_button.config(state=tk.NORMAL)
            self.status_var.set("Running...")
            self.update_time()
        else:
            # Stop the stopwatch
            self.running = False
            self.start_stop_button.config(text="START", bg='#27ae60')
            self.lap_button.config(state=tk.DISABLED)
            self.status_var.set("Stopped")
    
    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.display_time(self.elapsed_time)
            self.root.after(10, self.update_time)  # Update every 10ms
    
    def display_time(self, elapsed):
        # Convert seconds to hours, minutes, seconds, and milliseconds
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)
        milliseconds = int((elapsed - int(elapsed)) * 100)
        
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}"
        self.time_display.config(text=time_str)
    
    def record_lap(self):
        if self.running:
            lap_time = self.elapsed_time
            self.lap_times.append(lap_time)
            
            # Calculate lap number and time
            lap_number = len(self.lap_times)
            
            # Format lap time
            hours = int(lap_time // 3600)
            minutes = int((lap_time % 3600) // 60)
            seconds = int(lap_time % 60)
            milliseconds = int((lap_time - int(lap_time)) * 100)
            lap_time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}"
            
            # Add to listbox
            self.lap_listbox.insert(tk.END, f"Lap {lap_number}: {lap_time_str}")
            
            # Auto-scroll to latest lap
            self.lap_listbox.see(tk.END)
            
            self.status_var.set(f"Lap {lap_number} recorded")
    
    def reset(self):
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.lap_times = []
        
        self.time_display.config(text="00:00:00.00")
        self.start_stop_button.config(text="START", bg='#27ae60')
        self.lap_button.config(state=tk.DISABLED)
        self.lap_listbox.delete(0, tk.END)
        self.status_var.set("Reset complete")
    
    def run(self):
        self.root.mainloop()

def main():
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    stopwatch.run()

if __name__ == "__main__":
    main()