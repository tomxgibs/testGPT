#!/usr/bin/env python3
import json
import sys
from pathlib import Path

TODO_FILE = Path('todo.json')

def load_tasks():
    if TODO_FILE.exists():
        try:
            with TODO_FILE.open('r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_tasks(tasks):
    with TODO_FILE.open('w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2)

def list_tasks(tasks):
    if not tasks:
        print('Keine Aufgaben.')
        return
    for idx, task in enumerate(tasks, 1):
        status = 'x' if task.get('done') else ' '
        print(f"{idx}. [{status}] {task.get('text')}")

def add_task(tasks, text):
    tasks.append({'text': text, 'done': False})
    save_tasks(tasks)
    print('Aufgabe hinzugefügt.')

def complete_task(tasks, index):
    try:
        tasks[index]['done'] = True
        save_tasks(tasks)
        print('Aufgabe abgeschlossen.')
    except IndexError:
        print('Ungültiger Index')

def remove_task(tasks, index):
    try:
        tasks.pop(index)
        save_tasks(tasks)
        print('Aufgabe entfernt.')
    except IndexError:
        print('Ungültiger Index')

def print_help():
    print('Verwendung:')
    print('  python todo.py list')
    print('  python todo.py add "Beschreibung"')
    print('  python todo.py complete INDEX')
    print('  python todo.py remove INDEX')


def main():
    tasks = load_tasks()
    if len(sys.argv) < 2:
        print_help()
        return
    cmd = sys.argv[1]
    if cmd == 'list':
        list_tasks(tasks)
    elif cmd == 'add' and len(sys.argv) > 2:
        add_task(tasks, ' '.join(sys.argv[2:]))
    elif cmd == 'complete' and len(sys.argv) > 2:
        if sys.argv[2].isdigit():
            complete_task(tasks, int(sys.argv[2]) - 1)
        else:
            print('Bitte eine Zahl für INDEX angeben.')
    elif cmd == 'remove' and len(sys.argv) > 2:
        if sys.argv[2].isdigit():
            remove_task(tasks, int(sys.argv[2]) - 1)
        else:
            print('Bitte eine Zahl für INDEX angeben.')
    else:
        print_help()

if __name__ == '__main__':
    main()
