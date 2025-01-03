class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print(self.title)
        print(self.author)
class Python(Book):
    def __init__(self,name,title,author,price,number_of_pages):
       super().__init__(name,title,author)
       self.price = price
       self.number_of_pages = number_of_pages
    def display(self):
       super().display()
       print("name:",self.name)
       print("title:",self.title)
       print("author:",self.author)
       print("price:",self.price)
       print("number of pages:",self.number_of_pages)
p1=Python("Ashraf","aadjeevitham (THE GOAT LIFE)","Benyamin","560","1650")
p1.display()