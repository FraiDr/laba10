from book import Book


class Node:

    def __init__(self, data: Book):
        self.left = None
        self.right = None
        self.data = data

    def insert_node(self, data: Book):
        if self.data:
            if data.name < self.data.name:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert_node(data)
            elif data.name > self.data.name:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert_node(data)
        else:
            self.data = data

    def find_node(self, value):
        if value < self.data.publishing_house:
            if self.left is None:
                return str(value) + " is not found"
            return self.left.find_node(value)
        elif value > self.data.publishing_house:
            if self.right is None:
                return str(value) + " is not found"
            return self.right.find_node(value)
        else:
            print(self.data)
            if self.left is not None:
                self.left.find_node(value)
            if self.right is not None:
                self.right.find_node(value)

    def delete_node(self, value):
        if value < self.data.author:
            if self.left is None:
                return str(value) + " is not found"
            self.left.delete_node(value)
        elif value > self.data.author:
            if self.right is None:
                return str(value) + " is not found"
            self.right.delete_node(value)
        else:
            self.data = self.right
            if self.left is not None:
                self.left.delete_node(value)
            if self.right is not None:
                self.right.delete_node(value)

    def pre_order(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.pre_order(root.left)
            res = res + self.pre_order(root.right)
        return res
