class Library:
  def __init__(self):
    self.books=[]
    self.no_of_books=0
  def printbooks(self):
    print("The Library has following books: ")
    for book in self.books:
      print(book)

  def add_book(self,book):
    self.books.append(book)
    self.no_of_books+=1

  def get_no_of_books(self):
    return self.no_of_books

l1=Library()
l1.add_book("Chemistry")
l1.add_book("Python by Henry")
l1.add_book("The Great World")
l1.add_book("Physics")
l1.printbooks()
print("The Library has", l1.get_no_of_books(), "books.")
      
  