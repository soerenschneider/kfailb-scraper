"""
This module contains a class that parses information from the website content.
"""

import re
import logging

from bs4 import BeautifulSoup
from kfailb.kfailb_data import Raw


class InfoPageParser:
    """
    Class that's responsible of parsing K-Fail-Bs info page.
    """

    def _iterate_data(self, table):
        """
        Iterates each table's row to find current problems.
        :param table: the html table that contains the problems.
        :return: Incidents object with incidents extracted from the table.
        """
        ret = list()
        rows = table.find_all('tr')

        for row in rows:
            lines = self._extract_lines(row)
            cols = row.find_all('td')

            problem = ""
            for col in cols:
                problem += col.text.strip()

            for line in lines:
                ret.append(Raw(line, problem))

        return ret

    @staticmethod
    def _extract_lines(row):
        """
        Extracts the affected line that has the problems from the row.
        :param row: the row informing about a problem.
        :return: A list of integers representing the lines.
        """
        lines = []

        items = row.find_all('li')
        for line in items:
            try:
                lines.append(int(line.text))
            except ValueError as e:
                logging.error("Can't parse line information as int: %s", e)

        # burn after reading
        for entry in row.find_all('ul'):
            entry.decompose()

        return lines

    @staticmethod
    def _parse_table(data):
        """
        Parses the table that contains the data portion we're interested in.
        :param data: the raw website content.
        :return: the table object that the parser located inside the content.
        """
        soup = BeautifulSoup(data, 'html.parser')
        table = soup.find('table', attrs={'class': 'table'})
        return table

    def parse_data(self, data):
        """
        Entry point for scraping the info page.
        :return: Incidents object containing all the parsed incidents.
        """
        if data is None \
                or not str(data).strip():
            return list()

        table = self._parse_table(data)
        return self._iterate_data(table)
