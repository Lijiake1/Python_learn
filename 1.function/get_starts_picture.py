# Python学习
# 学习时间：2022/10/1 20:51
import os
from icrawler.builtin import BingImageCrawler
path = r'F:\data\korea_images'
f = open('starName_korea.txt', 'r', encoding='gbk')
lines = f.readlines()
for i, line in enumerate(lines):
    name = line.strip('\n')

    file_path = os.path.join(path, name)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    bing_storage = {'root_dir': file_path}
    bing_crawler = BingImageCrawler(parser_threads=2, downloader_threads=4, storage=bing_storage)
    bing_crawler.crawl(keyword=name, max_num=25)
    print('第{}位明星：{}'.format(i, name))
