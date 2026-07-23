# Terminal-Performance-Manager

A real-time, terminal-based system monitor designed to track CPU usage alongside command-line tools (like Claude Code) directly in your terminal.

## Why i am making this
When running terminal tools alongside system performance monitors (like Task Manager), switching focus often hides windows or clutter the workspace. Terminal-Performance-Manager solves this by giving a lightweight, inline performance readout directly in the terminal interface, avoiding window context switching and allowing remote tracking.

## What are the things i am adding and wanted to add
- Real-Time CPU Monitoring: Live updates of your system's CPU usage directly inside the terminal.
- Minimal Footprint: Fast and lightweight tracking logic written in Python/Node.
- Color-Coded Status Thresholds:
  -  **Normal (< 50%):** Standard output
  -  **Warning (50% - 75%):** Highlighted in Yellow
  -  **High (75% - 80%):** Highlighted in Orange
  -  **Critical (> 80%):** Highlighted in Red

## Tech Stack
- **Language:** Python / JavaScript / C++ *(Update to match your stack)*
- **Libraries:** psutil *(or whichever library you are using for system metrics)*

## 📦 How to Install & Run

### Prerequisites
Make sure you have installed:
- Python 3.x / Node.js
- Dependencies listed in `requirements.txt` / `package.json`

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/Sabih-sourcee/Terminal-Performance-Manager.git](https://github.com/Sabih-sourcee/Terminal-Performance-Manager.git)
   cd Terminal-Performance-Manager
