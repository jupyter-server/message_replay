from jupyter_server.extension.application import ExtensionApp
from traitlets import Unicode

from .handlers import PingHandler


class Extension(ExtensionApp):

    name = "message_replay"
    handlers = [("message-replay/ping", PingHandler)]

    # Example of a configurable trait. This is meant to be replaced
    # with configurable traits for this extension.
    ping_response = Unicode(default_value="pong").tag(config=True)

    def initialize_settings(self):
        self.settings.update({"ping_response": self.ping_response})
