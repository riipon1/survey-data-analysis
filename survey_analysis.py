# Survey Data 
survey_data = [25, 30, 22, 29, 25, 30, 22, 40]

# Function to display menu
def display_menu():
    print("\nSurvey Data Analysis Menu")
    print("1. View Survey Data")
    print("2. Analyze Survey Data")
    print("3. Quit")

# Main program loop
while True:
    display_menu() 
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        print(f"Survey Data: {survey_data}")
    elif choice == '2':
        print("Analysis coming soon!")  
    elif choice == '3':
        print("Goodbye!")
        break  
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
