class book:
  def __init__(self,title,author,is_borrowed = False):
    self.title = title
    self.author = author
    is_borrowed = False
  def borrow(self):
    self.is_borrowed = True
    print(f"{self.title} by {self.author} is borrowed.")
  def return_book(self):
    self.is_borrowed = False
    print(f"{self.title} by {self.author} is returned.")

rj = book("Romeo and Juliet","William Shakespeare")
ccf = book("Charlie and the Chocolate Factory","Roald Dahl")
motl = book("The Murder on the Links","Agatha Christie")

for i in rj,ccf,motl:
  i.borrow()
  i.return_book()
  print("")