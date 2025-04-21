class BasePage(): 
    def __init__(self, browser, url):
        self.brower = browser
        self.url = url
    
    def open(self):
        self.brower.get(self.url)