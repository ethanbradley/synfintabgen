import calendar
from datetime import datetime
import random
from typing import List, Tuple

from nltk.corpus import words
import numpy as np


class TableGenerator():
    """This is the TableGenerator class."""

    _section_titles = (
        "Called up share capital",
        "Capital and reserves",
        "Changes in equity",
        "Current assets",
        "Creditors: amounts falling due within one year",
        "Creditors: amounts falling due after more than one year",
        "Debtors: amounts falling due within one year",
        "Debtors: amounts falling due after more than one year",
        "Employees and directors",
        "Fixed asset investments",
        "Fixed assets",
        "Intangiable fixed assets",
        "Investment property",
        "Provisions for liabilities",
        "Related party transactions",
        "Reserves",
        "Revaluation reserve",
        "Tangible fixed assets",
        "Turnover"
    )

    def __init__(self) -> None:
        """The constructor for TableGenerator class."""

        self._vocab = self._load_vocab()

    def __call__(self, params: dict) -> List[List[dict]]:
        """
        The call method for TableGenerator class.

        Parameters:
            params (dict): The table parameters.

        Returns:
            List[List[dict]]: The table.
        """

        return self._create_table(params)

    def _create_table(self, params: dict) -> List[List[dict]]:
        current_eoy, previous_eoy = self._get_eoys(params)
        section_titles = self._get_section_titles(params)
        table = [self._create_table_header(current_eoy, previous_eoy, params)]

        for i, section_title in enumerate(section_titles):
            num_rows = np.random.randint(1, 9)
            section = self._create_section(
                i+1,
                section_title,
                num_rows,
                params)
            table.extend(section)

        return table

    def _get_section_titles(self, params: dict) -> List[str]:
        return random.choices(
            self._section_titles,
            k=params['num_sections'])

    def _create_table_header(
            self,
            current_eoy: str,
            previous_eoy: str,
            params: dict) -> list:
        row = [
            {
                'type': "DATA",
                'colspan': "1",
                'content': "",
                'classes': []
            },
            {
                'type': "HEADER",
                'colspan': "2" if params['double_column'] else "1",
                'content': current_eoy,
                'scope': "col",
                'classes': []
            },
            {
                'type': "HEADER",
                'colspan': "2" if params['double_column'] else "1",
                'content': previous_eoy,
                'scope': "col",
                'classes': []
            }
        ]

        if params['note_column']:
            row.insert(1, {
                'type': "HEADER",
                'colspan': "1",
                'content': params['note_column_name'],
                'scope': "col",
                'classes': []
            })

        return row

    def _create_section(
            self,
            number: int,
            title: str,
            num_rows: int,
            params: dict) -> List[List[dict]]:
        if params['numbered_sections']:
            title = f"{number}. {title}"

        if params['uppercase_sections']:
            title = title.upper()

        section = self._create_section_header(title, params)

        for i in range(num_rows):
            last_row = i == num_rows - 1
            row = self._create_row(params, last_row)
            section.append(row)

        return section

    def _create_section_header(self, title: str, params: dict):
        section_header = [
            [
                {
                    'type': "HEADER",
                    'colspan': "1",
                    'content': title,
                    'scope': "col",
                    'classes': []
                },
                {
                    'type': "DATA",
                    'colspan': "2" if params['double_column'] else "1",
                    'content': "",
                    'classes': []
                },
                {
                    'type': "DATA",
                    'colspan': "2" if params['double_column'] else "1",
                    'content': "",
                    'classes': []
                }
            ],
            [
                {
                    'type': "DATA",
                    'colspan': "1",
                    'content': "",
                    'classes': []
                },
                {
                    'type': "HEADER",
                    'colspan': "2" if params['double_column'] else "1",
                    'content': "&#163;'000" if params['thousand_factor']
                                            else "&#163;",
                    'scope': "col",
                    'classes': []
                },
                {
                    'type': "HEADER",
                    'colspan': "2" if params['double_column'] else "1",
                    'content': "&#163;'000" if params['thousand_factor']
                                            else "&#163;",
                    'scope': "col",
                    'classes': []
                }
            ]
        ]

        if params['note_column']:
            section_header[0].insert(1, {
                'type': "DATA",
                'colspan': "1",
                'content': "",
                'classes': []
            })

            section_header[1].insert(1, {
                'type': "DATA",
                'colspan': "1",
                'content': "",
                'classes': []
            })

        return section_header

    def _create_row(self, params: dict, last_row: bool):
        words = random.choices(self._vocab, k=np.random.randint(1, 5))
        negative = np.random.rand() > .8
        current_year_empty = np.random.rand() > .92 and not last_row
        last_year_empty = (np.random.rand() > .92
            and not current_year_empty
            and not last_row)

        if params['double_column']:
            row = self._get_double_col_row(
                words,
                last_row,
                negative,
                current_year_empty,
                last_year_empty,
                params)
        else:
            row = self._get_single_col_row(
                words,
                last_row,
                negative,
                current_year_empty,
                last_year_empty,
                params)

        if params['note_column']:
            if np.random.rand() > .7:
                content = str(np.random.randint(1, 11))
            else:
                content = ""

            row.insert(1, {
                'type': "DATA",
                'colspan': "1",
                'content': content,
                'classes': list(filter(lambda x: x is not None, [
                    "fw-bold" if params['note_column_bold'] else None
                ]))
            })

        return row

    def _get_single_col_row(
            self,
            words: list,
            last_row: bool,
            negative: bool,
            current_year_empty: bool,
            last_year_empty: bool,
            params: dict) -> List[dict]:

        if current_year_empty:
            current = params['no_value']
        else:
            if params['thousand_factor'] and params['max_value'] >= 1e6:
                current = f"{np.random.randint(0, 10000):,}"
            else:
                current = f"{np.random.randint(0, params['max_value']):,}"

            if negative:
                current = f"({current})"

        if last_year_empty:
            previous = params['no_value']
        else:
            if params['thousand_factor'] and params['max_value'] >= 1e6:
                previous = f"{np.random.randint(0, 10000):,}"
            else:
                previous = f"{np.random.randint(0, params['max_value']):,}"

            if negative:
                previous = f"({previous})"

        return [
            {
                'type': "HEADER",
                'colspan': "1",
                'content': " ".join(words).capitalize(),
                'scope': "row",
                'classes': []
            },
            {
                'type': "DATA",
                'colspan': "1",
                'content': current,
                'classes': list(filter(lambda x: x is not None, [
                    "fw-bold" if params['current_year_bold'] else None,
                    "total" if params['total_row'] and last_row else None
                ]))
            },
            {
                'type': "DATA",
                'colspan': "1",
                'content': previous,
                'classes': list(filter(lambda x: x is not None, [
                    "total" if params['total_row'] and last_row else None
                ]))
            }
        ]

    def _get_double_col_row(
            self,
            words: list,
            last_row: bool,
            negative: bool,
            current_year_empty: bool,
            last_year_empty: bool,
            params: dict) -> List[dict]:

        cell_1_content = self._get_double_col_content(
            current_year_empty or negative,
            negative,
            params)
        cell_2_content = self._get_double_col_content(
            current_year_empty or not negative,
            negative,
            params)
        cell_3_content = self._get_double_col_content(
            last_year_empty or negative,
            negative,
            params)
        cell_4_content = self._get_double_col_content(
            last_year_empty or not negative,
            negative,
            params)

        return [
            {
                'type': "HEADER",
                'colspan': "1",
                'content': " ".join(words).capitalize(),
                'scope': "row",
                'classes': []
            },
            {
                'type': "DATA",
                'colspan': "1",
                'content': cell_1_content,
                'classes': list(filter(lambda x: x is not None, [
                    "fw-bold" if params['current_year_bold'] else None,
                    "total" if params['total_row']
                                and last_row
                                and not negative
                            else None
                ]))
            },
            {
                'type': "DATA",
                'colspan': "1",
                'content': cell_2_content,
                'classes': list(filter(lambda x: x is not None, [
                    "fw-bold" if params['current_year_bold'] else None,
                    "total" if params['total_row']
                                and last_row
                                and negative
                            else None
                ]))
            },
            {
                'type': "DATA",
                'colspan': "1",
                'content': cell_3_content,
                'classes': list(filter(lambda x: x is not None, [
                    "total" if params['total_row']
                                and last_row
                                and not negative
                            else None
                ]))
            },
            {
                'type': "DATA",
                'colspan': "1",
                'content': cell_4_content,
                'classes': list(filter(lambda x: x is not None, [
                    "total" if params['total_row']
                                and last_row
                                and negative
                            else None
                ]))
            }
        ]

    def _get_double_col_content(
            self,
            empty: bool,
            negative: bool,
            params: dict) -> str:
        if empty:
            content = params['no_value']
        else:
            if params['thousand_factor'] and params['max_value'] >= 1e6:
                content = f"{np.random.randint(0, 10000):,}"
            else:
                content = f"{np.random.randint(0, params['max_value']):,}"

            if negative and params['bracket_negatives']:
                content = f"({content})"

        return content

    def _get_eoys(self, params: dict) -> Tuple[str]:
        current_year = np.random.randint(1970, 2023)
        previous_year = current_year - 1
        month = np.random.randint(1, 13)
        current_last_day = calendar.monthrange(current_year, month)[1]
        previous_last_day = calendar.monthrange(previous_year, month)[1]
        current_eoy_date = datetime(current_year, month, current_last_day)
        previous_eoy_date = datetime(previous_year, month, previous_last_day)
        current_eoy = current_eoy_date.strftime(params['eoy_format'])
        previous_eoy = previous_eoy_date.strftime(params['eoy_format'])

        return current_eoy, previous_eoy

    def _load_vocab(self) -> tuple:
        return tuple(words.words())
