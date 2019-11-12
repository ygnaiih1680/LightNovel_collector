import requests
from bs4 import BeautifulSoup

re = requests.get(
    "https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=50&ViewType=Detail&PublishMonth=0&SortOrder=6&page=1&Stockstatus=1&PublishDay=84&CID=50927",
    "html.parser")
soup = BeautifulSoup(re.text, "html.parser")

bookList = soup.find_all("div", {"class": "ss_book_box"})

bookDescriptions = []
for book in bookList:
    bookDescriptions.append(book.find_all("li")[0:2])
for description in bookDescriptions:
    temp = description[0].find("a", {"class": "bo3"})
    if temp is None:
        description[0] = description[0].find("span").string
        description[1] = description[1].find("a").find("b").string
    else:
        title = temp.find("b").string
        description[0] = "x"
        description[1] = title
print(bookDescriptions)
