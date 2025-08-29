import tkinter as tk
from tkinter import scrolledtext, font
import random
import datetime
import time

class SimpleChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Chatbot")
        self.root.geometry("500x600")
        self.root.resizable(True, True)
        self.root.configure(bg='#2c3e50')
        
        # Chatbot knowledge base
        self.responses = {
            "hello": ["Hello! 👋", "Hi there!", "Hey! How can I help you?"],
            "how are you": ["I'm doing great, thank you!", "I'm functioning perfectly!", "All systems operational! 🤖"],
            "what's your name": ["I'm ChatBot, your friendly AI assistant!", "You can call me ChatBot!", "I'm Bot, nice to meet you!"],
            "who made you": ["I was created by a Python developer using Tkinter!", "I'm built with Python and love! 💻"],
            "time": [f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"],
            "date": [f"Today is {datetime.datetime.now().strftime('%Y-%m-%d')}"],
            "thank you": ["You're welcome! 😊", "Anytime!", "Happy to help!"],
            "bye": ["Goodbye! 👋", "See you later!", "Take care!"],
            "weather": ["I'm sorry, I don't have access to weather data right now.", "You might want to check a weather app for that!"],
            "joke": ["Why don't scientists trust atoms? Because they make up everything! 😄", 
                    "Why did the scarecrow win an award? He was outstanding in his field! 🌾",
                    "What do you call a fake noodle? An impasta! 🍝"],
            "help": ["I can respond to: hello, how are you, what's your name, who made you, time, date, thank you, bye, weather, joke, help"],
            "default": ["That's interesting! Tell me more.", "I'm still learning. Could you rephrase that?", 
                       "I didn't understand that. Try asking something else!"]
        }
        
        # Colors
        self.colors = {
            "bg": "#2c3e50",
            "chat_bg": "#34495e",
            "user_bg": "#3498db",
            "bot_bg": "#27ae60",
            "text_color": "#ecf0f1",
            "input_bg": "#2c3e50",
            "button_bg": "#f39c12"
        }
        
        # Fonts
        self.chat_font = font.Font(family="Arial", size=10)
        self.input_font = font.Font(family="Arial", size=12)
        self.button_font = font.Font(family="Arial", size=10, weight="bold")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg=self.colors["bg"], padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="🤖 Python Chatbot", 
            font=font.Font(family="Arial", size=16, weight="bold"), 
            fg="white", 
            bg=self.colors["bg"],
            pady=10
        )
        title_label.pack()
        
        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(
            main_frame,
            wrap=tk.WORD,
            width=50,
            height=20,
            font=self.chat_font,
            bg=self.colors["chat_bg"],
            fg=self.colors["text_color"],
            state=tk.DISABLED
        )
        self.chat_area.pack(pady=10, fill=tk.BOTH, expand=True)
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg=self.colors["bg"])
        input_frame.pack(fill=tk.X, pady=10)
        
        # User input field
        self.user_input = tk.Entry(
            input_frame,
            font=self.input_font,
            bg=self.colors["input_bg"],
            fg=self.colors["text_color"],
            insertbackground="white"
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.user_input.bind("<Return>", lambda event: self.send_message())
        
        # Send button
        send_button = tk.Button(
            input_frame,
            text="Send",
            font=self.button_font,
            bg=self.colors["button_bg"],
            fg="white",
            command=self.send_message
        )
        send_button.pack(side=tk.RIGHT)
        
        # Clear button
        clear_button = tk.Button(
            main_frame,
            text="Clear Chat",
            font=self.button_font,
            bg="#e74c3c",
            fg="white",
            command=self.clear_chat
        )
        clear_button.pack(pady=5)
        
        # Add welcome message
        self.add_message("Bot", "Hello! I'm your friendly chatbot. Type 'help' to see what I can do!")
        
    def add_message(self, sender, message):
        self.chat_area.config(state=tk.NORMAL)
        
        # Add timestamp
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        
        # Configure tags for different senders
        if sender == "User":
            self.chat_area.tag_config("user", background=self.colors["user_bg"], 
                                    foreground="white", justify="right", 
                                    lmargin1=100, lmargin2=100, rmargin=10)
            self.chat_area.insert(tk.END, f"\n[{timestamp}] You: {message}\n", "user")
        else:
            self.chat_area.tag_config("bot", background=self.colors["bot_bg"], 
                                    foreground="white", justify="left", 
                                    lmargin1=10, lmargin2=10, rmargin=100)
            self.chat_area.insert(tk.END, f"\n[{timestamp}] Bot: {message}\n", "bot")
        
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)  # Auto-scroll to bottom
        
    def send_message(self):
        user_message = self.user_input.get().strip().lower()
        
        if user_message:
            self.add_message("User", user_message)
            self.user_input.delete(0, tk.END)
            
            # Simulate typing delay
            self.root.after(500, lambda: self.process_message(user_message))
    
    def process_message(self, user_message):
        response = self.get_response(user_message)
        self.add_message("Bot", response)
    
    def get_response(self, message):
        # Check for exact matches first
        for key in self.responses:
            if key in message.lower():
                return random.choice(self.responses[key])
        
        # Check for partial matches
        if any(word in message.lower() for word in ["hello", "hi", "hey"]):
            return random.choice(self.responses["hello"])
        elif any(word in message.lower() for word in ["how are", "how do you feel"]):
            return random.choice(self.responses["how are you"])
        elif any(word in message.lower() for word in ["name", "call you"]):
            return random.choice(self.responses["what's your name"])
        elif any(word in message.lower() for word in ["who made", "created", "built"]):
            return random.choice(self.responses["who made you"])
        elif any(word in message.lower() for word in ["time", "clock"]):
            return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
        elif any(word in message.lower() for word in ["date", "day", "today"]):
            return f"Today is {datetime.datetime.now().strftime('%Y-%m-%d')}"
        elif any(word in message.lower() for word in ["thank", "thanks"]):
            return random.choice(self.responses["thank you"])
        elif any(word in message.lower() for word in ["bye", "goodbye", "see you"]):
            return random.choice(self.responses["bye"])
        elif any(word in message.lower() for word in ["weather", "temperature"]):
            return random.choice(self.responses["weather"])
        elif any(word in message.lower() for word in ["joke", "funny"]):
            return random.choice(self.responses["joke"])
        elif any(word in message.lower() for word in ["help", "what can you do"]):
            return random.choice(self.responses["help"])
        
        # Default response
        return random.choice(self.responses["default"])
    
    def clear_chat(self):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state=tk.DISABLED)
        self.add_message("Bot", "Chat cleared! How can I help you?")
    
    def run(self):
        self.root.mainloop()

def main():
    root = tk.Tk()
    chatbot = SimpleChatbot(root)
    chatbot.run()

if __name__ == "__main__":
    main()