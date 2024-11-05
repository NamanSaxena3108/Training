def fun(x):
    if x>1:
        fun(x//2)
        fun(x//2)
    print(x)
fun(4)

def fun(x):
    print(x)
    if x>1:
        fun(x//2)
        fun(x//2)
fun(4)