# PandasXML
PandasXML is a Python package that imports data from remote XML files into Pandas dataframes, so they can be manipulated or exported to other file formats, such as CSV. 

### Installation
You can install PandasXML by running the following command in your terminal:

```commandline
pip3 install git+https://github.com/practical-data-science/PandasXML.git
```

### Usage
Install the package and then import `pandasxml` as `px`. Pass the URL of the remote XML file to `px.read_xml()` to read the data into a Pandas dataframe.

By default, the `read_xml()` function expects elements to be named `item`, but you can define the element name using the `element_name` parameter.

```python
import pandas as pd
import pandasxml as px

df = px.read_xml('https://practicaldatascience.co.uk/sitemap.xml', element_name='url')
df.head()
```

