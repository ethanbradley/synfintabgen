import os


class DatasetGeneratorConfig():
    """
    This is a class for configuring the Dataset Generator.

    Attributes:
        dataset_path (str): Absolute path to where the dataset will be
            created.
        dataset_name (str): The name of the dataset which will be
            created.
        document_width (int): The width, in pixels, of the documents.
        document_height (int): The height, in pixels, of the documents.
    """

    def __init__(
            self,
            dataset_path=None,
            dataset_name=None,
            document_width=None,
            document_height=None) -> None:
        """
        The constructor for DatasetGeneratorConfig class.

        Parameters:
            dataset_path (str): Absolute path to where the dataset will
                be created.
            dataset_name (str): The name of the dataset which will be
                created.
            document_width (int): The width, in pixels, of the
                documents.
            document_height (int): The height, in pixels, of the
                documents.
        """

        if dataset_path is not None:
            self.dataset_path = dataset_path
        else:
            self.dataset_path = os.getcwd()

        if dataset_name is not None:
            self.dataset_name = dataset_name
        else:
            self.dataset_name = "dataset"

        if document_width is not None:
            self.document_width = document_width
        else:
            self.document_width = 1489

        if document_height is not None:
            self.document_height = document_height
        else:
            self.document_height = 2106
