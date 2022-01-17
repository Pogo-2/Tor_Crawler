from bs4 import BeautifulSoup
import urllib.parse as up


class WebSite:
    def __init__(self, url, response=None):
        self.url = url
        self.response = response
        self.soup = self.get_soup()
        self.title = self.get_title()
        self.domain = self.check_domain()
        self.href_urls = []
        self.content_urls = []

    def get_soup(self):
        try:
            return BeautifulSoup(self.response, features="html.parser")
        except:
            return None

    def check_domain(self):
        try:
            return up.urlparse(self.url).netloc
        except:
            return None

    def get_href_values(self):
        if not self.soup:
            return

        for a in self.soup.find_all('a', href=True):
            self.href_urls.append(a['href'])

    def get_title(self):
        try:
            return self.soup.find("title").text
        except:
            return None

    def get_in_page_links(self):
        page = self.soup.text.split()
        for word in page:
            if word.endswith(".onion") or word.endswith(".onion/"):
                self.content_urls.append(word)

    def clean_lists(self):
        final_list = []

        for url in self.href_urls:
            try:
                value = up.urlparse(url)
                clean_url = value[0] + "://" + value.netloc


                if clean_url not in final_list and value.netloc.endswith(".onion"):
                    final_list.append(clean_url)
            except:
                print(f"could not find a domain for url: {url}")

        for url in self.content_urls:
            try:
                value = up.urlparse(url)
                clean_url = value[0] + "://" + value.netloc

                if clean_url not in final_list and value.netloc.endswith(".onion"):
                    final_list.append(clean_url)
            except:
                print(f"could not find a domain for url: {url}")

        return final_list

    def scrape_site(self):
        self.get_href_values()
        self.get_in_page_links()
        return self.clean_lists()
