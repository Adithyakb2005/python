
l=[]
def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter year of publication: ")
    book_id = str(len(l) + 1)
    book = {'title': title,'author': author,'year': year,'id': book_id}
    l.append(book)
    print("\nBook added successfully")

def update_book():
    book_id = input("Enter the id of the book to update: ")
    for book in l:
        if book['id'] == book_id:
            print(f"Updating book: {book['title']}")
            book['title'] = input("Enter new title: ")
            book['author'] = input("Enter new author: ")
            book['year'] = input("Enter new publication year: ")
            print(f"\nBook updated successfully")
            return
    print("\nBook not found")

def remove_book():
    book_id = input("Enter the id of the book to remove: ")
    for book in l:
        if book['id'] == book_id:
            l.remove(book)
            print(f"\nBook removed successfully!\n")
            return
    print("\nBook not found\n")

def view_books():
    if not l:
        print("\nNo books available")
    else:
        print("\nList of books in the library:")
        for book in l:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, ID: {book['id']}")
        print()

def search_book():
    search1 = input("Enter title or author to search: ").lower()
    rslt = [book for book in l if search1 in book['title'].lower() or search1 in book['author'].lower()]

    if rslt:
        print(f"\nFound {len(rslt)} result:\n")
        for book in rslt:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, ID: {book['id']}")
    else:
        print("\nNo books found")
def main():
    while True:
        print("\n Welcome to the library Management System!")
        print("1.Add book\n2.Update book\n3.Remove book\n4.View All books\n5.Search book\n6.Exit")
        ch=input("Select an option: ")
        if ch == '1':
            add_book()
        elif ch == '2':
            update_book()
        elif ch == '3':
            remove_book()
        elif ch == '4':
            view_books()
        elif ch == '5':
            search_book()
        elif ch == '6':
            print("Exiting")
            break
        else:
            print("\nInvalid option.")



main()