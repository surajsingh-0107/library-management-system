from utils import books
def show():
    if len(books)==0:
        print("book not available")
    else:
        for _ in books:
            print(_)