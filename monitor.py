import psutil
from rich.console import Console

console = Console()

while True:
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory().percent
    process = []
    console.clear()
    if cpu >= 80:
        console.print(f"CPU Usage: {cpu}%", style="red")
    elif cpu >= 50:
        console.print(f"CPU Usage: {cpu}%", style="yellow")
    else:
        console.print(f"CPU Usage: {cpu}%", style="green")

    if ram >= 80:
        console.print(f"RAM Usage: {ram}%", style="red")
    elif ram >= 50:
        console.print(f"RAM Usage: {ram}%", style="yellow")
    else:
        console.print(f"RAM Usage: {ram}%", style="green")
    for proc in psutil.process_iter(['name', 'memory_percent']):
        process.append(proc.info)
    large_proce = process[0]
    for proc in process:
        if proc["memory_percent"] > large_proce["memory_percent"]:
            biggest = proc
    print(large_proce)