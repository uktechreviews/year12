# Function 1: Calculates the BMI
# This function takes weight (kg) and height (m) and returns the calculated BMI value.
def get_bmi(weight_kg, height_m):
    if height_m <= 0:
        return 0.0 
    bmi_value = weight_kg / (height_m ** 2)
    return bmi_value

def categorize_bmi(bmi):
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25.0:
        category = "Normal Weight"
    elif 25.0 <= bmi < 30.0:
        category = "Overweight"
    else:
        category = "Obese"
    return category

def print_results(weight, height, bmi, category):
    print("--- BMI Calculation Summary ---")
    print(f"Weight Entered: {weight} kg")
    print(f"Height Entered: {height} m")
    print("-" * 30)
    print(f"Calculated BMI: {bmi:.2f}")  # Formats BMI to two decimal places
    print(f"Health Category: **{category}**")
    print("-" * 30)
    
user_weight = float(input("Enter your weight in Kg "))
user_height = float(input("Enter your height in m "))

bmi_result = get_bmi(user_weight, user_height)

bmi_category = categorize_bmi(bmi_result)

print_results(user_weight, user_height, bmi_result, bmi_category)

