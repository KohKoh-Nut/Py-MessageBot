from llm.llm_utils import generate_response
from reply_bot.capture import ScreenCapture

class ReplyBot:
    def __init__(self):
        self.capture_tool = ScreenCapture()
        self.is_active = False

    def start(self, region):
        """Start auto-replying."""
        self.capture_tool.set_region(region)
        self.is_active = True

    def stop(self):
        """Stop the reply bot."""
        self.is_active = False

    def get_message_and_reply(self):
        """Capture message and generate a response."""
        if not self.is_active:
            return

        message = self.capture_tool.capture_text_from_region()
        if message:
            response = generate_response(message)
            print("Reply:", response)  # This would be sent as a reply in an actual implementation
