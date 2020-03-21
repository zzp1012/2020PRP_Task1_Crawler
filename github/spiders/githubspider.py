import scrapy

from github.items import GithubItem

from bs4 import BeautifulSoup

class GithubspiderSpider(scrapy.Spider):
    name = 'githubspider'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/search?q=machine+learning/']

    def parse(self, response):
        soup = BeautifulSoup(response.body, "html5lib")

        for item in soup.find_all('li',{"class":"repo-list-item hx_hit-repo d-flex flex-justify-start py-4 public source"}):
            project = GithubItem()
            try:
                project_title = item.find('a', {"class":"v-align-middle"}).get('href')
                project['project_name'] = project_title.split('/')[2]
                project['author'] = project_title.split('/')[1]
                project['url'] = self.allowed_domains[0] + project_title
            except:
                project['project_name'] = "NAN"
                project['author'] = "NAN"
                project['url'] = "NAN"

            try:
                project['language'] = item.find("span", {"itemprop":"programmingLanguage" }).get_text()
            except:
                project['language'] = 'NAN'

            try:
                project['star'] = item.find('a',{"class":"muted-link"}).get_text().split('\n')[2].replace(" ", "");
            except:
                project['star'] = "NAN"

            try:
                project['date'] = item.find('relative-time').get_text()
            except:
                project['date'] = "NAN"
            
            yield project
        
        next_url = soup.find('a',{"rel":"next"}).get('href')
        if next_url is not None:    
            url = 'https://github.com' + next_url
            yield scrapy.Request(url=url, callback=self.parse)