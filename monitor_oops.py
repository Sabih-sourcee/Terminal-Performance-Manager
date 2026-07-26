import psutil
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, DataTable

class SystemMonitor(App):
    show_all = False
    BINDINGS = [
        ("x", "kill_selected", "kill_process"),
        ("l", "toggle_view", "Toggle all")
    ]

    def action_toggle_view(self) -> None:
        self.show_all = not self.show_all

    def action_kill_selected(self) -> None:
        table = self.query_one("#process_table", DataTable)
        row_key = table.cursor_row
        row_data = table.get_row_at(row_key)
        pid = int(row_data[0])

        psutil.Process(pid).terminate()
        self.notify(f"Killed PID {pid}")
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Loading...", id="stats")
        yield DataTable(id="process_table")
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one("#process_table", DataTable)
        table.add_columns("PID", "Name", "Memory %")
        table.cursor_type = "row"

        self.set_interval(1.0, self.update_stats)

    def update_stats(self) -> None:
        cpu = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory().percent

        stats_box = self.query_one("#stats", Static)
        stats_box.update(f"CPU: {cpu}% | RAM: {ram}% | show_all={self.show_all}")

        process = []
        for i in psutil.process_iter(['pid', 'name', 'memory_percent']):
            process.append(i.info)

        table = self.query_one('#process_table', DataTable)
        table.clear()

        if self.show_all:
            for p in process:
                table.add_row(str(p['pid']), p['name'], f"{p['memory_percent']:.1f}%")

        else:        
            top5 = []
            remaining = process.copy()
            for i in range(5):
                biggest = remaining[0]
                for p in remaining:
                    if p['memory_percent'] > biggest['memory_percent']:
                        biggest = p
                top5.append(biggest)
                remaining.remove(biggest)

            for p in top5:
                table.add_row(str(p['pid']), p['name'], f"{p['memory_percent']:.1f}%")

if __name__ == "__main__":
    app = SystemMonitor()
    app.run()