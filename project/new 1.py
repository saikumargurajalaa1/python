import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="employee",
            auth_plugin='123456'  )

        return conn
    except mysql.connector.Error as err:
        print(f"Database Connection Error: {err}")  # Critical: Prints to terminal
        messagebox.showerror("Database Error", f"Cannot connect to DB: {err}")
        return None



def register_employee():
    # Validation to make sure fields aren't empty
    emp_id = emp_id_entry.get().strip()
    emp_name = emp_name_entry.get().strip()

    if not emp_id or not emp_name:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO emp (id,name) VALUES (%s, %s)"


            try:
                formatted_id = int(emp_id)
            except ValueError:
                formatted_id = emp_id

            cursor.execute(query, (formatted_id, emp_name))
            conn.commit()

            messagebox.showinfo("Success", "Employee registered successfully")
            emp_id_entry.delete(0, tk.END)
            emp_name_entry.delete(0, tk.END)

        except mysql.connector.Error as err:
            print(f"SQL Execution Error: {err}")  # Prints to terminal
            messagebox.showerror("Registration Error", str(err))
        finally:
            cursor.close()
            conn.close()


def search_employee():
    emp_id = search_entry.get().strip()
    if not emp_id:
        messagebox.showwarning("Input Error", "Please enter an Employee ID to search.")
        return

    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT id, name FROM emp WHERE id = %s"

            cursor.execute(query, (emp_id,))
            result = cursor.fetchall()

            # Clear old search results first
            for item in tree.get_children():
                tree.delete(item)

            if result:
                for row in result:
                    tree.insert("", tk.END, values=row)
            else:
                messagebox.showinfo("No Result", "No employee found with the given ID")
        except mysql.connector.Error as err:
            print(f"Search Error: {err}")  # Prints to terminal
            messagebox.showerror("Search Error", str(err))
        finally:
            cursor.close()
            conn.close()


root = tk.Tk()
root.title("Employee Registration")
root.geometry("400x400")

emp_id_label = tk.Label(root, text="Employee ID:")
emp_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
emp_id_entry = tk.Entry(root)
emp_id_entry.grid(row=0, column=1, padx=5, pady=5)

emp_name_label = tk.Label(root, text="Employee Name:")
emp_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
emp_name_entry = tk.Entry(root)
emp_name_entry.grid(row=1, column=1, padx=5, pady=5)

register_button = tk.Button(root, text="Register", command=register_employee)
register_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

search_label = tk.Label(root, text="Search by Employee ID:")
search_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
search_entry = tk.Entry(root)
search_entry.grid(row=3, column=1, padx=5, pady=5)

search_button = tk.Button(root, text="Search", command=search_employee)
search_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

tree = ttk.Treeview(root, columns=("Employee ID", "Employee Name"), show="headings")
tree.column("Employee ID", width=150, anchor="center")
tree.column("Employee Name", width=200, anchor="center")
tree.heading("Employee ID", text="Employee ID")
tree.heading("Employee Name", text="Employee Name")
tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()