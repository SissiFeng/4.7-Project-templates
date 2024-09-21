# Debugging in VS Code Assignment

## 📚 Introduction

This assignment is designed to help you practice various debugging techniques in Visual Studio Code (VS Code). You'll implement and debug three functions using different methods, including print statements and output logging.

## 🎯 Objectives

By the end of this assignment, you should be able to:

1. Use print statements for basic debugging
2. Implement and debug a sorting algorithm
3. Use print statements to inspect variables during code execution
4. Apply different debugging techniques to solve programming problems

## 🛠️ Setup

1. Ensure you have Python installed in your environment.
2. Install pytest by running `pip install pytest` in your terminal.
3. Open the `debugging.py` file in VS Code.

## 📝 Instructions

### Step 1: Implement the functions

Open `debugging.py` and implement the following functions:

1. `find_max(numbers)`: Find and return the maximum number in the list. Use print statements to debug your implementation.
2. `sort_list(numbers)`: Sort the list in ascending order. Use print statements to output the number of comparisons and swaps.
3. `calculate_average(numbers)`: Calculate and return the average of the numbers. Use print statements to debug your implementation.

### Step 2: Run the main program

After implementing the functions, run the main program to test your implementation:

1. Open a terminal in VS Code.
2. Run the command: `python debugging.py`
3. Observe the output and ensure it looks correct.

### Step 3: Run the tests

To verify your implementation, run the provided tests:

1. In the terminal, run the command: `pytest debugging_test.py`
2. If any tests fail, read the error messages carefully.
3. Go back to `debugging.py`, revise your code, and try again.
4. Repeat steps 2 and 3 until all tests pass.

## 🧪 Testing

The `debugging_test.py` file contains tests for each function. These tests check both the correctness of your implementation and the use of appropriate debugging techniques (print statements).

## 📈 Completion Criteria

You've completed the assignment when:

1. All functions in `debugging.py` are correctly implemented.
2. You've used print statements for debugging in `find_max` and `calculate_average`.
3. You've used print statements to log comparisons and swaps in `sort_list`.
4. All tests in `debugging_test.py` pass when you run `pytest debugging_test.py`.

## 💡 Tips

- Don't rush! Take your time to understand each function's requirements.
- Use meaningful print statements that help you understand what's happening in your code.
- If you're stuck, try adding more print statements to see the state of your variables at different points in the code.
- Remember, debugging is a crucial skill in programming. The more you practice, the better you'll become.

## 🆘 Getting Help

If you encounter any issues or have questions:

1. Review this README file and the comments in `debugging.py` carefully.
2. Check the Python documentation for any functions or methods you're unsure about.
3. If you're still stuck, reach out to your instructor or teaching assistant for help.

Good luck, and happy debugging! 🐛🔍
