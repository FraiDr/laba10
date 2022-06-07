from book import Book
from node import Node

dune = Book("Dune", "Frank Herbert", 1965, "Analog Science Fiction and Fact", 120)
grad = Book("Voroshylovgrad", "Sergiy Zhadan", 2010, "Folio", 210)
stranger = Book("Stranger", "Max Frai", 2005, "Amphora", 135)
foundation = Book("Foundation's Edge.", "Isaac Asimov", 1997, "KSD", 199)


root = Node(grad)
root.insert_node(stranger)
root.insert_node(dune)
root.insert_node(foundation)

for book in root.pre_order(root):
    print(book)
print()
print(root.find_node("Folio"))
print()
root.delete_node("Sergiy Zhadan")

for book in root.pre_order(root):
    print(book)
