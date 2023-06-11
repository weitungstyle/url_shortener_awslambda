from random import choice
import string


class URL_model(object):
    def __init__(self, original_url):
        self.original_url = original_url
        self.short_url = self.generate()
        self.fields = {"original_url": "string", "short_url": "string"}
        self.create_required_fields = ['original_url']

    def generate(self):
        collection = string.ascii_letters + string.digits
        short_url = ''.join(choice(collection) for i in range(6))
        return short_url

    def validator(self):
        pass
