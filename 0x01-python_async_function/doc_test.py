import importlib.util
import inspect
import sys
import os
from typing import List

def test_module_docstring(module_name: str) -> bool:
    """
    Tests if the module has a docstring.

    Args:
        module_name (str): The name of the module.

    Returns:
        bool: True if the module has a docstring, False otherwise.
    """
    spec = importlib.util.find_spec(module_name)
    if not spec:
        print(f"Module {module_name} not found.")
        return False
    
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    if module.__doc__ and len(module.__doc__.strip()) > 0:
        return True
    return False

def test_function_docstring(module_name: str, function_name: str) -> bool:
    """
    Tests if the function has a docstring.

    Args:
        module_name (str): The name of the module.
        function_name (str): The name of the function.

    Returns:
        bool: True if the function has a docstring, False otherwise.
    """
    spec = importlib.util.find_spec(module_name)
    if not spec:
        print(f"Module {module_name} not found.")
        return False
    
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    func = getattr(module, function_name, None)
    if not func:
        print(f"Function {function_name} not found in module {module_name}.")
        return False
    
    if func.__doc__ and len(func.__doc__.strip()) > 0:
        return True
    return False

def test_type_annotations(module_name: str, function_name: str) -> bool:
    """
    Tests if the function has type annotations.

    Args:
        module_name (str): The name of the module.
        function_name (str): The name of the function.

    Returns:
        bool: True if the function has type annotations, False otherwise.
    """
    spec = importlib.util.find_spec(module_name)
    if not spec:
        print(f"Module {module_name} not found.")
        return False
    
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    func = getattr(module, function_name, None)
    if not func:
        print(f"Function {function_name} not found in module {module_name}.")
        return False
    
    sig = inspect.signature(func)
    for param in sig.parameters.values():
        if param.annotation == param.empty:
            return False
    if sig.return_annotation == sig.empty:
        return False
    return True

def run_tests(file_path: str):
    module_name = os.path.splitext(os.path.basename(file_path))[0]

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if not spec:
        print(f"File {file_path} not found.")
        return
    
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    print(f"Testing module: {module_name}")
    print(f"Module docstring test: {'Passed' if test_module_docstring(module_name) else 'Failed'}")

    functions = [func for func in dir(module) if callable(getattr(module, func))]
    for function_name in functions:
        print(f"Testing function: {function_name}")
        print(f"Function docstring test: {'Passed' if test_function_docstring(module_name, function_name) else 'Failed'}")
        print(f"Function type annotations test: {'Passed' if test_type_annotations(module_name, function_name) else 'Failed'}")
    print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 test_documentation.py <file_name.py>")
    else:
        file_path = sys.argv[1]
        run_tests(file_path)

