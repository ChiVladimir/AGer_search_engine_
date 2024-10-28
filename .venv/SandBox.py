# from display import HTML
from bs4 import BeautifulSoup

html = """
<html><body>
<h1>Test</h1>
<ol>
	<li>First item</li>
	<li>Item with <a href="http://hse.ru">link</a></li>
	<li>Another item with <a href="http://wikipedia.org">another link</a>.</li>
</ol>
</body>
</html>
"""

soup = BeautifulSoup(html, "lxml")

srch_1 = soup.find("h1")
print('srch_1', srch_1)

srch_2 = soup.find("ol")
print('srch_2',srch_2)

srch_3 = soup.find("a")
print('srch_3', srch_3)
print('srch_3+', srch_3["href"])  # ask content with tag <href> from <a>

srch_4 = soup.find_all("li")  # return list[]
print('srch_4', len(srch_4), srch_4)
print('srch_4+', srch_4[2])

# Task - return all links from <a>
_links = soup.find_all("a")
print(_links)
i = 0
for i in range(len(_links)):
    print(_links[i]["href"])
    i += 1
