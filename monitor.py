import psutil
from rich.console import Console
from rich.table import Table

console = Console()

while True:
    console.print("=== Live System Monitoring ===", style='bold cyan')
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    cores = psutil.cpu_percent(interval=1, percpu=True)
    process = []

    for i in psutil.process_iter(['pid','name', 'memory_percent']):
        process.append(i.info)
        
    top5 = []

    remaining = process.copy()
    for i in range(5):
        biggest = remaining[0]
        for p in remaining:
            if p['memory_percent'] > biggest['memory_percent']:
                biggest = p
        top5.append(biggest)
        remaining.remove(biggest)

    console.clear()
    console.print()

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
    console.print()

    core_table = Table(title="Per-Core Usage")
    core_table.add_column("Core")
    core_table.add_column("Usage %")

    core_number = 0
    for core in cores:
        core_table.add_row(f"Core {core_number}", f"{core}%")
        core_number = core_number + 1
    console.print(core_table)

    process_table = Table(title="Top 5 Processes")
    process_table.add_column("Name")
    process_table.add_column("Memory %")

    for p in top5:
        process_table.add_row(p['name'], f"{p['memory_percent']:.1f}%")
    console.print(process_table)



    kill_target = input("\nEnter process name to skill (or press enter to skip)")

    if kill_target != "":
        for p in process:
            if p['name'] == kill_target:
                psutil.Process(p['pid']).terminate()
                console.print(f"Killed {kill_target}", style='red')

    biggest = process[0]
    console.print("Top 5 Process: ")
    # for p in top5:
    #     console.print(f'{p['name']} - {p['memory_percent']:.1f}%')