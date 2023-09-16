import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url) -> None:
        self.url: str = url
        pass

    def scrape(self):
        if not self.doesURLExist(self.url):
            print(f"URL does not exist: {self.url}")
            exit()
        
        try:
            html = requests.get(self.url)
        except:
            print(f"Unable to request url: {self.url}")
            exit()

        page = BeautifulSoup(html.content, "html.parser")

        #print(page)

        content = page.find_all("div", {"class": "mw-parser-output"})
        out = ""

        out += "# " + page.find("span",{"class": "mw-page-title-main"}).text + "\n"

        for tag in content:
            itm = tag.find_all(["p","h1","h2","h3","h4","h5"])

            for item in itm:
                match(item.name):
                    case "p":
                        out += f"{item.text}\n"
                    case "h1":
                        out += f"\n# {item.text}\n"
                    case "h2":
                        out += f"\n## {item.text}\n"
                    case "h3":
                        out += f"\n### {item.text}\n"
                    case "h4":
                        out += f"\n#### {item.text}\n"
                    case "h5":
                        out += f"\n##### {item.text}\n"
            
            with(open("out.md","w")) as f:
                f.write(out)
                f.close()
        pass

    def isWikipedia(self, url: str):
        if self.url.startswith("https://en.wikipedia.org/wiki/"):
            return True
        
        return False
    
    def doesURLExist(self, url: str):
        res = requests.get(url)

        if res.status_code == 200:
            return True
        
        return False
    
