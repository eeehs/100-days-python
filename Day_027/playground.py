
# *args

def add(*args):
    result = 0
    for n in args:
        result +=n
    return result

print(add(3,4,5,6,7,8))

# **kwargs

def calculate(**kwargs):
    print(kwargs)