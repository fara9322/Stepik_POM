class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):   # открываet нужную страницу в браузере, используя метод get().
        self.browser.get(self.url)  #реализация метода
