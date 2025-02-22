from llm.llm_utils import generate_response

class Chatbot:
    def __init__(self):
        self.conversations = {}

    def start_chat(self, chat_id):
        """Start a new chat session."""
        self.conversations[chat_id] = []

    def send_message(self, chat_id, message):
        """Send a message to the chatbot."""
        if chat_id not in self.conversations:
            self.start_chat(chat_id)

        response = generate_response(message)
        self.conversations[chat_id].append((message, response))
        return response
