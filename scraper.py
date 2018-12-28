from urllib.request import urlopen

from urllib.error import HTTPError

from urllib.error import URLError

from bs4 import BeautifulSoup

try:

    html = urlopen("https://www.polimi.it/")

except HTTPError as e:

    print(e)

except URLError:

    print("Server down or incorrect domain")

else:

    res = BeautifulSoup(html.read(), "html5lib")

    tags = res.findAll("span", {"class": "newsSubHeader"})

    for tag in tags:

        print(tag.getText())
