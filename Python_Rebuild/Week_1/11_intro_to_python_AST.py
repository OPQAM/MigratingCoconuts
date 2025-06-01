import ast

# Abstract Syntax Tree, or AST, is Python's way of representing code as data.
# When Python runs our script, it first parses it into a tree structure (AST),
# where each node represents a syntactic element (i.e., function call, variable, ...)

tree = ast.parse("x = a + b")

print(ast.dump(tree, indent=4))


