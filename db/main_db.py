# руляционная и нереляционная

import sqlite3
from config import path_db
from db import queries


def init_db():
    conn = sqlite3.connect(path_db)   # соединение к бд
    cursor = conn.cursor()   # исполнитель который относит запросы к бд
    cursor.execute(queries.tasks_table)
    # cursor.execute('SELECT * FROM tasks') # принимает запрос в видде стринг
    conn.commit()
    conn.close()


def add_task(task):
    conn = sqlite3.connect(path_db)  
    cursor = conn.cursor()  
    cursor.execute(queries.insert_task, (task, ))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id


def update_task(task_id, new_task):
    conn = sqlite3.connect(path_db)  
    cursor = conn.cursor()  
    cursor.execute(queries.update_task, (new_task, task_id))
    conn.commit()

    conn.close()
    return task_id


def delete_task(task_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.delete_task, (task_id, ))
    conn.commit()

    conn.close()