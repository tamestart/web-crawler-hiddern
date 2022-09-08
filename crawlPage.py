from html.parser import HTMLParser



class crawlPage(HTMLParser):

    def __init__(self,  page):
        super().__init__()
        self.links = set()
        self.feed(page)



    def handle_starttag(self, tag, attrs):
        print(tag)
        if tag == "a":
            for(attribute, value) in attrs:
                if attribute == "href":
                    self.links.add(value)

        if tag == "meta":
            print(attrs)

    def return_links(self):
        return self.links

    def error(self, message):
        pass
