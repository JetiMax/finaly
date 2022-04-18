from config import url


class ShopPage():

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(url)

    def get_shops(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Дом и сад')]").click()

    def get_shops1(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Красота и здоровье')]")
