import ast


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.indent_level = 0

    def visit_Assign(self, node):
        indent = '    ' * self.indent_level
        for target in node.targets:
            if isinstance(target, ast.Name):
                print(f"{indent}Variable: {target.id}")
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        indent = '    ' * self.indent_level
        args = [arg.arg for arg in node.args.args]
        print(f"{indent}Function: {node.name}({', '.join(args)})")
        self.indent_level += 1
        self.generic_visit(node)
        self.indent_level -= 1

    def visit_ClassDef(self, node):
        indent = '    ' * self.indent_level
        print(f"{indent}Class: {node.name}")
        self.indent_level += 1
        self.generic_visit(node)
        self.indent_level -= 1


def list_names_signatures_classes(filename):
    with open(filename, "r") as source:
        tree = ast.parse(source.read(), filename=filename)

    analyzer = Analyzer()
    analyzer.visit(tree)


# Replace 'example.py' with the path to the Python source file you want to analyze
list_names_signatures_classes("cavern.py")
