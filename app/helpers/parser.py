

class parsing():
    def parse_dom(self, domain):
        return domain[:domain.find('.')]

    def parse_email(self, email):
        return email.split('@')[0]