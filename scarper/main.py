from bs4 import BeautifulSoup
import requests
import re


url='https://github.com/jborean93?tab=repositories'

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

main_layout = []
main_layout = soup.find_all('a', attrs={'itemprop':'name codeRepository'})
star_layout = soup.find_all('a',attrs={'href':re.compile("stargazers")})

hrefs =[]
texts =[]


for data in main_layout:
    hrefs.append(data.attrs['href'])
    texts.append(data.text)
stars =dict()
for star in star_layout:
    stars[star.attrs['href']] =int(star.text)

pass
