import json
from typing import List, Tuple

import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By


class AnnotationGenerator():
    """This is a class for creating annotations."""

    empty_values = ("", "-")

    def __init__(self,
                 annotations_file_path: str,
                 driver: webdriver.Chrome) -> None:
        """
        The constructor for AnnotationGenerator class.

        Parameters:
            annotations_file_path (str): The annotations file path.
            driver (webdriver.Chrome): The Selenium webdriver to
                screenshot the find the bounding boxes.
        """

        self._annotations_file_path = annotations_file_path
        self._driver = driver
        self._tables = []

    def __call__(self,
                 id: str,
                 theme_idx: int,
                 table: List[List[dict]],
                 params: dict) -> None:
        """
        The call method for AnnotationGenerator class.

        Parameters:
            id (str): The ID of the table being annotated.
            theme_idx (int): The index of the theme function used.
            table (List[List[dict]]): The table to be turned into
                annotations.
            params (dict): The table parameters.
        """

        table_dict = self._create_table_dict(id, theme_idx, table, params)
        self._tables.append(table_dict)

    def _create_table_dict(
            self,
            id: str,
            theme_idx: int,
            table: List[List[dict]],
            params: dict) -> dict:
        rows = []

        for i, row in enumerate(table):
            cells = []

            for j, cell in enumerate(row):
                words = []

                for k, word in enumerate(cell['content'].split()):
                    words.append({
                        'bbox': self._get_bounding_box(f"t0:r{i}:c{j}:w{k}"),
                        'text': word
                    })

                cells.append({
                    'bbox': self._get_bounding_box(f"t0:r{i}:c{j}"),
                    'text': cell['content'],
                    'words': words
                })

            rows.append({
                'bbox': self._get_bounding_box(f"t0:r{i}"),
                'cells': cells
            })

        question, answer, ans_row_key, ans_col_key = self._create_q_and_a(
            table,
            params)

        return {
            'id': id,
            'theme': theme_idx,
            'bbox': self._get_bounding_box("t0"),
            'rows': rows,
            'question': question,
            'answer': answer,
            'answerKeys': {
                'row': ans_row_key,
                'col': ans_col_key
            }
        }

    def _create_q_and_a(
            self,
            table: List[List[dict]],
            params: dict) -> Tuple[str, str, str, str]:
        row_count = len(table)
        ans_rox_idx = np.random.randint(0, row_count)

        while (table[ans_rox_idx][0]['type'] == "DATA"
                or table[ans_rox_idx][0]['scope'] == "col"):
            ans_rox_idx += 1

        ans_row_key = table[ans_rox_idx][0]['content']

        if params['note_column']:
            col_start_idx = 2
        else:
            col_start_idx = 1

        if params['double_column']:
            col_end_idx = col_start_idx + 3
        else:
            col_end_idx = col_start_idx + 1

        ans_col_idx = np.random.randint(col_start_idx, col_end_idx+1)
        answer = table[ans_rox_idx][ans_col_idx]['content']

        while answer in self.empty_values:
            if ans_col_idx == col_end_idx:
                ans_col_idx = col_start_idx
            else:
                ans_col_idx += 1

            answer = table[ans_rox_idx][ans_col_idx]['content']

        ans_col_key_idx = ans_col_idx

        if params['double_column']:
            ans_col_key_idx = int(col_start_idx
                + np.floor((ans_col_idx - col_start_idx) / 2))

        ans_col_key = table[0][ans_col_key_idx]['content']
        question = f"What is the value of {ans_row_key} for {ans_col_key}?"

        assert answer not in self.empty_values

        return question, answer, ans_row_key, ans_col_key

    def _get_bounding_box(self, id: str) -> List[int]:
        rect = self._driver.find_element(By.ID, id).rect
        x_0 = rect['x']
        y_0 = rect['y']
        x_1 = x_0 + rect['width']
        y_1 = y_0 + rect['height']

        return [int(x_0), int(y_0), int(x_1), int(y_1)]

    def write_to_file(self) -> None:
        """Calling this writes the tables to the annotations file."""

        with open(self._annotations_file_path, "w") as annotations:
            json.dump(self._tables, annotations, ensure_ascii=False)
