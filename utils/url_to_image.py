import requests



def url_to_image(link:str):
    r = requests.get(url=link,allow_redirects=True)
    open("./image_file.png",'wb').write(r.content)
    return