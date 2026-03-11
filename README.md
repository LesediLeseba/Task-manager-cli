# Task Tracker CLI

https://roadmap.sh/projects/task-tracker

A simple Command Line Interface (CLI) application built with Python to manage and track tasks.  
This tool allows you to add, update, delete, and track the status of tasks directly from your terminal.

The application stores tasks in a JSON file in the current directory and uses only Python’s standard library.

---

## 🚀 Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as:
  - `todo`
  - `in-progress`
  - `done`
- List:
  - All tasks
  - Tasks by status (`todo`, `in-progress`, `done`)
- Automatically creates a `tasks.json` file if it does not exist
- Graceful error handling
- No external dependencies

---

## 📁 Project Structure
    task_manager_cli/
    │
    ├── task_cli.py
    └── tasks.json (created automatically)


---

## 🧰 Requirements

- Python 3.x
- No external libraries required

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/LesediLeseba/Task-manager-cli.git
cd task-cli

python --version
