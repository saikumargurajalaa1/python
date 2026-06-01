import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


# Database connection function
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="employee"
        )
        return conn

    except mysql.connector.Error as err:
        print(f"Database Connection Error: {err}")
        messagebox.showerror("Database Error", f"Cannot connect to DB: {err}")
        return None


# Function to insert data into database
def register_employee():

    emp_id = emp_id_entry.get().strip()
    emp_name = emp_name_entry.get().strip()
    department = dept_entry.get().strip()
    gender = gender_var.get()
    address = address_entry.get().strip()
    qualification = qualification_entry.get().strip()
    mobile = mobile_entry.get().strip()
    url = url_entry.get().strip()

    if not emp_id or not emp_name or not department or not gender or not address or not qualification or not mobile or not url:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = "INSERT INTO emp(id,name, department, Gender, Address,qualification,mobile,URL)VALUES (%s, %s, %s, %s, %s,%s,%s,%s)"

            try:
                formatted_id = int(emp_id)
            except ValueError:
                formatted_id = emp_id

            cursor.execute(
                query,
                (formatted_id, emp_name, department, gender, address,qualification,mobile,url)
            )

            conn.commit()

            messagebox.showinfo("Success", "Employee registered successfully")

            emp_id_entry.delete(0, tk.END)
            emp_name_entry.delete(0, tk.END)
            dept_entry.delete(0, tk.END)
            address_entry.delete(0, tk.END)
            gender_var.set("")
            qualification_entry.delete(0, tk.END)
            mobile_entry.delete(0, tk.END)
            url_entry.delete(0, tk.END)

        except mysql.connector.Error as err:
            print(f"SQL Execution Error: {err}")
            messagebox.showerror("Registration Error", str(err))

        finally:
            cursor.close()
            conn.close()


# Function to search data from database
def search_employee():

    emp_id = search_entry.get().strip()

    if not emp_id:
        messagebox.showwarning(
            "Input Error",
            "Please enter an Employee ID to search."
        )
        return

    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = "SELECT id,name,department,gender,Address,qualification,mobile,URL FROM emp WHERE id = %s"

            cursor.execute(query, (emp_id,))
            result = cursor.fetchall()

            # Clear old records
            for item in tree.get_children():
                tree.delete(item)

            if result:
                for row in result:
                    tree.insert("", tk.END, values=row)
            else:
                messagebox.showinfo(
                    "No Result",
                    "No employee found with the given ID"
                )

        except mysql.connector.Error as err:
            print(f"Search Error: {err}")
            messagebox.showerror("Search Error", str(err))

        finally:
            cursor.close()
            conn.close()


# ================= GUI =================

root = tk.Tk()
root.title("Employee Registration System")
root.geometry("1200x600")


# Employee ID
emp_id_label = tk.Label(root, text=" ID:")
emp_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

emp_id_entry = tk.Entry(root)
emp_id_entry.grid(row=0, column=1, padx=5, pady=5)


# Employee Name
emp_name_label = tk.Label(root, text="Employee Name:")
emp_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

emp_name_entry = tk.Entry(root)
emp_name_entry.grid(row=1, column=1, padx=5, pady=5)


# Department
dept_label = tk.Label(root, text="Department:")
dept_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

dept_entry = tk.Entry(root)
dept_entry.grid(row=2, column=1, padx=5, pady=5)


# Gender
gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

gender_var = tk.StringVar()

male_radio = tk.Radiobutton(root,text="Male",variable=gender_var,value="Male")
male_radio.grid(row=3, column=1, sticky="w")

female_radio = tk.Radiobutton(root,text="Female",variable=gender_var,value="Female")
female_radio.grid(row=3, column=1, padx=80, sticky="w")


# Address
address_label = tk.Label(root, text="Address:")
address_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

address_entry = tk.Entry(root, width=30)
address_entry.grid(row=4, column=1, padx=5, pady=5)

# Qualification
qualification_label = tk.Label(root, text="Qualification:")
qualification_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

qualification_entry = tk.Entry(root)
qualification_entry.grid(row=5, column=1, padx=5, pady=5)

# Mobile
mobile_label = tk.Label(root, text="Mobile:")
mobile_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

mobile_entry = tk.Entry(root)
mobile_entry.grid(row=6, column=1, padx=5, pady=5)

# URL
url_label = tk.Label(root, text="URL:")
url_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")

url_entry = tk.Entry(root, width=40)
url_entry.grid(row=7, column=1, padx=5, pady=5)


# Register Button
register_button = tk.Button(root,text="Register",command=register_employee)
register_button.grid(row=8,column=0,columnspan=2,padx=5,pady=10)


# Search Section
search_label = tk.Label(root,text="Search by Employee ID:")
search_label.grid(row=9,column=0,padx=5,pady=5,sticky="w")

search_entry = tk.Entry(root)
search_entry.grid(row=9,column=1,padx=5,pady=5)

search_button = tk.Button(root,text="Search",command=search_employee)
search_button.grid(row=10,column=0,columnspan=2,padx=5,pady=10)


# Treeview
tree = ttk.Treeview(root,columns=("Employee ID","Employee Name","Department","Gender","Address","Qualification",
    "Mobile","URL"),show="headings")

tree.heading("Employee ID", text="Employee ID")
tree.heading("Employee Name", text="Employee Name")
tree.heading("Department", text="Department")
tree.heading("Gender", text="Gender")
tree.heading("Address", text="Address")
tree.heading("Qualification", text="Qualification")
tree.heading("Mobile", text="Mobile")
tree.heading("URL", text="URL")


tree.column("Employee ID", width=100, anchor="center")
tree.column("Employee Name", width=150, anchor="center")
tree.column("Department", width=120, anchor="center")
tree.column("Gender", width=100, anchor="center")
tree.column("Address", width=250, anchor="center")
tree.column("Qualification", width=120, anchor="center")
tree.column("Mobile", width=120, anchor="center")
tree.column("URL", width=120, anchor="center")

tree.grid(row=11,column=0,columnspan=2,padx=10,pady=10)

root.mainloop()