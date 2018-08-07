from googlesearch import search


class siph0n(object):
    def search(self, data):
        query = 'site:siph0n.net' + '"' + str(data) + '"'

        return search(query, stop=50)

