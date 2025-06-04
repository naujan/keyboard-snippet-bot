# ⚡ Keyboard Snippet Bot

A **minimal** and **lightning-fast** Python tool that automatically replaces typed commands with predefined text or code snippets.  
Perfect for quickly inserting reusable content in **terminals**, **editors**, **browsers**, and more – anywhere your keyboard works.

## ✨ Features

- 💡 Detects custom trigger commands as you type
- 🔁 Replaces commands with snippet content instantly
- 📂 Snippets are stored in `snippet.txt`
- ⚙️ Fully configurable in `main.py`
- 🛑 Press `ESC` to safely stop the script
- 🐍 Lightweight – just Python + `pynput`, no bloat

## 🚀 How to Use

1. **Set your custom command**  
   At the top of `main.py`, set the `command` value to something unique (e.g., `/code`, `$insert`, etc.)

2. **Write your snippet**  
   Edit the `snippet.txt` file – whatever you put in here will be inserted when you type the command.

3. **Run the bot**  
   ```bash
   pip install pynput
   python main.py
