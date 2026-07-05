from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_text(self, locator):
        return self.find(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_invisibility(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_url_contains(self, text):
        self.wait.until(lambda driver: text in driver.current_url)

    def wait_for_text_not_equal(self, locator, unwanted_text):
        self.wait.until(lambda driver: self.get_text(locator) != unwanted_text)

    def drag_and_drop(self, source_locator, target_locator):
        source = self.find(source_locator)
        target = self.find(target_locator)
        self.execute_script("arguments[0].scrollIntoView(true);", source)
        self.execute_script("arguments[0].scrollIntoView(true);", target)
        js_code = """
        function simulateDragDrop(source, target) {
            var dataTransfer = new DataTransfer();
            var dragStartEvent = new DragEvent('dragstart', {bubbles: true, cancelable: true, dataTransfer: dataTransfer});
            var dragEnterEvent = new DragEvent('dragenter', {bubbles: true, cancelable: true, dataTransfer: dataTransfer});
            var dragOverEvent = new DragEvent('dragover', {bubbles: true, cancelable: true, dataTransfer: dataTransfer});
            var dropEvent = new DragEvent('drop', {bubbles: true, cancelable: true, dataTransfer: dataTransfer});
            var dragEndEvent = new DragEvent('dragend', {bubbles: true, cancelable: true, dataTransfer: dataTransfer});
            source.dispatchEvent(dragStartEvent);
            target.dispatchEvent(dragEnterEvent);
            target.dispatchEvent(dragOverEvent);
            target.dispatchEvent(dropEvent);
            source.dispatchEvent(dragEndEvent);
        }
        simulateDragDrop(arguments[0], arguments[1]);
        """
        self.execute_script(js_code, source, target)