def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).

    Parameters:
    weight (float): Weight in kilograms.
    height (float): Height in meters.

    Returns:
    float: Calculated BMI.
    """
    return weight / (height ** 2)

def bmi_category(bmi):
    """
    Determine the BMI category.

    Parameters:
    bmi (float): The calculated BMI.

    Returns:
    str: The BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

if __name__ == "__main__":
    # Example usage
    weight = 70.0  # Weight in kilograms
    height = 1.75  # Height in meters

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    print(f"Weight: {weight} kg")
    print(f"Height: {height} m")
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")
