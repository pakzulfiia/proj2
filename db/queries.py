# Create- Read - Update -Delete

tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        complited INTEGER DEFAULT 0
    )
"""

# create
insert_task = "INSERT INTO tasks(task) VALUES (?)"

# read 
select_task = 'SELECT * FROM tasks'

select_task_complited= 'SELECT id, task, complited FROM tasks WHERE complited = 1' 

select_task_uncomplited = 'SELECT * FROM tasks WHERE complited = 0' 


# update + where
update_task = 'UPDATE tasks SET task = ? WHERE id = ?'

update_complited = "UPDATE tasks SET complited = ? WHERE id = ?"

# delete
delete_task = "DELETE FROM tasks WHERE id = ?"

delete_complited_task = "DELETE FROM tasks WHERE complited = 1"