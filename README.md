# PandasXML
PandasXML is a Python package that imports data from remote XML files into Pandas dataframes, so they can be manipulated or exported to other file formats, such as CSV. 

### Usage

```python
import pandas as pd
import pandasxml as px

df = px.xml_to_df('https://practicaldatascience.co.uk/sitemap.xml', item='url')
df.head()
```

