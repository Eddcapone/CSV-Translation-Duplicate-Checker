import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import csv
from collections import Counter


def upload_csv():
    """Upload a CSV file."""
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if filepath:
        csv_file_path.set(filepath)


def normalize_words(words):
    """Normalize words by stripping whitespace, quotes, and converting to lowercase."""
    return {word.strip().strip('"').strip("'").lower() for word in words if word.strip()}


def check_words():
    """Check if words exist in the uploaded CSV and find duplicates."""
    csv_path = csv_file_path.get()
    if not csv_path:
        messagebox.showerror("Error", "Please upload a CSV file first!")
        return

    word_input = textarea.get("1.0", tk.END).strip()
    if not word_input:
        messagebox.showerror("Error", "Please enter some words to check!")
        return

    # Read words from text area
    word_list = normalize_words(word_input.splitlines())

    try:
        # Read the CSV and process rows with a progress bar
        with open(csv_path, 'r', encoding='utf-8') as csvfile:
            reader = list(csv.reader(csvfile))
            total_rows = len(reader)

            # Reset progress bar
            progress_bar["maximum"] = total_rows
            progress_bar["value"] = 0

            csv_content = set()
            all_csv_values = []  # Collect values for duplicate detection
            for idx, row in enumerate(reader):
                # Normalize and add the first column and the second column to csv_content
                if len(row) > 0:
                    first_col = row[0].strip().strip('"').strip("'").lower()
                    csv_content.add(first_col)
                    all_csv_values.append(first_col)
                if len(row) > 1:
                    second_col = row[1].strip().strip('"').strip("'").lower()
                    csv_content.add(second_col)
                    all_csv_values.append(second_col)
                progress_bar["value"] = idx + 1
                root.update_idletasks()  # Force the GUI to refresh

            # Check for duplicates in all values
            duplicates = [item for item, count in Counter(all_csv_values).items() if count > 1]

            # Perform matching
            found_words = word_list.intersection(csv_content)
            not_found_words = word_list - csv_content

            # Update the listbox with results
            result_listbox.delete(0, tk.END)
            result_listbox.insert(tk.END, "Found Words:")
            for word in found_words:
                result_listbox.insert(tk.END, f"  {word}")

            # Conditionally display "Not Found Words" if the checkbox is set
            if show_not_found_var.get():
                result_listbox.insert(tk.END, "\nNot Found Words:")
                for word in not_found_words:
                    result_listbox.insert(tk.END, f"  {word}")

            # Conditionally display "Duplicates" if the checkbox is set
            if show_duplicates_var.get():
                result_listbox.insert(tk.END, "\nDuplicates:")
                for duplicate in duplicates:
                    result_listbox.insert(tk.END, f"  {duplicate}")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to process the CSV file: {e}")


# Create main window
root = tk.Tk()
root.title("CSV Translation Duplicate Checker")
root.geometry("800x600")

# Variables
csv_file_path = tk.StringVar()
show_not_found_var = tk.BooleanVar(value=False)  # Checkbox state for "Not Found Words"
show_duplicates_var = tk.BooleanVar(value=False)  # Checkbox state for "Duplicates"

# GUI Elements
tk.Label(root, text="Upload CSV File:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Button(root, text="Upload CSV", command=upload_csv).grid(row=0, column=1, padx=10, pady=5, sticky="w")
tk.Label(root, textvariable=csv_file_path, wraplength=500, fg="blue").grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

tk.Label(root, text="Enter Words to Check (one per line):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
textarea = tk.Text(root, height=10, width=40)
textarea.grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Checkbox for "Not Found Words"
tk.Checkbutton(root, text="List Not Found Words", variable=show_not_found_var).grid(row=4, column=0, padx=10, pady=5, sticky="w")

# Checkbox for "Duplicates"
tk.Checkbutton(root, text="Show Duplicates", variable=show_duplicates_var).grid(row=5, column=0, padx=10, pady=5, sticky="w")

tk.Button(root, text="Check Words", command=check_words).grid(row=6, column=0, padx=10, pady=10, sticky="w")

# Progress bar
tk.Label(root, text="Processing Progress:").grid(row=7, column=0, padx=10, pady=5, sticky="w")
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.grid(row=8, column=0, padx=10, pady=5, sticky="w")

# Results Listbox
tk.Label(root, text="Results:").grid(row=2, column=1, padx=10, pady=5, sticky="w")
result_listbox = tk.Listbox(root, width=50, height=25)
result_listbox.grid(row=3, column=1, rowspan=6, padx=10, pady=5, sticky="w")

# Run the application
root.mainloop()
