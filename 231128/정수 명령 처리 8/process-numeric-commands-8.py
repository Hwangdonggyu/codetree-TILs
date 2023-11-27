# Node 클래스를 만들어줍니다.
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        self.prev = None


# 이중 연결 리스트 클래스를 만들어줍니다.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0
  
    def push_front(self, new_data):   # 원소를 첫 번째 위치에 넣어줍니다.
        new_node = Node(new_data)     # 새로운 노드를 만들어줍니다.
        new_node.next = self.head     # 새로운 노드의 next 값을 head로 바꿔줍니다.

        if self.head != None:         # 기존 리스트가 비어있지 않았다면
            self.head.prev = new_node # 이전 head의 prev값을 바꾼 뒤
            self.head = new_node      # head값을 변경해줍니다.
            new_node.prev = None
    
        else:                         # 기존 리스트가 비어있었다면
            self.head = new_node      # head, tail을 새로 설정해줍니다.
            self.tail = new_node
            new_node.prev = None
        
        self.node_num += 1

    def push_back(self, new_data):    # 원소를 맨 끝 위치에 넣어줍니다.
        new_node = Node(new_data)     # 새로운 노드를 만들어줍니다.
        new_node.prev = self.tail     # 새로운 노드의 prev 값을 tail로 바꿔줍니다.

        if self.tail != None:         # 기존 리스트가 비어있지 않았다면
            self.tail.next = new_node # 이전 tail의 next값을 바꾼 뒤
            self.tail = new_node      # tail 값을 변경해줍니다.
            new_node.next = None

        else:                         # 기존 리스트가 비어있었다면
            self.head = new_node      # head, tail을 새로 설정해줍니다.
            self.tail = new_node
            new_node.next = None

        self.node_num += 1

    def pop_front(self):              # 첫 번째 수를 빼면서 동시에 그 수를 반환합니다.
        if self.head == None:
            print("List is empty")
    
        elif self.head.next == None:  # 노드가 하나 남았다면
            temp = self.head

            self.head = None          # head값을 None으로 바꿔주고
            self.tail = None          # tail값도 None으로 바꿔주고
            self.node_num = 0         # 원소의 수도 0개로 변경해줍니다.
            return temp.data

        else:
            temp = self.head
            temp.next.prev = None     # 새로 head가 될 노드의 prev값을 지워줍니다.
            self.head = temp.next     # head값을 새로 갱신해주고
            temp.next = None          # 이전 head의 next 값을 지워줍니다.

            self.node_num -= 1
            return temp.data
  
    def pop_back(self):               # 맨 끝에 있는 수를 빼면서 동시에 그 수를 반환합니다.
        if self.tail == None:
            print("List is empty")

        elif self.tail.prev == None:  # 노드가 하나 남았다면
            temp = self.tail

            self.head = None          # head값을 None으로 바꿔주고
            self.tail = None          # tail값도 None으로 바꿔주고
            self.node_num = 0         # 원소의 수도 0개로 변경해줍니다.
            return temp.data

        else:
            temp = self.tail
            temp.prev.next = None     # 새로 tail이 될 노드의 next값을 지워줍니다.
            self.tail = temp.prev     # tail값을 새로 갱신해주고
            temp.prev = None          # 이전 tail의 prev 값을 지워줍니다.

            self.node_num -= 1
            return temp.data

    def size(self):
        return self.node_num

    def empty(self):
        return self.node_num == 0

    def front(self):                  # 첫 번째 수를 반환합니다.
        if self.head == None:
            print("List is empty")
        else:
            return self.head.data
  
    def back(self):                   # 맨 끝에 있는 수를 반환합니다.
        if self.tail == None:
            print("List is empty")
        else:
            return self.tail.data


# 변수 선언 및 입력:
n = int(input())
l = DoublyLinkedList()

for _ in range(n):
    command = input()
    if command.startswith("push_front"):
        x = int(command.split()[1])
        l.push_front(x)
    elif command.startswith("push_back"):
        x = int(command.split()[1])
        l.push_back(x)
    elif command == "pop_front":
        print(l.pop_front())
    elif command == "pop_back":
        print(l.pop_back())
    elif command == "size":
        print(l.size())
    elif command == "empty":
        print(1 if l.empty() else 0)
    elif command == "front":
        print(l.front())
    else:
        print(l.back())