import requests
from bs4 import BeautifulSoup

#url of web page you want to scrap 
url = 'https://www.constitutionofindia.net/stages-of-constitution-making/' #web page url of stage of indian constitution 

#send a web page to request for scraping the particular url...first creating any variable(please)
please = requests.get(url)

#check if request was successful
if please.status_code == 200:
    # Parse (to break) the html code for web ... first make a variable(soup)
    soup = BeautifulSoup(please.text, 'html.parser')

    # Extract all the text from the page 
    page_text = soup.get_text()
    
    # Extract all the links from the page ...link & a is the variable assigned by me 
    links = [a['href'] for a in soup.find_all('a', href=True)]

    # Extract all the images from the page 
    images = [img['src'] for img in soup.find_all('img', src=True)]

    # href used for links and src used for images...

    # Print the extracted data
    print("Page Text:")
    print(page_text)

    print("\nLinks:")
    for link in links:
        print(link)

    print("\nImages:")
    for image in images:
        print(image)
    
    else:
        print(f"failed to retrieve the web page. Status code: {please.status_code}")
