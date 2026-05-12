import tkinter as tk
from tkinter import messagebox

def calculate_gui_bmi():
    try:
        # Get values from input fields
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        if weight <= 0 or height <= 0:
            messagebox.showwarning("Input Error", "Please enter positive numbers.")
            return

        # Calculate and categorize
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
            
        # Update the result label
        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Create the main window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("300x250")

# --- UI Elements ---

# Weight Label and Input
tk.Label(window, text="Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(window)
weight_entry.pack()

# Height Label and Input
tk.Label(window, text="Height (m):").pack(pady=5)
height_entry = tk.Entry(window)
height_entry.pack()

# Calculate Button
calc_button = tk.Button(window, text="Calculate BMI", command=calculate_gui_bmi)
calc_button.pack(pady=15)

# Result Display
result_label = tk.Label(window, text="BMI: --\nCategory: --", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run the application
window.mainloop()