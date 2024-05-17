from datetime import timedelta
from typing import Union, List, Any
from urllib.parse import ParseResult
from RPA.Browser.Selenium import Selenium
from RPA.Robocorp.WorkItems import WorkItems
from script import logger
from script.exceptions import ElementInteractionError


class BrowserAction:
    """
    Class for performing actions on a web browser.
    """

    def __init__(self, selenium: Selenium, timeout_sec: int = 20):
        """
        Initializes BrowserAction with a Selenium instance.
        
        Args:
            selenium (Selenium): Instance of Selenium.
            timeout_sec (int, optional): Timeout in seconds.
        """
        self.selenium = selenium
        self.selenium.set_selenium_timeout(timedelta(seconds=timeout_sec))
        self.logger = logger
        self.library = WorkItems()

    def connect(self, url: Union[str, ParseResult] = None) -> None:
        """
        Connect to the browser and maximize the window.
        
        Args:
            url (Union[str, ParseResult], optional): URL to open in the browser.
        """
        if url is None:
            self.selenium.open_available_browser()
        else:
            self.logger.info(f"Connecting to URL: {url}")
            self.selenium.open_available_browser(url)

    def browse(self, url: Union[str, ParseResult]) -> None:
        """
        Browse a specific url after the browser is already open.

        Args:
            url (Union[str, ParseResult], optional): URL to open in the browser.
        """
        if url is not None:
            try:
                self.selenium.go_to(url)
            except Exception as e:
                self.logger.exception(f'Error opening url: {url} with the error: {e}')
                raise Exception(f'Error opening url: {url} with the error: {e}')
        else:
            self.logger.exception("URL cannot be None")

    def maximize(self):
        """
        Maximize the browser to the full screen size.
        """
        self.selenium.maximize_browser_window()

    def _click_element(self, locator: str) -> None:
        """
        Clicks the web element identified by the given locator.

        Args:
            locator (str): The locator of the web element to click.

        Returns:
            bool: True if the element was successfully clicked, False otherwise.
        """
        try:
            self.selenium.click_element(locator)
            self.logger.info("Button clicked")
        except Exception as e:
            self.logger.exception(f"Error clicking element: {e}")
            raise ElementInteractionError(f"Error clicking element: {e}")

    def _input_text(self, locator: str, text: str) -> None:
        """
        Enters text into the input field identified by the given locator.

        Args:
            locator (str): The locator of the input field.
            text (str): The text to enter into the input field.

        Returns:
            bool: True if the text was successfully entered, False otherwise.
        """
        try:
            self.selenium.input_text(locator, text)
            self.logger.info("Successfully entered input text")
        except Exception as e:
            self.logger.exception(f"Error entering text: {e}")
            raise ElementInteractionError(f"Error entering text: {e}")

    def _retrieve_elements(self, locator: str) -> List[Any]:
        """
        Retrieves a list of web elements identified by the given locator.
        If the elements are found, they are returned as a list of WebElements.
        If the elements are not found, an exception is raised.

        Args:
            locator (str): The locator of the web elements to retrieve.

        Returns:
            List[Any]: A list of web elements matching the locator.
        """
        try:
            elements = self.selenium.find_elements(locator)
            self.logger.info("Successfully retrieved elements")
            return elements
        except Exception as e:
            self.logger.exception(f"Error retrieving elements: {e}")
            raise ElementInteractionError(f"Error retrieving elements: {e}")

    def _retrieve_text(self, locator: str) -> str:
        """
        Retrieves the text passed into the input field identified by the given locator.
        If the elements are found, the text part of the element is returned as a string.
        If the elements are not found, an exception is raised.

        Args:
            locator (str): The locator of the web elements to retrieve.

        Returns:
            List[Any]: A list of web elements matching the locator.
        """
        try:
            self.logger.info("Retrieving text element")
            text = self.selenium.get_text(locator)
            self.logger.info("Successfully retrieved elements")
            return text
        except Exception as e:
            self.logger.exception(f"Error retrieving elements: {e}")
            raise ElementInteractionError(f"Error retrieving elements: {e}")

    def _handle_invalid_action(self, action: str) -> None:
        """
        Handles an invalid action by raising a ValueError.

        Args:
            action (str): The invalid action.

        Raises:
            ValueError: If an invalid action is provided.
        """
        raise ValueError(f"Invalid action: {action}")

    def element_interaction(self, locator: str, action: str, text: str = None) -> Union[bool, List]:
        """
        Perform interaction with a web element based on the specified action.

        Args: locator (str): The locator of the web element. action (str): The action to perform. Possible values are
        'click', 'input_text', 'retrieve_element', or 'retrieve_elements'. text (str, optional): The text to input (
        only required for 'input_text' action). Defaults to None.

        Returns: Union[bool, List]: Returns True for actions that succeed, and for 'retrieve_element' or
        'retrieve_elements' actions, returns a list of web elements.

        Raises:
            ValueError: If an invalid action is provided.
        """
        try:
            self.selenium.wait_until_element_is_visible(locator)

            actions = {
                'click': lambda: self._click_element(locator),
                'input_text': lambda: self._input_text(locator, text),
                'retrieve_elements': lambda: self._retrieve_elements(locator),
                'retrieve_text': lambda: self._retrieve_text(locator),
            }

            handler = actions.get(action, self._handle_invalid_action)
            return handler()
        except ElementInteractionError as e:
            e.log_error(f"Error interacting with the element: {e}")
            raise ElementInteractionError(f"Error interacting with the element: {e}")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Error occurred while interacting with element: {e}")


    def close_browser(self):
        """
        Close the browser.
        """
        self.logger.info("Closing the browser")
        self.selenium.close_browser()