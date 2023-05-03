import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import subprocess
import os
import sys
import re

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[('JSON Files', '*.json')])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filepath)

def execute_command():
    filepath = file_entry.get()
    password = 'babb4a9f774ab853c96c2d653dfe544a'
    iv = '00000000000000000000000000000000'
    
    openssl_path = get_openssl_path()
    if not openssl_path:
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "OpenSSL executable not found.")
        return
    
    command = f'"{openssl_path}" aes-128-cbc -d -K {password} -iv {iv} -in "{filepath}"'
    
    try:
        result = subprocess.check_output(command, shell=True)
        decoded_result = result.decode('utf-8-sig', errors='replace')
        
        user_matches = re.findall(r'"user"\s*:\s*"([^"]+)"', decoded_result)
        password_matches = re.findall(r'"password"\s*:\s*"([^"]+)"', decoded_result)
        
        result_text.delete('1.0', tk.END)
        
        if user_matches and password_matches:
            for user, password in zip(user_matches, password_matches):
                result_text.insert(tk.END, f"User: {user}\nPassword: {password}\n{'-' * 20}\n")
        else:
            result_text.insert(tk.END, "No user and password found.")
            
    except subprocess.CalledProcessError:
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "Error occurred while executing the command.")

def reset_selection():
    file_entry.delete(0, tk.END)
    result_text.delete('1.0', tk.END)



def get_openssl_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    if sys.platform.startswith('win'):
        openssl_exe = 'openssl.exe'
    else:
        openssl_exe = 'openssl'
    
    openssl_path = os.path.join(script_dir, openssl_exe)
    if os.path.isfile(openssl_path):
        return openssl_path
    
    return None

# main window
window = tk.Tk()
window.title("Gabe's DBeaver Password Magician v0.1")

script_path = os.path.dirname(os.path.abspath(__file__))
icon_file = os.path.join(script_path, "icon.ico")
window.iconbitmap(icon_file)

title_label = tk.Label(window, text='Gabe DBeaver Password Magician', justify=tk.CENTER, font=('Graffiti', 16,'bold'))
title_label.pack(pady=10)

file_frame = tk.Frame(window)
file_frame.pack(pady=20)

file_label = tk.Label(file_frame, text="Select File:")
file_label.grid(row=0, column=0)

file_entry = tk.Entry(file_frame, width=40)
file_entry.grid(row=0, column=1, padx=10)

file_button = tk.Button(file_frame, text="Browse", command=open_file)
file_button.grid(row=0, column=2)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

execute_button = tk.Button(button_frame, text="Execute Command", command=execute_command)
execute_button.grid(row=0, column=0, padx=5)

reset_button = tk.Button(button_frame, text="Reset Selection", command=reset_selection)
reset_button.grid(row=0, column=1, padx=5)

result_frame = tk.Frame(window)
result_frame.pack(pady=20)

result_label = tk.Label(result_frame, text="Decrypted Result:")
result_label.pack(side=tk.LEFT)

image = Image.open(os.path.join(script_path, "magicbeaver.png"))
image = image.resize((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(result_frame, image=photo)
image_label.image = photo
image_label.pack(side=tk.RIGHT, padx=10)

result_text = tk.Text(result_frame, width=50, height=10)
result_text.pack()

# Run the GUI
window.mainloop()
