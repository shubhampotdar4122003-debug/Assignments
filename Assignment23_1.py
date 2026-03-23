class Bookstore :
    NoofBooks = 0

    def __init__(self,name,Author):
        self.name = name
        self.Author = Author
        Bookstore.NoofBooks += 1
      
    def display(self):     
        print(self.name,"by",self.Author,"No of books :",Bookstore.NoofBooks)
        
obj1 =Bookstore("Linux Sysytem programming","Robert love")
obj1.display()
obj2 = Bookstore("C programming ", "Dennis Ritchie")
obj2.display()       



            
            
            
        
            