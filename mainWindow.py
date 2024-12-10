import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


field_names = ["Name"] + ["Course"] + [f"Hole {i}" for i in range(1, 19)]
min_height = len(field_names) * 50 + 100
# Function to initialize the SQLite database
def initialize_database():
    conn = sqlite3.connect("data_store.db")
    cursor = conn.cursor()
    # Create a table if it doesn't already exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            course TEXT NOT NULL,
            hole1 TEXT,
            hole2 TEXT,
            hole3 TEXT,
            hole4 TEXT,
            hole5 TEXT,
            hole6 TEXT,
            hole7 TEXT,
            hole8 TEXT,
            hole9 TEXT,
            hole10 TEXT,
            hole11 TEXT,
            hole12 TEXT,
            hole13 TEXT,
            hole14 TEXT,
            hole15 TEXT,
            hole16 TEXT,
            hole17 TEXT,
            hole18 TEXT
        )
    """)
    conn.commit()
    conn.close()

# Function to insert data into the database
def insert_data(data):
    conn = sqlite3.connect("data_store.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO entries (name, course, hole1, hole2, hole3, hole4, hole5, hole6, hole7, hole8, hole9, hole10, hole11, hole12, hole13, hole14, hole15, hole16, hole17, hole18) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (data["Name"], data["Course"], data.get("Hole 1"), data.get("Hole 2"), data.get("Hole 3"), data.get("Hole 4"), data.get("Hole 5"), data.get("Hole 6"), data.get("Hole 7"), data.get("Hole 8"), data.get("Hole 9"), data.get("Hole 10"), data.get("Hole 11"), data.get("Hole 12"), data.get("Hole 13"), data.get("Hole 14"), data.get("Hole 15"), data.get("Hole 16"), data.get("Hole 17"), data.get("Hole 18")))
    conn.commit()
    conn.close()

# Function to retrieve data from the database
def fetch_data():
    conn = sqlite3.connect("data_store.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entries")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to handle form submission
def submit_form():
    data = {}
    for field, entry in entry_fields.items():
        value = entry.get()
        if not value:  # Name is a required field
            messagebox.showerror("Error", f"{field} is required!")
            return
        data[field] = value

    insert_data(data)
    messagebox.showinfo("Success", "Data saved successfully!")

    # Clear the input fields
    for entry in entry_fields.values():
        entry.delete(0, tk.END)

# Function to display saved records
def view_records():
    records = fetch_data()

    # Create a new window to display records
    records_window = tk.Toplevel(app)
    records_window.title("Saved Records")
    records_window.minsize(min_height, 600)

    tree = ttk.Treeview(records_window, columns=("ID", "Name", "Course", "Hole 1", "Hole 2", "Hole 3", "Hole 4", "Hole 5", "Hole 6", "Hole 7", "Hole 8", "Hole 9", "Hole 10", "Hole 11", "Hole 12", "Hole 13", "Hole 14", "Hole 15", "Hole 16", "Hole 17", "Hole 18"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Course", text="Name")
    tree.heading("Hole 1", text="Hole 1")
    tree.heading("Hole 2", text="Hole 2")
    tree.heading("Hole 3", text="Hole 3")
    tree.heading("Hole 4", text="Hole 4")
    tree.heading("Hole 5", text="Hole 5")
    tree.heading("Hole 6", text="Hole 6")
    tree.heading("Hole 7", text="Hole 7")
    tree.heading("Hole 8", text="Hole 8")
    tree.heading("Hole 9", text="Hole 9")
    tree.heading("Hole 10", text="Hole 10")
    tree.heading("Hole 11", text="Hole 11")
    tree.heading("Hole 12", text="Hole 12")
    tree.heading("Hole 13", text="Hole 13")
    tree.heading("Hole 14", text="Hole 14")
    tree.heading("Hole 15", text="Hole 15")
    tree.heading("Hole 16", text="Hole 16")
    tree.heading("Hole 17", text="Hole 17")
    tree.heading("Hole 18", text="Hole 18")

    tree.column("ID", width=50)
    tree.column("Name", width=150)
    tree.column("Course", width=150)
    tree.column("Hole 1", width=50)
    tree.column("Hole 2", width=50)
    tree.column("Hole 3", width=50)
    tree.column("Hole 4", width=50)
    tree.column("Hole 5", width=50)
    tree.column("Hole 6", width=50)
    tree.column("Hole 7", width=50)
    tree.column("Hole 8", width=50)
    tree.column("Hole 9", width=50)
    tree.column("Hole 10", width=50)
    tree.column("Hole 11", width=50)
    tree.column("Hole 12", width=50)
    tree.column("Hole 13", width=50)
    tree.column("Hole 14", width=50)
    tree.column("Hole 15", width=50)
    tree.column("Hole 16", width=50)
    tree.column("Hole 17", width=50)
    tree.column("Hole 18", width=50)

    for record in records:
        tree.insert("", tk.END, values=record)

    tree.pack(fill=tk.BOTH, expand=True)

# Initialize the database
initialize_database()

# Create the GUI application window
app = tk.Tk()
app.title("Golf Score Entry Form")

# Set default window size for the main app
app.geometry("800x600")

# Configure grid layout for responsiveness
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=2)

# Dictionary to store the Entry widgets
entry_fields = {}

# Create input fields dynamically based on the list
for i, field in enumerate(field_names):
    label = tk.Label(app, text=f"{field}:")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

    entry = tk.Entry(app)
    entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")

    # Store the Entry widget in the dictionary
    entry_fields[field] = entry

# Adjust window size dynamically to fit all widgets
app.minsize(min_height, 700)

# Create submit button
submit_button = tk.Button(app, text="Submit", command=submit_form)
submit_button.grid(row=len(field_names), column=0, padx=10, pady=10, sticky="ew")

# Create view records button
view_button = tk.Button(app, text="View Records", command=view_records)
view_button.grid(row=len(field_names), column=1, padx=10, pady=10, sticky="ew")

# Start the application
app.mainloop()