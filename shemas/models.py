from mongoengine import Document, connect, StringField, EmailField

connect("Hours")


class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    email = EmailField(required=True)

    def __str__(self):
        return self.username