# this file can be empty

# PURPOSE OF THE INIT__.PY FILE



"""
It can be completely empty, The __init__.py tells Python:
"This folder can be treated as a Python package.


Then you can do things like:

"from cloud_storage import s3operation.py "



__init__.py does not run your FastAPI server.
It mainly helps organize your Python code into packages and control what gets exposed when the package is imported.

Also, you don't necessarily need __init__.py just because you're using FastAPI. 
Modern Python can recognize certain directories as packages without it. 
However, you'll still see __init__.py commonly used in FastAPI and other Python projects 
because it makes the package structure explicit.


"""