# import requests

# # Making a GET request
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# # check status code for response received
# # success code - 200
# print(r)

# # print content of request
# print(r.content)


# import requests
# from bs4 import BeautifulSoup


# # Making a GET request
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# # check status code for response received
# # success code - 200
# print(r)

# # Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())


import requests

def ExtractData(url):
    response = requests.get(url=url).content


dummy=ExtractData(url = 'https://vglug.org/')
print(dummy)