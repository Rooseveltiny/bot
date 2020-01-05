from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

'''
Some models are presented here!
'''
class CurrentWebSite(db.Model):

    user = db.Column(db.Integer, primary_key = True)
    current_web_site = db.Column(db.String(50))

    def __repl__(self):

        return 'user is {}, and the current web site is {}'.format(self.user, self.current_web_site)

    def str(self):

        return 'user is {}, and the current web site is {}'.format(self.user, self.current_web_site)

    def users_web_site(self, type_string=False):

        if type_string:
            return self.query.filter_by(user = self.user).first().current_web_site
        return self.query.filter_by(user = self.user)

    def save(self):

        current_web_site = self.users_web_site()
        if current_web_site:
            current_web_site.update({'current_web_site': self.current_web_site})
            db.session.commit()
        else:
            db.session.add(self)
            db.session.commit()