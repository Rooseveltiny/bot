from app import db

class CurrentWebSite(db.Model):

    user = db.Column(db.Integer, primary_key = True)
    current_web_site = db.Column(db.String(50))

    def __repl__(self):

        return 'user is {}, and the current web site is {}'.format(self.user, self.current_web_site)

    def str(self):

        return 'user is {}, and the current web site is {}'.format(self.user, self.current_web_site)


if __name__ == "__main__":
   
    db.create_all()
