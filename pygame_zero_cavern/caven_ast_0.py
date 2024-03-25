import ast


def list_names_signatures_classes(filename):
    """List variable names, function signatures, and class names in a Python file."""

    # Read the source code from the file
    with open(filename, "r") as source:
        tree = ast.parse(source.read(), filename=filename)

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            # For variables, print the variable name (target of assignment)
            for target in node.targets:
                if isinstance(target, ast.Name):
                    print(f"Variable: {target.id}")
        elif isinstance(node, ast.FunctionDef):
            # For functions, print the function name and its arguments
            args = [arg.arg for arg in node.args.args]
            print(f"Function: {node.name}({', '.join(args)})")
        elif isinstance(node, ast.ClassDef):
            # For classes, print the class name
            print(f"Class: {node.name}")


# Replace 'example.py' with the path to the Python source file you want to analyze
list_names_signatures_classes("cavern.py")
