
day = 32

try:
    if day > 31:
        raise ValueError('Invalid Day Number')
except ValueError as msg:
    print("The program found an ", msg)
finally:
    print("But the day is beautiful anyway")
