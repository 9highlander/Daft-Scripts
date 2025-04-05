import tkinter as tk
from tkinter import messagebox, filedialog
import json

def run_input_form():
    # Variables to store user input
    result = {
        "address": "",
        "min_price": "",
        "max_price": "",
        "beds_number": "",
        "max_distance":"",
        "date": "",
        "use_google_maps_api": "",
        "use_actual_date": "",
        "open_browser": "",
    }


    def submit():
        result["address"] = entry_address.get()
        result["min_price"] = entry_min_price.get()
        result["max_price"] = entry_max_price.get()
        result["beds_number"] = entry_beds_number.get()
        result["max_distance"] = entry_max_distance.get()
        result["date"] = entry_date.get()
        result["use_google_maps_api"] = google_maps_var.get()
        result["use_actual_date"] = actual_date_var.get()
        result["open_browser"] = open_browser_var.get()

        if (    result["address"]      
            and result["min_price"]    and result["min_price"].isnumeric 
            and result["max_price"]    and result["max_price"].isnumeric 
            and result["beds_number"]  and result['beds_number'].isnumeric
            and result["max_distance"] and result["max_distance"].isnumeric
            and result["date"] 
            and result["use_google_maps_api"]
            and result["use_actual_date"]
            and result["open_browser"] ):
             
            messagebox.showinfo("Success", "Form submitted successfully!")
            root.quit()  # This will stop the mainloop
            root.destroy()  # This will close the window

        else:
           messagebox.showerror("Invalid input",
                                 "You must correctly compile all fields")
           

    def save_to_file():
        data = {
            "address": entry_address.get(),
            "min_price": entry_min_price.get(),
            "max_price": entry_max_price.get(),
            "beds_number": entry_beds_number.get(),
            "max_distance": entry_max_distance.get(),
            "date": entry_date.get(),
            "use_google_maps_api": google_maps_var.get(),
            "use_actual_date": actual_date_var.get(),
            "open_browser": open_browser_var.get(),
        }
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w') as file:
                json.dump(data, file)
            #messagebox.showinfo("Success", "Data saved to file successfully!")

    def load_from_file():
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r') as file:
                data = json.load(file)
            entry_address.delete(0, tk.END)
            entry_address.insert(0, data.get("address", ""))
            entry_min_price.delete(0, tk.END)
            entry_min_price.insert(0, data.get("min_price", ""))
            entry_max_price.delete(0, tk.END)
            entry_max_price.insert(0, data.get("max_price", ""))
            entry_beds_number.delete(0, tk.END)
            entry_beds_number.insert(0, data.get("beds_number", ""))
            entry_max_distance.delete(0, tk.END)
            entry_max_distance.insert(0, data.get("max_distance", ""))
            entry_date.delete(0, tk.END)
            entry_date.insert(0, data.get("date", ""))
            google_maps_var.set(data.get("use_google_maps_api", "No"))
            actual_date_var.set(data.get("use_actual_date", "No"))
            open_browser_var.set(data.get("open_browser", "No"))
            #messagebox.showinfo("Success", "Data loaded from file successfully!")

    # Create the main window
    root = tk.Tk()
    root.title("Property Search Form")
    root.geometry("365x310")

    # Create and position the widgets
    tk.Label(root, text="Address:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entry_address = tk.Entry(root)
    entry_address.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Min Price:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entry_min_price = tk.Entry(root)
    entry_min_price.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text="Max Price:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    entry_max_price = tk.Entry(root)
    entry_max_price.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(root, text="Beds Number:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
    entry_beds_number = tk.Entry(root)
    entry_beds_number.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(root, text="Max distance:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
    entry_max_distance = tk.Entry(root)
    entry_max_distance.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(root, text="Date:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
    entry_date = tk.Entry(root)
    entry_date.grid(row=5, column=1, padx=5, pady=5)

    # Google Maps API call option
    tk.Label(root, text="Google Maps API call:").grid(row=6, column=0, sticky="e", padx=5, pady=5)
    google_maps_var = tk.StringVar(value="No")  # Default to "No"
    tk.Radiobutton(root, text="Yes", variable=google_maps_var, value="Yes").grid(row=6, column=1, sticky="w", padx=5, pady=2)
    tk.Radiobutton(root, text="No", variable=google_maps_var, value="No").grid(row=6, column=1, sticky="e", padx=5, pady=2)

    # Actual date use option
    tk.Label(root, text="Use actual date:").grid(row=7, column=0, sticky="e", padx=5, pady=5)
    actual_date_var = tk.StringVar(value="No")  # Default to "No"
    tk.Radiobutton(root, text="Yes", variable=actual_date_var, value="Yes").grid(row=7, column=1, sticky="w", padx=5, pady=2)
    tk.Radiobutton(root, text="No", variable=actual_date_var, value="No").grid(row=7, column=1, sticky="e", padx=5, pady=2)

    # Open browser option
    tk.Label(root, text="Open map on browser ?").grid(row=8, column=0, sticky="e", padx=5, pady=5)
    open_browser_var = tk.StringVar(value="No")  # Default to "No"
    tk.Radiobutton(root, text="Yes", variable=open_browser_var, value="Yes").grid(row=8, column=1, sticky="w", padx=5, pady=2)
    tk.Radiobutton(root, text="No", variable=open_browser_var, value="No").grid(row=8, column=1, sticky="e", padx=5, pady=2)


    # Buttons for submit, save, and load
    btn_submit = tk.Button(root, text="   Submit   ", command=submit)
    btn_submit.place(x=130, y=280)

    btn_save = tk.Button(root,   text=" Save to File", command=save_to_file)
    btn_save.place(x=200, y=280)

    btn_load = tk.Button(root,   text="Load from File", command=load_from_file)
    btn_load.place(x=276, y=280)

    # Start the main loop
    root.mainloop()

    # Return the saved data
    return result