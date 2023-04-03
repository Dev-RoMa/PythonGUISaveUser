import tkinter as tk

def save_name(name):
    # Save the name to a file
    with open("name.txt", "w") as f:
        f.write(name)
        print("Name saved to file.")

def load_name():
    # Load the name from the file
    with open("name.txt", "r") as f:
        name = f.read()
        print(f"Name loaded from file: {name}")
        return name

def show_menu():
    # Create the main window
    root = tk.Tk()
    root.title("Menu")

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the window width and height
    window_width = 300
    window_height = 200

    # Calculate the x and y positions for centering the window
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Set the window size and position
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create the label
    label = tk.Label(root, text="Select an option:")
    label.pack(pady=10)

    # Create the buttons
    button1 = tk.Button(root, text="Save name", command=save_name_window)
    button1.pack(pady=5)

    button2 = tk.Button(root, text="Load name", command=load_name_window)
    button2.pack(pady=5)

    button3 = tk.Button(root, text="Exit program", command=root.quit)
    button3.pack(pady=5)

    # Run the main event loop
    root.mainloop()

def save_name_window():
    # Create the save name window
    save_window = tk.Toplevel()
    save_window.title("Save name")

    # Center the window on the screen
    screen_width = save_window.winfo_screenwidth()
    screen_height = save_window.winfo_screenheight()
    window_width = 300
    window_height = 150
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    save_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create the label and entry widget
    label = tk.Label(save_window, text="Enter your name:")
    label.pack(pady=5)

    entry = tk.Entry(save_window)
    entry.pack(pady=5)

    def save_and_close():
        save_name(entry.get())
        popup = tk.Toplevel()
        popup.title("Name saved")
        popup.geometry("200x100")

        # Center the pop-up window on the screen
        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()
        window_width = popup.winfo_reqwidth()
        window_height = popup.winfo_reqheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        popup.geometry(f"+{x}+{y}")

        popup_label = tk.Label(popup, text="Name saved!")
        popup_label.pack(pady=10)
        popup_button = tk.Button(popup, text="OK", command=popup.destroy)
        popup_button.pack(pady=5)
        save_window.destroy()

        
    button = tk.Button(save_window, text="Save", command=save_and_close)
    button.pack(pady=5)


def load_name_window():
    # Create the load name window
    load_window = tk.Toplevel()
    load_window.title("Load name")

    # Center the window on the screen
    screen_width = load_window.winfo_screenwidth()
    screen_height = load_window.winfo_screenheight()
    window_width = 300
    window_height = 150
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    load_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Load the name from the file
    try:
        with open("name.txt", "r") as f:
            name = f.readline().strip()
    except FileNotFoundError:
        name = None

    if name:
        name_label = tk.Label(load_window, text=f"Name loaded from file: {name}")
        name_label.pack(pady=10)
    else:
        name_label = tk.Label(load_window, text="No name has been saved yet.")
        name_label.pack(pady=10)

    # Create the close button
    button = tk.Button(load_window, text="Close", command=load_window.destroy)
    button.pack(pady=5)



# Initialize the name variable
name = ""

# Show the menu
show_menu()