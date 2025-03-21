from selenium import webdriver


class ImageGenerator():
    """This is a class for creating images."""

    def __init__(self, image_dir: str, driver: webdriver.Chrome) -> None:
        """
        The constructor for ImageGenerator class.

        Parameters:
            image_dir (str): The image directory.
            driver (webdriver.Chrome): The Selenium webdriver to
                screenshot the HTML document.
        """

        self._image_dir = image_dir
        self._driver = driver

    def __call__(self, id: str, document_file_path: str) -> None:
        """
        The call method for ImageGenerator class.

        Parameters:
            id (str): The ID of the image to be created.
            document_file_path (str): The file path of the HTML document
                to be made into an image.
        """

        self._create_image_from_html(id, document_file_path)

    def _create_image_from_html(
            self,
            id: str,
            document_file_path: str) -> None:
        self._driver.get(document_file_path)
        self._driver.save_screenshot(f"{self._image_dir}/{id}.png")
