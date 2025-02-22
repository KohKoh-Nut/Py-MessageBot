import tkinter as tk
from tkinter import ttk
from chatbot.chatbot import Chatbot
from reply_bot.reply_bot import ReplyBot

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot & Reply Bot")
        self.root.geometry("400x300")

        self.chatbot = Chatbot()
        self.reply_bot = ReplyBot()

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Chatbot & Reply Bot", font=("MS Sans Serif", 12, "bold")).pack(pady=10)

        self.start_chat_btn = ttk.Button(self.root, text="Start Chatbot", command=self.start_chat)
        self.start_chat_btn.pack(pady=5)

        self.start_reply_btn = ttk.Button(self.root, text="Start Reply Bot", command=self.start_reply_bot)
        self.start_reply_btn.pack(pady=5)

    def start_chat(self):
        chat_window = tk.Toplevel(self.root)
        chat_window.title("Chatbot Chat")

        chat_text = tk.Text(chat_window, height=10, width=40)
        chat_text.pack()

        message_entry = tk.Entry(chat_window)
        message_entry.pack()

        def send_message():
            msg = message_entry.get()
            response = self.chatbot.send_message("default_chat", msg)
            chat_text.insert(tk.END, f"You: {msg}\nBot: {response}\n")

        send_button = tk.Button(chat_window, text="Send", command=send_message)
        send_button.pack()

    def start_reply_bot(self):
        self.reply_bot.start(region=(100, 100, 500, 300))  # Example region
