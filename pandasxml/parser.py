import typing
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup


def get_xml(url):
    """Scrapes an XML feed from the provided URL and returns XML source.

    Args:
        url (string): Fully qualified URL pointing to XML feed.

    Returns:
        source (string): XML source of scraped feed.
    """

    try:
        response = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla'}))
        xml = BeautifulSoup(response, 'lxml-xml', from_encoding=response.info().get_param('charset'))
        return xml
    except Exception as e:
        print('Error: ' + str(e))
        exit()


def get_elements(xml, item='item'):
    """ Returns a list of elements in the XML feed.

    Args:
        xml (string): Beautiful Soup XML object from get_xml() function.
        item (string): Element to search for. Default is 'item'.

    Returns:
        elements (list): List of elements in the XML feed.
    """

    try:
        items = xml.find_all(item)

        print(items)

        elements = [element.name for element in items[0].find_all()]
        return elements
    except Exception as e:
        print('Error: ' + str(e))


def xml_to_df(url, item='item'):
    """Converts XML feed to a Pandas DataFrame.

    Args:
        url (string): Fully qualified URL pointing to XML feed.
        item (string): Element to search for. Default is 'item'.

    Returns:
        df (DataFrame): Pandas DataFrame of XML feed.
    """

    xml = get_xml(url)
    elements = get_elements(xml)
    print('Elements=', elements)

    if isinstance(elements, typing.List):
        df = pd.DataFrame(columns=elements)

        items = xml.find_all(item)

        for item in items:
            row = {}
            for element in elements:
                if xml.find(element):
                    if item.find(element):
                        row[element] = item.findNext(element).text
                    else:
                        row[element] = ''
                else:
                    row[element] = ''

            df = pd.concat([df, pd.DataFrame.from_records([row])])
        return df
