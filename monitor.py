import psutil
from rich.console import Console

console = Console()

while True:
    console.print("=== Live System Monitoring ===", style='bold cyan')
    console.print()
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    process = []
    top5 = []
    console.clear()

    if cpu >= 80:
        console.print(f"CPU Usage : {cpu}", style="red")
    elif cpu >= 50:
        console.print(f"CPU Usage : {cpu}", style="yellow")
    else:
        console.print(f"CPU Usage : {cpu}", style="green")

    if ram >= 80:
        console.print(f"RAM Usage : {ram}", style="red")
    elif ram >= 50:
        console.print(f"RAM Usage : {ram}", style="yellow")
    else:
        console.print(f"RAM Usage : {ram}", style="green")
    for i in psutil.process_iter(['name', 'memory_percent']):
        process.append(i.info)

    biggest = process[0]
    remaining = process.copy()

    for i in range(5):
        biggest = remaining[0]
        for p in remaining:
            if p['memory_percent'] > biggest['memory_percent']:
                biggest = p
        top5.append(biggest)
        remaining.remove(biggest)
    console.print("Top 5 Process: ")
    for p in top5:
        console.print(f'{p['name']} - {p['memory_percent']:.1f}%')