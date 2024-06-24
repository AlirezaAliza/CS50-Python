# calculator
#### Video Demo:  <https://youtu.be/mgVkL0TpixI>
#### Description:
The provided code snippet is a simple Python program designed to perform basic arithmetic operations based on user input. The program is structured around several key components, each serving a distinct purpose in the overall functionality of the calculator. Let's delve into the details of each part of the code to understand how they work together to achieve the desired functionality.

Initial Setup and User Input
The program begins by defining a list of arithmetic operators ("+", "-", "*", "/") in the main() function. This list is stored in the variable list_to_do_list. The function then proceeds to collect user input for two numbers (number_1 and number_2) and an operator (op) using the input() function. The input() function reads a line from input, converts it to a string, and returns that string. Since the program requires numerical operations, the input for the numbers is converted to integers using the int() function. This conversion is crucial because the input() function returns a string by default, and arithmetic operations require numerical types 25.

Input Validation
After collecting the user input, the program validates the inputs using three separate functions: check_for_number_1(number_1), check_for_op(list_to_do_list, op), and check_for_number_2(number_2). These functions check if the inputs are valid and not empty strings. If an input is empty or invalid, an error message is printed. This validation is essential to ensure that the program does not attempt to perform arithmetic operations with invalid data, which could lead to runtime errors or unexpected behavior.

Performing Arithmetic Operations
The core functionality of the program lies in the check_for_op(list_to_do_list, op) function. This function checks if the operator (op) entered by the user is valid (i.e., it is one of the operators in list_to_do_list) and then performs the corresponding arithmetic operation on number_1 and number_2. The results of these operations are printed to the console, enclosed within a series of dashes for visual separation. This approach allows the program to dynamically execute different arithmetic operations based on the operator provided by the user.

Program Execution
The program is executed by calling the main() function and assigning its return values to the variables list_to_do_list, number_1, op, and number_2. After the inputs are collected and validated, the program calls the check_for_op(list_to_do_list, op) function to perform the arithmetic operation and display the result. The program also includes a conditional check at the end (if __name__ == "__main__":) to ensure that the main() function is called only when the script is run directly, and not when it is imported as a module.

Enhancements and Considerations
While the program accomplishes its basic goal of performing arithmetic operations based on user input, there are several areas for improvement and consideration:

Error Handling: The current error handling mechanism is quite basic, simply printing "Error" when invalid input is detected. A more robust error handling system could provide more detailed feedback to the user, helping them correct their input.
User Experience: The program could be made more user-friendly by providing a clear prompt for each input, explaining the expected format or type of input.
Extensibility: The program could be extended to support more operators and more complex mathematical expressions by expanding the list_to_do_list and adding additional conditions in the check_for_op() function.
In conclusion, this simple calculator program demonstrates the basic principles of collecting and validating user input, performing arithmetic operations, and displaying results in Python. It serves as a foundational example for understanding how to build interactive command-line applications.