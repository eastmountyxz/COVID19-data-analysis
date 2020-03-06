import requests,re, csv, sys, time
from lxml import html
from fake_useragent import UserAgent

# 记录起始时间
startTime = time.time()

# 创建CSV文件，并写入表头信息
fp = open('中国社会组织_疫情防控.csv','a',newline='',encoding='utf-8-sig')
writer = csv.writer(fp)
writer.writerow(("标题", "时间", "URL", "正文内容", "来源"))

#----------------------------------------------抓取数据----------------------------------------------
def spider_html_info(url):
    try:
        headers = {
            "User-Agent" : UserAgent().chrome #chrome浏览器随机代理
        }
        response = requests.get(url=url, headers=headers).text
        text_html = html.fromstring(response)
        
        # 获取下一页链接,先其他元素获取一页链接，保证程序的强壮性
        next_url = "http://www.chinanpo.gov.cn" + text_html.xpath('/html/body/div[2]/div/ul[1]/li[2]/a[2]/@href')[0]
        print("next_url", next_url)
    
        # 获取文章标题
        article_title = text_html.xpath('//*[@id="fontinfo"]/p[2]/b[1]//text()')
        title = "".join(article_title)
        if title == "":
            title = "".join(text_html.xpath('//*[@id="fontinfo"]/p[3]/b[1]//text()'))
        print ("title = ",title)
        
        # 获取发布时间
        publish_time = text_html.xpath('/html/body/div[2]/div/ul[1]/li[3]/strong/text()')[0][5:]
        print ("publish_time = ", publish_time)
        print ("url = ", url)
        
        # 获取来源
        source_text = text_html.xpath('//*[@id="fontinfo"]/p[last()]//text()')[0]
        source = source_text[3:]
        
        # 爬取文本
        text_list = text_html.xpath('//*[@id="fontinfo"]//text()')
        article_text = "".join(text_list).replace('\r\n','').replace("\xa0", "").replace("\t", "").replace(source_text,"").replace(title, "")    
        # print ("article_text", article_text)
        # print ("source = ", source)
        writer.writerow((title, publish_time, url, article_text, source))
    except:
        pass
    
    if url == 'http://www.chinanpo.gov.cn/1944/123496/index.html':
        fp.close()
        # 获取结束时的时间
        endTime =time.time()           
        useTime =(endTime-startTime)/60
        print ("该次所获的信息一共使用%s分钟"%useTime)
        # 正常退出程序
        sys.exit(0)       
    else:
        return next_url

#----------------------------------------------主函数----------------------------------------------
def main():
    url = "http://www.chinanpo.gov.cn/1944/125177/nextindex.html" # 125177第一篇文章
    count = 1
    while True:
        print ("正在爬取第%s篇："%count, url)
        next_url = spider_html_info(url)
        url = next_url
        count = count + 1
                
if __name__ == '__main__':
    main()
