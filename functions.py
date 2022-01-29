# The function that does all the work in this program

import bs4
import requests


def findText(url):
    result = requests.get(url)  # To retrieve the webpage data
    result.raise_for_status()  # To raise an exception if something goes wrong

    soup = bs4.BeautifulSoup(result.text, features='html.parser')  # To make a beautifulsoup object of the html content
    p_elements = soup.select('p')  # To make a list of all the paragraph elements

    paragraphs = []
    for element in p_elements:
        paragraphs.append(element.text)  # To add just the text of each paragraph to the list

    text = '\n\n'.join(paragraphs)  # This will make the article into a single string

    return text
