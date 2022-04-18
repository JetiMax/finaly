from config import url


class OzonPage():

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(url)

    def get_shops(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Бренды')]").click()
