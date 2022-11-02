# PaperSpider

### Usage
To run web scraper with default settings in `config.py`, just run `python spider.py spider`. You can manually change conference name, keywords, and year in `config.py`or run with parameters.

For example, to crawl ACL papers about dialog, conversation, and chatbot on 2019, 2020, 2021, run:
```
python spider.py spider --spiderTool='ACLSeries' --Keywords=['dialog','conversation','chatbot'] --Years=[2019, 2020, 2021] --Field='nlp' --Meeting='ACL' --path='code/PaperSpider/dataset
```

To tokenize the PDF data, run `generate_data.py`. You would get a .txt file ready for annotation.








