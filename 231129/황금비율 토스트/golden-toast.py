# Node 클래스를 만들어줍니다.
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        self.prev = None


# 이중 연결 리스트 클래스를 만들어줍니다.
class DoublyLinkedList:
    def __init__(self):
        self.END = Node(-1)                # 구현의 편의를 위해 dummy 값을 넣어놓고 시작합니다.
        self.head = self.END
        self.tail = self.END
  
    def push_front(self, new_data):        # 원소를 첫 번째 위치에 넣어줍니다.
        new_node = Node(new_data)          # 새로운 노드를 만들어줍니다.
        new_node.next = self.head          # 새로운 노드의 next 값을 head로 바꿔줍니다.

        self.head.prev = new_node          # 이전 head의 prev값을 바꾼 뒤
        self.head = new_node               # head값을 변경해줍니다.
        new_node.prev = None

    def push_back(self, new_data):         # 원소를 맨 끝 위치에 넣어줍니다.
        if self.begin() == self.end():     # 만약 리스트가 비어있다면
            self.push_front(new_data)      # 맨 앞에 원소를 넣어주는 것과 로직이 같습니다. 
            
        else:
            new_node = Node(new_data)      # 새로운 노드를 만들어줍니다.
            new_node.prev = self.tail.prev # 새로운 노드의 prev 값을 맨 끝 dummy의 prev로 변경해준 뒤
            self.tail.prev.next = new_node # 맨 끝 dummy의 next로 새로운 노드를 연결해주고
            new_node.next = self.tail      # 새로운 노드의 next값을 맨 끝 dummy 값으로 바꿔주고
            self.tail.prev = new_node      # 맨 끝 dummy의 prev값을 새로운 노드로 변경합니다.

    def erase(self, node):
        next_node = node.next

        if node == self.begin():           # 만약 head가 삭제되어야 한다면
            temp = self.head          
            temp.next.prev = None          # 새로 head가 될 노드의 prev값을 지워줍니다.
            self.head = temp.next          # head값을 새로 갱신해주고
            temp.next = None               # 이전 head의 next 값을 지워줍니다.

        else:                              # head가 삭제되는 것이 아니라면
            node.prev.next = node.next     # 바로 전 노드의 next값을 바꿔주고
            node.next.prev = node.prev     # 바로 다음 노드의 prev값을 바꿔주고
            node.prev = None               # 해당 노드의 prev 와 
            node.next = None               # 해당 노드의 next 값을 모두 지워줍니다.

        return next_node
    
    def insert(self, node, new_data):
        if node == self.end():             # node가 맨 끝 위치에 있다면
            self.push_back(new_data)       # 맨 뒤에 원소를 추가합니다.   

        elif node == self.begin():         # node가 맨 앞 위치에 있다면
            self.push_front(new_data)      # 맨 앞에 원소를 추가합니다.

        else:                              # 그렇지 않다면
            new_node = Node(new_data)      # 새로운 노드를 만들어줍니다.
            new_node.prev = node.prev      # 새로운 노드의 prev값을 node의 prev값으로 하고
            new_node.next = node           # 새로운 노드의 next값을 node로 하고
            node.prev.next = new_node      # node의 prev의 next값을 새로운 노드로 변경하고
            node.prev = new_node           # node의 prev 값을 새로운 노드로 변경합니다.

    def begin(self):
        return self.head
    
    def end(self):
        return self.tail


n,m = map(int,input("").split(" "))
str = input("")

l = DoublyLinkedList()
for i in range(n):
    l.push_back(str[i])
it = l.end()
for i in range(m):
    command = input("").split(" ")
    if(command[0] == "L"):
        if(it.prev != None):
            it = it.prev
    elif(command[0] == "R"):
        if(it.next != None):
            it = it.next
    elif(command[0] == "D"):
        it = l.erase(it)
    else:
        l.insert(it,command[1])

it = l.begin()
while it != l.end(): 
    print(it.data, end="")
    it = it.next