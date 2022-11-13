from criticalpath import Node
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np

def load_tasks(q_tasks):
    tasks = []
    for i in range(q_tasks):
        task_name = str(input('Ingresar Nombre de actividad: '))
        task_duration = int(input('Ingresar duración de actividad: '))
        tasks.append((task_name,{"duration": task_duration}))
    return tasks

def load_tasks_dependencies():
    dependecies = []
    while(True):
        prev_task = str(input('Ingresar Actividad Antecesora: '))
        if(prev_task != 'x'):
            next_task = str(input('Ingresar Actividad Predecesora: '))
            dependecies.append((prev_task, next_task))
        else:
            break
    return dependecies

def CPM(project, tasks, dependecies):
    # load tasks and dependencies at the project
    for i in tasks:
        project.add(Node(i[0], duration=i[1]["duration"]))
    for j in dependecies:
        project.link(j[0],j[1])
    project.update_all()
    return project

def main():
    project_name = str(input('Ingresar Nombre del Proyecto: '))
    q_tasks = int(input('Ingresar Cantidad de Tareas: '))
    project = Node(project_name)

    print('\nCargar Tareas:')
    tasks = load_tasks(q_tasks)
    print('\nCargar Dependencias:')
    dependecies = load_tasks_dependencies()

    project = CPM(project, tasks, dependecies)
    print('\nResultado: ')
    print(project.get_critical_path())
    print('\nDuración: ')
    print(project.duration)

main()