#couroutine
#coroutines are mostly used in cases of time-consuming programs, such as tasks related to machine learning or deep
# learning algorithms, or in cases where the program has to read a file containing a large number of data.
#The while block continues the execution of the coroutine for as long as
# it receives values. The value is collected through the yield statement.
def searcher():
    import time
    book="book content containing thousand words"
    time.sleep(4)

    while True:
        text=yield
        if text in book:
            print("your text is in book")
        else:
            print("your text is not in book")
search=searcher()
print("search started")
next(search)
print("Next method run")
search.send("book")



