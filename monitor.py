import psutil
import os
import time
while True:
    cpu = psutil.cpu_percent(interval=1)
    if os.name == 'nt':
        clear_command = 'cls'
    else:
        clear_command = 'clear'
    os.system(clear_command)
    print(f'CPU Usage: {cpu}%')