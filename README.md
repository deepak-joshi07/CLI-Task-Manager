This is a simple task manager that runs in the command line and is built using Python. The idea is to make it easier to manage daily tasks without relying on messy lists or notes.

At the beginning, using a normal list to track tasks feels fine. But once tasks start increasing, things get difficult. You have to scroll through everything to find one task, there’s no proper way to search or filter, and updating something becomes annoying.

This project tries to fix that by giving a structured way to manage tasks directly from the terminal.

What it does

You can add tasks, update them, delete them, search for specific ones, and mark them as completed. Everything is stored in a JSON file, so your data stays saved even after you close the program.

Tasks are sorted by priority, and you can quickly find something using keywords instead of manually scanning through a long list.

How to use it

You run the program from the command line and use different commands depending on what you want to do.

For example:

Add a task
python -m task_manager.cli add --name "Buy RAM" --priority 1 --category tech --due_date 2026-04-25

List all tasks
python -m task_manager.cli list

Search for a task
python -m task_manager.cli search --keyword "ram"

Delete a task
python -m task_manager.cli delete --id <task_id>

Mark task as complete
python -m task_manager.cli complete --id <task_id>

Why this project

The goal wasn’t to build something complex, but something practical. A small tool that actually solves the problem of managing multiple tasks without wasting time.

What I learned

I learned how to structure a project properly instead of putting everything in one file. I also got better at separating logic from interface, handling data with JSON, and building a CLI using argparse.