import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


# Database connection function
def connect_db():
    try:

        #1 - get connection
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="employee"
        )
        return conn

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))


                    # Function to insert data into database

def register_employee():

    conn = connect_db()
    if conn:

        #2 - Statement
        cursor = conn.cursor()

                        #read data into var to pass into sql

        emp_id = emp_id_entry.get() # g() f  gets data from entry box or text box given by user
        emp_name = emp_name_entry.get()
        emp_dep = emp_dep_entry.get()

                            #INSERT data

        query = "INSERT INTO employee.emp (id, name, department) VALUES (%s, %s, %s);"

        try:

            cursor.execute(query, (emp_id, emp_name, emp_dep))
            conn.commit()

            messagebox.showinfo("Success", "Employee registered successfully")


        except mysql.connector.Error as err:
            messagebox.showerror("Registration Error", str(err))


        finally:
            cursor.close()
            conn.close()



                                # Create GUI
root = tk.Tk()


root.title("Employee Registration")

# Employee ID label and entry
emp_id_label = tk.Label(root, text="Employee ID:")
emp_id_label.grid(row=0, column=0, padx=5, pady=5)

emp_id_entry = tk.Entry(root)
emp_id_entry.grid(row=0, column=1, padx=5, pady=5)


# Employee Name label and entry
emp_name_label = tk.Label(root, text="Employee Name:")
emp_name_label.grid(row=1, column=0, padx=5, pady=5)
emp_name_entry = tk.Entry(root)
emp_name_entry.grid(row=1, column=1, padx=5, pady=5)

#Emp department
emp_dep_label = tk.Label(root, text="Department:")
emp_dep_label.grid(row=2, column=0, padx=5, pady=5)
emp_dep_entry = tk.Entry(root)
emp_dep_entry.grid(row=2, column=1, padx=5, pady=5)


# Register button
register_button = tk.Button(root, text="Register", command=register_employee)
register_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()  # run
