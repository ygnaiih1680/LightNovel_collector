import requests
from bs4 import BeautifulSoup

re = requests.get("https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=50&ViewType=Detail&PublishMonth=0&SortOrder=6&page=1&Stockstatus=1&PublishDay=84&CID=50927", "html.parser")
soup = BeautifulSoup(re.text, "html.parser")

bookList = soup.find_all("div", {"class": "ss_book_box"})

print(bookList)
