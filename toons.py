import time
from bs4 import BeautifulSoup
import requests
from requests import get

url = "https://tamiltvtoons.blogspot.com/2022/11/kiteretsu-1988-season-1-episodes-in.html?m=1"

def toons(url):
    client = requests.session()
    r = client.get(url).text
    soup = BeautifulSoup (r, "html.parser")
    links = soup.select('a[href*="short2url"]')
    gd_txt = f"Total Links Found : {len(links)}\n\n"
    print(gd_txt)
    for a in links:
         download = get(a['href'], stream=True, allow_redirects=False)
         url = download.headers["location"]
         DOMAIN = "https://technemo.xyz/blog"
         url = url[:-1] if url[-1] == '/' else url
         code = url.split("/")[-1]
         final_url = f"{DOMAIN}/{code}"
         ref = "https://mytop5.club/"
         h = {"referer": ref}
         resp = client.get(final_url, headers=h)
         soup = BeautifulSoup(resp.content, "html.parser")
         inputs = soup.find_all("input")
         data = { input.get('name'): input.get('value') for input in inputs }
         h = { "x-requested-with": "XMLHttpRequest" }
         time.sleep(10)
         r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
         g = r.json()['url']
         if "drive.google.com" in g:
                t = client.get(g).text
                soupt = BeautifulSoup(t, "html.parser")
                title = soupt.title
                gd_txt = f"{(title.text).replace('GDToT | ' , '')}\n{g}\n\n"
                print(gd_txt)

print(toons(url))
