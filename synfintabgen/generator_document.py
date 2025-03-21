from typing import List

from htmltree import (HtmlElement, Body, Head, Html, Meta, Style, Title, Table,
                      Tr, Th, Td, Span)


class DocumentGenerator():
    """This is a class for creating documents."""

    def __init__(self, html_dir: str) -> None:
        """
        The constructor for DocumentGenerator class.

        Parameters:
            html_dir (str): The HTML file directory.
        """

        self._html_dir = html_dir

    def __call__(self, id: str, table: List[List[dict]], theme: dict) -> str:
        """
        The call method for DocumentGenerator class.

        Parameters:
            id (str): The ID of the document to be created.
            table (List[List[dict]]): The data to be turned into a table
                in a document.
            theme (dict): The document's theme (a CSS-like dict).

        Returns:
            str: The file path of the HTML document.
        """

        return self._create_html_document(id, table, theme)

    def _create_html_document(
            self,
            id: str,
            table: List[List[dict]],
            theme: dict) -> str:
        html_table = self._create_html_table(table)
        doc_head = self._create_html_head(id, theme)
        doc_body = Body(html_table)
        doc = Html(doc_head, doc_body, lang="en")

        return doc.renderToFile(f"{self._html_dir}/{id}.html")

    def _create_html_head(self, id: str, theme: dict) -> HtmlElement:
        charset_meta = Meta(charset="utf-8")
        viewport_meta = Meta(
            name="viewport",
            content="width=device-width, initial-scale=1")
        style = Style(**theme)
        title = Title(id)

        return Head(charset_meta, viewport_meta, style, title)

    def _create_html_table(self, table: List[List[dict]]) -> HtmlElement:
        html_table = Table(id="t0")

        for i, row in enumerate(table):
            table_row = Tr(id=f"t0:r{i}")

            for j, col in enumerate(row):
                if col['type'] == "HEADER":
                    table_row_col = Th(
                        id=f"t0:r{i}:c{j}",
                        colspan=col['colspan'],
                        scope=col['scope'])
                else:
                    table_row_col = Td(
                        id=f"t0:r{i}:c{j}",
                        colspan=col['colspan'])

                if len(col['classes']) > 0:
                    table_row_col.A.update({'class': col['classes']})

                for k, word in enumerate(col['content'].split()):
                    table_row_col.C.extend([
                        Span(word, id=f"t0:r{i}:c{j}:w{k}"), " "
                    ])

                table_row.C.append(table_row_col)

            html_table.C.append(table_row)

        return html_table
