class ListNode:
    def __init__(self, item, next_node):
        self.item = item
        self.next_node = next_node


class LinkedList():
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__node_cnt = 0

    def __get_node(self, i):
        curr_node = self.__head
        for idx in range(i+1):
            curr_node = curr_node.next_node
        return curr_node

    def __find_node(self, item):
        prev_node = self.__head
        curr_node = prev_node.next_node

        for i in range(self.__node_cnt+1):
            if curr_node.item == item:
                return prev_node, curr_node

            prev_node = curr_node
            curr_node = curr_node.next_node

        return None, None

    def is_empty(self):
        return self.__node_cnt == 0

    def size(self):
        return self.__node_cnt

    def clear(self):
        self.__head.next_node = None
        self.__node_cnt = 0

    def count(self, item):
        curr_node = self.__head.next_node
        cnt = 0
        while curr_node:
            if curr_node.item == item:
                cnt += 1

            curr_node = curr_node.next_node
        return cnt

    def extend(self, next_linked_list):
        for idx in range(next_linked_list.size()):
            self.append(next_linked_list.get(idx))

    def copy(self):
        copied_list = LinkedList()
        for idx in range(self.__node_cnt):
            copied_list.append(self.get(idx))
        return copied_list

    def reverse(self):
        reversed_list = LinkedList()
        for idx in range(self.__node_cnt):
            reversed_list.insert(0, self.get(idx))
        self.clear()
        self.extend(reversed_list)

    def sort(self):
        sorted_list = []
        for idx in range(self.__node_cnt):
            sorted_list.append(self.get(idx))
        sorted_list.sort()
        self.clear()
        for item in sorted_list:
            self.append(item)

    def print_list(self):
        curr_node = self.__head.next_node
        while curr_node:
            print(curr_node.item, end=' ')
            curr_node = curr_node.next_node
        print()

    def insert(self, i, item):
        if 0 <= i <= self.__node_cnt:
            prev_node = self.__get_node(i-1)
            new_node = ListNode(item, prev_node.next_node)
            prev_node.next_node = new_node
            self.__node_cnt += 1
        else:
            raise IndexError

    def append(self, item):
        self.insert(self.__node_cnt, item)

    def pop(self, *args):
        if args:
            i = args[0]
            if 0 <= i < self.__node_cnt:
                prev_node = self.__get_node(i-1)
                curr_node = prev_node.next_node
                prev_node.next_node = curr_node.next_node
                self.__node_cnt -= 1
                ret = curr_node.item
                return ret
            else:
                raise IndexError
        else:
            if not self.is_empty():
                prev_node = self.__get_node(self.__node_cnt-2)
                curr_node = prev_node.next_node
                ret = curr_node.item
                prev_node.next_node = None
                self.__node_cnt -= 1
                return ret
            else:
                return None

    def remove(self, item):
        prev_node, curr_node = self.__find_node(item)
        if curr_node:
            prev_node.next_node = curr_node.next_node
            self.__node_cnt -= 1
        else:
            raise ValueError

    def get(self, i):
        if 0 <= i <= self.__node_cnt:
            return self.__get_node(i).item
        else:
            raise IndexError

    def index(self, item):
        curr_node = self.__head.next_node
        for idx in range(self.__node_cnt):
            if curr_node.item == item:
                return idx

            curr_node = curr_node.next_node

        return -1
