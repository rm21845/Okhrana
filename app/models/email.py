import emailahoy


class emailahoy(object):
    """check if email exists"""
    def verify(self, email):
        return emailahoy.verify_email_address(str(email))