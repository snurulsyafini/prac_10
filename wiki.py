import wikipedia

try:
    page_title = input("Page title/Search phrase: ")
    while page_title != "":
        print(f"Title: {page_title}")
        print("Summary:")
        print(wikipedia.summary(f"{page_title}"))
        page_title = input("Page title/Search phrase: ")
    else:
        print("Thank you.")
except wikipedia.exceptions.DisambiguationError as e:
    print(e.options)
