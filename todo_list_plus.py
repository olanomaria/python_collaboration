#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:54:48 2024

@author: maritaolano
"""

def sort_by_priority_key(task):
    return task["priority"]

def sort_by_priority(tasks):
    return sorted(tasks, key=sort_by_priority_key, reverse=True)

def to_do_list():
    tasks = []

    def view_tasks():
        print("=========To-Do List=========")
        for i, task in enumerate(tasks, 1):
            print(f'{i}. Priority: {task["priority"]}, Task: {task["name"]}')

    def add_task():
        name = input("Add new task: ")
        priority = input("Enter priority (high/normal): ").lower()
        tasks.append({"name": name, "priority": priority})

    def mark_completed():
        view_tasks()
        mark_completed = int(input("Enter task you want to mark as completed: "))
        if 1 <= mark_completed <= len(tasks):
            del tasks[mark_completed - 1]
        else:
            print("Task DNE, try again!")

    while True:
        view_tasks()

        print("Options:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Sort by Priority")
        print("4. Exit")

        choice = input("Enter your choice 1-4: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            mark_completed()
        elif choice == "3":
            tasks = sort_by_priority(tasks)
        elif choice == "4":
            break
        else:
            print("Try again! Enter your choice 1-4")

to_do_list()
