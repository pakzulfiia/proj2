# Create- Read - Update -Delete

tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL
    )
"""

# create
insert_task = "INSERT INTO tasks(task) VALUES (?)"

# read 
selct_task = 'SELECT * FROM tasks' 

# update + where
update_task = 'UPDATE tasks SET task = ? WHERE id = ?'

# delete
delete_task = "DELETE FROM tasks WHERE id = ?"