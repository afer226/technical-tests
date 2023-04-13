class Computer:

    # Give attributes better names
    active_user = ""

    def _sign_in(self, new_user):
        if not self.active_user:
            self.active_user = new_user
        elif self.active_user != new_user:
            raise Exception("A different user is using this system.")

    def _sign_out(self):
        if self.active_user:
            self.active_user = ""

    def display_message(self, content, identity):
        if not content:
            raise Exception("Message has no contents")

        self._sign_in(identity)

        print(f"{self.active_user} - {content}")

        self._sign_out()

class SignInException(Exception):
    """Exception raised when user sign-on fails."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)

class MessageException(Exception):
    """Exception raised when message is not displayed"""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)