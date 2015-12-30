import requests
from bs4 import BeautifulSoup

def parseHTMLResponse(htmlObject):
    beautiful_soup_object = BeautifulSoup(htmlObject, 'html.parser')

    # Search through the "results_info" div and return how many children DIVs contain the "success" class
    for div in beautiful_soup_object.find_all("div", class_="results_info"):
        return len(div.find_all("div", class_="success"))

def isCurrentOSUStudent(nameWithDotNumber):
    response = requests.post('https://www.osu.edu/findpeople', params = {"name_n":nameWithDotNumber, "filter":"student"})
    if parseHTMLResponse(response.text) == 1:
        return True
    else:
        return False
    
nameDotNumber = raw_input()
print isCurrentOSUStudent(nameDotNumber)
