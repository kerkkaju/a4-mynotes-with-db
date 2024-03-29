from random import randint
import web
render = web.template.render('templates/')
urls = (
    '/', 'Home',
)

# Connect to db:
db = web.database(
    dbn='mysql',
    host='127.0.0.1',
    port=3306,
    user='root',
    pw='',
    db='db_mynotes_XXX',    # Replace with the real db name!
)

class Home:
    def GET(self):
        notes = db.select('notes')
        return render.home(notes)   # the template name
    
    def POST(self):
        i = web.input()
        # etc ...
            
class Newnote:
    def GET(self):
        return render.note_new()


if __name__ == "__main__":
    myapp = web.application(urls, globals())
    myapp.run() 
