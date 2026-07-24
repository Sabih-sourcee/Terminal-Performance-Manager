# Terminal-Performance-Manager

A real-time CPU monitor that lives in your terminal instead of stealing your window focus.

## Why

I kept alt-tabbing to Task Manager while running Claude Code in the terminal, and every switch broke my flow and cluttered the desktop. This just prints CPU usage inline, so I never have to leave the terminal to check if something's about to choke.

## Features

- Live CPU usage, updates in place, no flicker
- Small footprint — this is a monitor, not a resource hog itself
- Color-coded thresholds so you can tell at a glance:
  - under 50% — green
  - 50–75% — yellow
  - over 80% — red

## Stack
Python, using `psutil` for the metrics.

## Install

```bash
git clone https://github.com/Sabih-sourcee/Terminal-Performance-Manager.git
cd Terminal-Performance-Manager
pip install rich; pip install psutil
```

Run:

```bash
python monitor.py
```
