from pathlib import Path
import sys

from nanoid import non_secure_generate as nanoid
import numpy as np
from selenium import webdriver
from tqdm import trange

from synfintabgen.configuration_dataset_generator import DatasetGeneratorConfig
from synfintabgen.generator_annotation import AnnotationGenerator
from synfintabgen.generator_document import DocumentGenerator
from synfintabgen.generator_image import ImageGenerator
from synfintabgen.generator_table import TableGenerator
from synfintabgen.generator_theme import ThemeGenerator


class DatasetGenerator():
    """This class is for generating a synthetic table image dataset."""

    if sys.platform == "win32":
        _no_pad_char = "#"
    else:
        _no_pad_char = "-"

    _eoy_formats = ("%Y", f"%{_no_pad_char}d.%{_no_pad_char}m.%y")
    _note_column_names = ("Note", "Notes")
    _empty_values = ("", "-")
    _font_sizes = ("x-small", "small", "smaller", "medium", "large", "larger")
    _border_styles = ("solid", "double")
    _typefaces = (
        "Lato",
        "DejaVu Serif",
        "Latin Modern Roman",
        "TeX Gyre Bonum",
        "Nimbus Sans",
        "Utopia"
    )
    _document_id_length = 11
    _document_id_alphabet = ("0123456789abcdefghijklmnopqrstuvwxyz"
                             "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def __init__(self, config=DatasetGeneratorConfig()) -> None:
        """
        The constructor for DatasetGenerator class.

        Parameters:
            config (DatasetGeneratorConfig): A configuration for the
                dataset generator.
        """

        self._config = config
        self._dataset_dir = (f"{self._config.dataset_path}"
                             f"/{self._config.dataset_name}")
        self._html_dir = f"{self._dataset_dir}/html"
        self._image_dir = f"{self._dataset_dir}/image"
        self._annotations_file_path = f"{self._dataset_dir}/annotations.json"
        self._driver = self._get_driver()
        self._table_generator = TableGenerator()
        self._theme_generator = ThemeGenerator()
        self._theme_idices = range(6)
        self._theme_probabilities = (0.4, 0.12, 0.12, 0.12, 0.12, 0.12)
        self._document_generator = DocumentGenerator(self._html_dir)
        self._image_generator = ImageGenerator(self._image_dir, self._driver)
        self._annotation_generator = AnnotationGenerator(
            self._annotations_file_path,
            self._driver)

    def __call__(self, size: int) -> None:
        """
        The call method for DatasetGenerator class.

        This creates a dataset of synthetic dataset based on the config
        passed to the constructor.

        Parameters:
            size (int): Size of the dataset to be generated.
        """

        self._create_dataset_dir()

        for _ in trange(size):
            document_id = nanoid(
                self._document_id_alphabet,
                self._document_id_length)
            params = self._get_params()
            table = self._table_generator(params)
            theme_idx = int(np.random.choice(
                self._theme_idices,
                p=self._theme_probabilities))
            theme = self._theme_generator(theme_idx, params)
            document_file_path = self._document_generator(
                document_id,
                table,
                theme)
            self._image_generator(document_id, document_file_path)
            self._annotation_generator(document_id, theme_idx, table, params)

        self._annotation_generator.write_to_file()

    def _get_params(self) -> dict:
        return {
            'num_sections': np.random.randint(2, 5),
            'numbered_sections': np.random.rand() > .5,
            'uppercase_sections': np.random.rand() > .7,
            'note_column': np.random.rand() > .7,
            'note_column_name': np.random.choice(self._note_column_names),
            'double_column': np.random.rand() > .8,
            'max_value': int(np.random.choice((1e3, 1e4, 1e5, 1e6, 1e7))),
            'thousand_factor': np.random.rand() > .5,
            'eoy_format': np.random.choice(self._eoy_formats),
            'no_value': np.random.choice(self._empty_values, p=(0.8, 0.2)),
            'bracket_negatives': np.random.rand() > .5,
            'typeface': np.random.choice(self._typefaces),
            'font_size': np.random.choice(self._font_sizes),
            'line_height': np.random.choice((1, 1.25, 1.5), p=(0.7, 0.2, 0.1)),
            'border': np.random.rand() > .9,
            'total_row': np.random.rand() > .7,
            'total_border_style': np.random.choice(
                self._border_styles, 
                p=(0.8, 0.2)),
            'total_border_width': np.random.randint(1, 4),
            'double_header_centered': np.random.rand() > .4,
            'current_year_bold': np.random.rand() > .8,
            'note_column_bold': np.random.rand() > .5,
            'note_column_min_width': np.random.randint(35, 80),
            'column_min_width': np.random.randint(55, 250),
            'row_header_max_width': np.random.randint(300, 372)
        }

    def _create_dataset_dir(self) -> None:
        Path(self._dataset_dir).mkdir(exist_ok=True)
        Path(self._image_dir).mkdir(exist_ok=True)
        Path(self._html_dir).mkdir(exist_ok=True)

    def _get_driver(self) -> webdriver.Chrome:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(
            f"window-size={self._config.document_width},"
            f"{self._config.document_height}")

        return webdriver.Chrome(options)
