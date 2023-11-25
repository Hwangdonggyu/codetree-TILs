n = int(input(""))
arr = []
def push_back(a):
    arr.append(a)

def pop_back():
    arr.pop()

def size():
    return len(arr)

def get(k):
    return arr[k-1]

for i in range(n):
    str_input = input("").split(" ")
    str = str_input[0]
    if(len(str_input)>1):
        a = int(str_input[1])
    if(str == "push_back"):
        push_back(a)
    elif(str == "pop_back"):
        pop_back()
    elif(str=="get"):
        print(get(a))
    else:
        print(size())