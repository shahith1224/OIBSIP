def calculate_bmi(weight, height):
    """Calculates the Body Mass Index."""
    return weight / (height ** 2)

def categorize_bmi(bmi):
    """Classifies the BMI into standard health categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("--- Python Command-Line BMI Calculator ---")
    
    # 1. User Input Validation & Error Handling
    try:
        weight_str = input("Enter your weight in kilograms (kg): ")
        height_str = input("Enter your height in meters (m): ")
        
        weight = float(weight_str)
        height = float(height_str)
        
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive numbers greater than zero.")
            return

        # 2. BMI Calculation
        bmi = calculate_bmi(weight, height)
        
        # 3. Categorization
        category = categorize_bmi(bmi)
        
        # Output results rounded to 2 decimal places
        print(f"\nResults:")
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Health Category: {category}")

    except ValueError:
        # Handles cases where the user types text instead of numbers
        print("Error: Invalid input. Please enter numerical values only.")

if __name__ == "__main__":
    main()