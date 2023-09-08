import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyLinkPresence(self, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger