import tkinter as tk

def submit_info():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()

    message_label.config(text=f"Name: {name}\nAge: {age}\nEmail: {email}")

window = tk.Tk()
window.title("Registration Form")

name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack() 

email_label = tk.Label(window, text="Email:")
email_label.pack()
email_entry = tk.Entry(window)
email_entry.pack()

submit_button = tk.Button(window, text="SUBMIT", command=submit_info)
submit_button.pack()

message_label = tk.Label(window, text="")
message_label.pack()

window.mainloop()
