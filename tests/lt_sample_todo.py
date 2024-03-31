import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('driver')
class TestLink:

    def test_title(self, driver):
        """
        Verify click and title of page
        :return: None
        """
        driver.get('https://www.flatknotinfo.com')
        driver.implicitly_wait(3)
        driver.find_element(By.NAME, "submit").click()

        driver.implicitly_wait(3)

        driver.find_element(By.LINK_TEXT,"4.1").click();

        driver.implicitly_wait(3)

        title = "FlatKnotInfo: Flat knot 4.1"
        assert title.strip() == driver.title.strip()

