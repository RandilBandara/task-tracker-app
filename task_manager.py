import sqlite3

def create_table():
    # Connect to SQLite DB (file 'tasks.db' will be created automatically)
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    # Create table 'tasks' if it doesn't exist yet
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL DEFAULT 'pending'
        )
    ''')

    # Save changes and close connection
    conn.commit()
    conn.close()
    print("Database and table created!")

# Run the function to create the table
create_table()
import sqlite3

def connect_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    return conn

def add_task(conn, title, description):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (title, description))
    conn.commit()
    print("Task added!")

def view_tasks(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    rows = cursor.fetchall()
    if rows:
        print("\nYour Tasks:")
        for row in rows:
            print(f"ID: {row[0]}, Title: {row[1]}, Description: {row[2]}")
    else:
        print("No tasks found.")

def update_task(conn, task_id, new_title, new_description):
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET title = ?, description = ? WHERE id = ?', (new_title, new_description, task_id))
    if cursor.rowcount == 0:
        print("Task ID not found.")
    else:
        conn.commit()
        print("Task updated!")

def delete_task(conn, task_id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    if cursor.rowcount == 0:
        print("Task ID not found.")
    else:
        conn.commit()
        print("Task deleted!")

def main():
    conn = connect_db()
    while True:
        print('''
        Task Manager:
        1. Add Task
        2. View Tasks
        3. Update Task
        4. Delete Task
        5. Exit
        ''')
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(conn, title, description)

        elif choice == '2':
            view_tasks(conn)

        elif choice == '3':
            task_id = input("Enter task ID to update: ")
            new_title = input("Enter new title: ")
            new_description = input("Enter new description: ")
            update_task(conn, task_id, new_title, new_description)

        elif choice == '4':
            task_id = input("Enter task ID to delete: ")
            delete_task(conn, task_id)

        elif choice == '5':
            print("Goodbye!")
            conn.close()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

