import requests, json
from datetime import date
import config

def func() :
    # set patht in file config to your path to the directory where you want to store the image
    folder_path = config.setting.patht
    # set api_key in file config to your api key #
    api_key = config.setting.api_key


    URL = "https://api.nasa.gov/planetary/apod?api_key={}".format(api_key) 
    page = requests.get(URL) # this returns a Response
    data = json.loads(page.content)

    print(data['hdurl'])

    image = requests.get(data['hdurl'])
    file_path = "{}/{}.jpg".format(folder_path, date.today())
    
    # Write the image content to a file in the specified folder
    with open(file_path, 'wb') as file:
        file.write(image.content)
    print(("picture added! {}").format(date.today()))

