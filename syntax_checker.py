import sys 

def check_python_syntax(file_path):
    """
    This Checks for syntax errors in a Python file without executing it.

    Args:
        file_path (str): The path to the Python script.

    Returns:
        None
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        # Using the built-in compile() function to validate syntax.
        # The 'exec' mode is used for compiling module-level code.
        compile(source_code, file_path, 'exec')
        
        print(f"✅ The Python script '{file_path}' is valid and has no syntax errors.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' was not found. Please check the file path.")
        sys.exit(1)
    except SyntaxError as e:
        print(f"❌ Syntax Error found in '{file_path}' at line {e.lineno}:")
        print(f"   {e.msg}")

        # The following lines of code will help the user in identifying the line with the error.
        lines = source_code.splitlines()
        if e.lineno <= len(lines):
            print(f"   --> {lines[e.lineno - 1].strip()}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    
    # Asking the user to enter the file path.
    file_to_check = input("Enter the path to the Python script you want to check: ")
    check_python_syntax(file_to_check)
