from tkinter import *
from tkinter import ttk
import random

class PythonCourseChatbot:
    def __init__(self, master):
        self.master = master
        master.title("Python Course Chatbot")
        master.geometry("450x400")
        master.config(bg='#1d3557')
        master.resizable(False, False)

        # Create and pack the greeting label
        self.greet_label = ttk.Label(master, text="Hello! How can I help you with Python today?",
                                     font=("Arial", 14), background='#1d3557', foreground='#f1faee')
        self.greet_label.pack(pady=20, fill='x', padx=20)

        # Create and pack the message entry field
        self.message_entry = ttk.Entry(master, width=50, font=("Arial", 12), background='#a8dadc',
                                       foreground='#1d3557')
        self.message_entry.pack(ipady=10, padx=20)

        # Create and pack the send button
        self.send_button = ttk.Button(master, text="Send", style='Send.TButton', command=self.send_message)
        self.send_button.pack(pady=10, padx=20)

        # Create and pack the conversation label
        self.conversation_label = ttk.Label(master, text="", font=("Arial", 12), background='#1d3557',
                                            foreground='#f1faee', wraplength=380, justify='left')
        self.conversation_label.pack(pady=20, fill='both', padx=20, expand=True)

        # Set the responses for the chatbot
        self.responses = ["Have you learned about functions in Python?", "Do you know what a for loop is?",
                          "What's your favorite Python library?", "Have you worked with data in Python?",
                          "What's the last thing you learned in your Python course?"]

    # Function to send the user message and receive a response from the chatbot
    def send_message(self):
        message = self.message_entry.get()
        self.conversation_label.config(text=f"You: {message}\n", anchor='w')
        self.message_entry.delete(0, END)

        response = self.get_response(message)
        self.conversation_label.config(text=self.conversation_label.cget('text') + f"Chatbot: {response}\n",
                                        anchor='w')

    # Function to get a response from the chatbot based on the user's message
    def get_response(self, message):
        if "functions" in message.lower():
            return "Functions are an essential part of Python programming. Have you learned how to define your own functions?"
        elif "for loop" in message.lower():
            return "A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). Have you used for loops in your Python course?"
        elif "library" in message.lower():
            return "There are many popular Python libraries, such as NumPy, Pandas, and Matplotlib. What's your favorite library to work with?"
        elif "data" in message.lower():
            return "Python is great for working with data! Have you learned about data types, variables, and data structures like lists and dictionaries?"
        elif "last" in message.lower() and "learned" in message.lower():
            return "The last thing I learned in my Python course was how to work with APIs to retrieve data from external sources."
        else:
            return random.choice(self.responses)

root = Tk()
style = ttk.Style(root)
style.configure('Send.TButton', font=('Arial', 12), background='#007bff', foreground='#010b13', padding=10, 
                borderwidth=0, focuscolor='#007bff', activebackground='#0062cc', activeforeground='#010b13')

PythonCourseChatbot = PythonCourseChatbot(root)
root.mainloop()
