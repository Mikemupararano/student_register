def register_students():
    try:
        # Ask the user how many students are registering
        num_students = int(input("How many students are registering? "))
        
        # Open the file in write mode
        with open('reg_form.txt', 'w') as file:
            # Loop for each student
            for i in range(num_students):
                # Ask the user to enter the next student ID number
                student_id = input(f"Enter student {i+1} ID number: ")
                
                # Write the student ID number to the file
                file.write(student_id + '\n')
                # Add a dotted line after each student ID
                file.write('-' * len(student_id) + '\n')
                
            print("Registration successful. Attendance register created as reg_form.txt")
    except ValueError:
        print("Please enter a valid number of students.")

# Call the function to register students
register_students()
