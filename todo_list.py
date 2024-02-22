#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:15:59 2024

@author: maritaolano
"""
        
def to_do_list():
    tasks = []

    def view_tasks():
        print("=========To-Do List=========")
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')

    def add_task():
        new_task = input("Add new task: ")
        tasks.append(new_task)

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
        print("3. Exit")

        choice = input("Enter your choice 1-3: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            mark_completed()
        elif choice == "3":
            break
        else:
            print("Try again! Enter your choice 1-3")

to_do_list()
    
            
    