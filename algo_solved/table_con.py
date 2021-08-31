class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    # 헤더부터 탐색해 뒤에 새로운 노드 추가하기
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    # 모든 노드 값 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index-1)
        node.next = node.next.next

    def length(self):
        cur = self.head
        length = 0
        while cur is not None:
            length += 1
            cur = cur.next
        return length




def solution(n, k, cmd):
    link = dict()
    for i in range(1, n-1):
        link[i] = [i - 1, i + 1]
    link[0], link[n-1] = [0, 1], [n-2, 0]
    delete = []
    idx = k
    first_num, last_num = 0, n-1


    for control in cmd:
        if control[0] == 'D':
            for _ in range(int(control[2])):
                before, after = link[idx]
                idx = after

        elif control[0] == 'U':
            for _ in range(int(control[2])):
                before, after = link[idx]
                idx = before
        elif control[0] == 'C':
            if idx == first_num:
                delete.append(idx)
                idx, first_num = link[first_num][1], link[first_num][1]


            elif idx == last_num:
                delete.append(idx)
                idx, last_num = link[last_num][0], link[last_num][0]


            else:
                before, after = link[idx]
                delete.append(idx)
                link[before][1], link[after][0] = after, before
                idx = link[idx][1]

        else: # 삭제된 행 복구
            num = delete.pop()
            if num > last_num:
                last_num = num

            elif num < first_num:
                first_num = num

            link[link[num][0]][1], link[link[num][1]][0] = num, num



    answer = ['O'] * n
    for i in delete:
        answer[i] = 'X'
    # print(link)
    return ''.join(answer)


print(solution(8, 2, ["D 2","C","U 4","C","D 4","C","U 2","Z","Z","U 1","C"]))
# print(solution(8, 2, [ "C", "C", "C", "C", "C", "C", "C","Z", "Z", "Z", "Z", "Z", "Z", "Z",]))