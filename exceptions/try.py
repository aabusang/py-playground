
#intentionally misspelled a variable name to test
#an exception
title = "Python for beginners in easy steps"

try:
    print(titel)
except NameError as msg:
    print(msg)
