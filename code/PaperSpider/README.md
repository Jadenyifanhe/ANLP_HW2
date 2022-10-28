# PaperSpider

This NLP paper crawling pipeline work as follows:

1) Construct dblp query url (including literature keywords, conference name, year), crawl the page corresponding to the url, and parse out the page url of each paper.

2) Crawl the page corresponding to the url of each paper, and parse out the download link corresponding to the pdf of each paper.

3) Crawl the pdf of each paper and save it in the specified local space.


# Usage
1）打开命令行，进入spider.py文件所在的路径下。

2）执行以下命令：

python spider.py spider  #此时将使用config.py中的默认配置

可以在config.py中修改配置，再次运行上面的命令。也可以在命令行传入新的参数对其进行覆盖：


#爬取ACL
```
python spider.py spider --spiderTool='ACLSeries' --Keywords=['dialog','conversation','chatbot'] --Years=[2019] --Field='对话' --Meeting='ACL' --path='/Users/apple/Desktop' 
```

#爬取EMNLP
python spider.py spider --spiderTool='ACLSeries' --Keywords=['dialog','conversation','chatbot'] --Years=[2016,2017,2018,2019] --Field='对话' --Meeting='EMNLP' --path='/Users/apple/Desktop' 
 
#爬取AAAI会议论文
python spider.py spider --spiderTool='AAAI' --Keywords=['dialog','conversation','chatbot'] --Years=[2016,2017,2018,2019] --Field='对话' --Meeting='AAAI' --path='/Users/apple/Desktop' 

#爬取IJCAI会议论文
python spider.py spider --spiderTool='IJCAI' --Keywords=['dialog','conversation','chatbot'] --Years=[2016,2017,2018,2019] --Field='对话' --Meeting='IJCAI' --path='/Users/apple/Desktop' 









