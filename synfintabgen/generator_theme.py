class ThemeGenerator():
    """This is the ThemeGenerator class."""

    def __init__(self) -> None:
        """The constructor for ThemeGenerator class."""

        self._theme_functions = [
            self._theme_0,
            self._theme_1,
            self._theme_2,
            self._theme_3,
            self._theme_4,
            self._theme_5
        ]

    def __call__(self, idx: int, params: dict) -> dict:
        """
        The call method for ThemeGenerator class.

        Parameters:
            idx (int): The index of the theme function to use.
            params (dict): The table parameters.
        """

        theme_function = self._theme_functions[idx]

        return theme_function(params)

    def _theme_0(self, params: dict) -> dict:
        theme = {
            '*, ::after, ::before': {
                'box-sizing': "border-box"
            },
            'body': {
                'margin': 0,
                'font-family': params['typeface'],
                'line-height': params['line_height']
            },
            'tr > :first-child': {
                'max-width': f"{params['row_header_max_width']}px"
            },
            'th': {
                'text-align': "inherit"
            },
            'th[scope=row]': {
                'font-weight': "inherit"
            },
            'th[scope="col"]:not(:first-child)': {
                'text-align': "center" if (params['double_column']
                    and params['double_header_centered']) else "right",
            },
            'td': {
                'min-width': f"{params['column_min_width']}px",
                'text-align': "right"
            },
            'tbody, td, th, tr': {
                'border-color': "inherit",
                'border-style': "solid",
                'border-width': "0"
            },
            '.fw-bold': {
                'font-weight': "700 !important"
            }
        }

        if params['note_column']:
            theme['tr:first-child th:first-of-type'] = {
                'text-align': "left"
            }

            theme['td:nth-child(2)'] = {
                'min-width': f"{params['note_column_min_width']}px",
                'text-align': "left"
            }

        if params['border']:
            theme['table'] = {
                'border-color': "#dee2e6"
            }

            theme['table > :not(caption) > * > *'] = {
                'border-bottom-width': "1px"
            }

        if params['total_row']:
            theme['.total'] = {
                'border-style': params['total_border_style'],
                'border-width': f"{params['total_border_width']}px 0",
                'border-color': "#000"
        }

        return theme

    def _theme_1(self, params: dict) -> dict:
        theme = {
            '*, ::after, ::before': {
                'box-sizing': "border-box"
            },
            'body': {
                'margin': 0,
                'font-family': params['typeface'],
                'font-size': params['font_size'],
                'line-height': params['line_height']
            },
            'table': {
                'border-collapse': "collapse"
            },
            'tr > :first-child': {
                'max-width': f"{params['row_header_max_width']}px"
            },
            'td': {
                'min-width': f"{params['column_min_width']}px",
                'text-align': "right"
            },
            'th, td': {
                'padding': "0.5em"
            },
            # Main heading
            'tr:first-child': {
                'background-color': "#13137c !important",
                'color': "#fff !important"
            },
            # Section heading
            'tr:has(th[scope="col"]:first-child)': {
                'background-color': "#13137c",
                'color': "#fff",
                'text-align': "left"
            },
            # Section column heading
            'tr:has(td:first-child) :not(:empty)': {
                'background-color': "#13137c",
                'color': "#fff",
                'text-align': "center" if (params['double_column']
                    and params['double_header_centered']) else "right",
            },
            # Row heading
            'th[scope="row"]': {
                'color': "#000",
                'text-align': "left"
            },
            # Aggregate row
            '.total': {
                'color': "#000",
                'font-weight': "bold"
            },
            '.fw-bold': {
                'font-weight': "700 !important"
            }
        }

        if params['note_column']:
            theme['tr:first-child th:first-of-type'] = {
                'text-align': "left !important"
            }

            theme['td:nth-child(2)'] = {
                'min-width': f"{params['note_column_min_width']}px",
                'text-align': "left !important"
            }

        return theme

    def _theme_2(self, params: dict) -> dict:
        theme = {
            '*, ::after, ::before': {
                'box-sizing': "border-box"
            },
            'body': {
                'margin': 0,
                'font-family': params['typeface'],
                'font-size': params['font_size'],
                'line-height': params['line_height']
            },
            'table': {
                'border-collapse': "collapse",
                'border': "1px solid #015402"
            },
            'tr > :first-child': {
                'max-width': f"{params['row_header_max_width']}px"
            },
            'td': {
                'min-width': f"{params['column_min_width']}px",
                'text-align': "right"
            },
            'th, td': {
                'padding': "0.5em",
                'border-width': "1px 0",
                'border-style': "solid",
                'border-color': "#015402"
            },
            # Main heading
            'tr:first-child': {
                'background-color': "#015402 !important",
                'color': "#fff !important"
            },
            # Section heading
            'tr:has(th[scope="col"]:first-child)': {
                'background-color': "#015402",
                'color': "#fff",
                'font-weight': "bold",
                'text-align': "center"
            },
            # Section column heading
            'tr:has(td:first-child)': {
                'text-align': "center" if (params['double_column']
                    and params['double_header_centered']) else "right",
            },
            # Row heading
            'th[scope="row"]': {
                'color': "#000",
                'text-align': "left"
            },
            # Aggregate row
            '.total': {
                'color': "#000",
                'font-weight': "bold"
            },
            '.fw-bold': {
                'font-weight': "700 !important"
            }
        }

        if params['note_column']:
            theme['tr:first-child th:first-of-type'] = {
                'text-align': "left !important"
            }

            theme['td:nth-child(2)'] = {
                'min-width': f"{params['note_column_min_width']}px",
                'text-align': "left !important"
            }

        return theme

    def _theme_3(self, params: dict) -> dict:
        theme = {
            '*, ::after, ::before': {
                'box-sizing': "border-box"
            },
            'body': {
                'margin': 0,
                'font-family': params['typeface'],
                'font-size': params['font_size'],
                'line-height': params['line_height']
            },
            'table': {
                'border-collapse': "collapse",
                'border': "1px solid #000"
            },
            'tr > :first-child': {
                'max-width': f"{params['row_header_max_width']}px"
            },
            'td': {
                'min-width': f"{params['column_min_width']}px",
                'text-align': "right"
            },
            'th, td': {
                'padding': "0.5em"
            },
            # Main heading
            'tr:first-child': {
                'background-color': "#808080 !important",
                'color': "#fff !important"
            },
            # Section heading
            'tr:has(th[scope="col"]:first-child)': {
                'color': "#000",
                'text-align': "left",
                'border-width': "1px 0",
                'border-style': "solid"
            },
            # Section column heading
            'tr:has(td:first-child)': {
                'text-align': "center" if (params['double_column']
                    and params['double_header_centered']) else "right",
            },
            # Row heading
            'th[scope="row"]': {
                'color': "#000",
                'text-align': "left"
            },
            # Aggregate row
            '.total': {
                'color': "#000",
                'font-weight': "bold"
            },
            '.fw-bold': {
                'font-weight': "700 !important"
            }
        }

        if params['note_column']:
            theme['tr:first-child th:first-of-type'] = {
                'text-align': "left !important"
            }

            theme['td:nth-child(2)'] = {
                'min-width': f"{params['note_column_min_width']}px",
                'text-align': "left !important"
            }

        return theme

    def _theme_4(self, params: dict) -> dict:
        theme = {
            '*, ::after, ::before': {
                'box-sizing': "border-box"
            },
            'body': {
                'margin': 0,
                'font-family': params['typeface'],
                'font-size': params['font_size'],
                'line-height': params['line_height']
            },
            'table': {
                'border-collapse': "collapse",
                'background-color': "#faebd7",
                'border': "1px solid #000"
            },
            'tr > :first-child': {
                'max-width': f"{params['row_header_max_width']}px"
            },
            'td': {
                'min-width': f"{params['column_min_width']}px",
                'text-align': "right"
            },
            'th, td': {
                'padding': "0.5em"
            },
            # Main heading
            'tr:first-child': {
                'background-color': "#774a1c !important",
                'color': "#fff !important"
            },
            # Section heading
            'tr:has(th[scope="col"]:first-child)': {
                'text-align': "left",
                'border-width': "1px 0",
                'border-style': "solid",
                'border-color': "#000"
            },
            # Section column heading
            'tr:has(td:first-child)': {
                'background-color': "#b88858",
                'text-align': "center" if (params['double_column']
                    and params['double_header_centered']) else "right",
            },
            # Row heading
            'th[scope="row"]': {
                'color': "#000",
                'text-align': "left"
            },
            # Aggregate row
            '.total': {
                'color': "#000",
                'font-weight': "bold"
            },
            '.fw-bold': {
                'font-weight': "700 !important"
            }
        }

        if params['note_column']:
            theme['tr:first-child th:first-of-type'] = {
                'text-align': "left !important"
            }

            theme['td:nth-child(2)'] = {
                'min-width': f"{params['note_column_min_width']}px",
                'text-align': "left !important"
            }

        return theme

    def _theme_5(self, params: dict) -> dict:
        theme = {
            '*, ::after, ::before': {
                'box-sizing': "border-box"
            },
            'body': {
                'margin': 0,
                'font-family': params['typeface'],
                'font-size': params['font_size'],
                'line-height': params['line_height']
            },
            'table': {
                'border-collapse': "collapse"
            },
            'tr > :first-child': {
                'max-width': f"{params['row_header_max_width']}px"
            },
            'td': {
                'min-width': f"{params['column_min_width']}px",
                'text-align': "right"
            },
            'th, td': {
                'padding': "0.5em",
                'border-bottom': "1px solid"
            },
            # Section heading
            'tr:has(th[scope="col"]:first-child) > *': {
                'border-top': "3px solid #efc51e",
                'border-bottom': "0",
                'text-align': "left"
            },
            # Section column heading
            'tr:has(td:first-child)': {
                'border-bottom': "2px solid #000",
                'text-align': "center" if (params['double_column']
                    and params['double_header_centered']) else "right",
            },
            # Row heading
            'th[scope="row"]': {
                'color': "#000",
                'text-align': "left"
            },
            # Aggregate row
            '.total': {
                'color': "#000",
                'font-weight': "bold"
            },
            '.fw-bold': {
                'font-weight': "700 !important"
            }
        }

        if params['note_column']:
            theme['tr:first-child th:first-of-type'] = {
                'text-align': "left !important"
            }

            theme['td:nth-child(2)'] = {
                'min-width': f"{params['note_column_min_width']}px",
                'text-align': "left !important"
            }

        return theme
