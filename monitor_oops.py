import psutil
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class SystemMonitor(App):

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Loading...", id="stats")
        yield Footer()

    def on_mount(sled) -> None:
        self.set_interval(1.0)