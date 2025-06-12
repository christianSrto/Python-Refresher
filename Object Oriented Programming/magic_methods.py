# Magic Methods = Dunder methods __init__, __str__, __repr__, __add__, __len__, etc.
#                 They are automatically called by many built-in functions and operators
#                 They allow us to define or customize the behavior of objects 

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"


    def __eq__(self, other):
        return (self.title == other.title and 
            self.author == other.author and 
            self.pages == other.pages)   

    def __lt__(self, other):       
        return self.pages < other.pages
        
    def __gt__(self, other):       
        return self.pages > other.pages
        
    def __add__(self, other):
        return self.pages + other.pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'pages':
            return self.pages
        else:
            return "Invalid key"

book1 = Book("Harry Potter", "J.K. Rowling", 500)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 300)
book3 = Book("The Hobbit", "J.R.R. Tolkien", 300)

# Using the __str__ method to print the book object
print(book1)

# Using the __eq__ method to compare book objects
print(book3 == book2)

# Using the __lt__ method to compare book objects based on the number of pages
print(book1 < book2)

print(book1 > book2)

# Using the __add__ method to add the number of pages of two book objects
print(book2+book3)

# Using the __contains__ method to check if a keyword is in the book title or author
print("Hobbit" in book2)

# Using the __getitem__ method to access book attributes
print(book1['title'])