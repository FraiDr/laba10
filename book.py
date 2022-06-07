class Book:
    def __init__(self, name, author, year_of_publication, publishing_house, price):
        self.name = name
        self.author = author
        self.year_of_publication = year_of_publication
        self.publishing_house = publishing_house
        self.price = price

    def __repr__(self):
        return f'The {self.name} written by  {self.author} in' \
               f' {self.year_of_publication} by publishing house named {self.publishing_house}' \
               f' and it\'s price ₴{self.price}'
