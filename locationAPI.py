import pymysql
from   datetime import datetime 

from flask import (
    Flask,
    render_template
)

# Create the application instance
app = Flask(__name__, template_folder="templates")

def dbConnecttest(type):
    result = type
    return (result)

def dbConnect(type):
    connection = pymysql.connect(host='192.168.0.17',
                                 user='dave',
                                 password='Radius534!',
                                 db='locationdb',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    if type == "add": #Add a new record into the db
        try:
            with connection.cursor() as cursor:
                #Create
                timenow = str(datetime.now())
                sql = "INSERT INTO `location` (`longit`, `lat`,'time') VALUES (%s, %s, %s)"
                cursor.execute(sql, ('long', 'lat', timenow))
            connection.commit()
        finally:
            connection.close()
    elif type == "read": #Read a record from the db
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `lat`, `longit`,'time' FROM `location`" #WHERE `email`=%s"
                #cursor.execute(sql, ('webmaster@python.org',))
                cursor.execute(sql)
                result = cursor.fetchone()
                print(result) 
                return (result)
        finally:
            connection.close()        
    elif type == "delete": #Delete the records from the DB 
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
                cursor.execute(sql, ('webmaster@python.org',))
                result = cursor.fetchone()
                print(result)    
        finally:
            connection.close()
    else:
        connection.close()        
                
                    
# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

@app.route('/current', endpoint='current')
def current():
    #currentrec = dbConnecttest('read')   
    currentrec = dbConnect('read')
    return currentrec

@app.route('/update/<lat>/<long>', endpoint='add')
def add(lat,long):
    #currentrec = dbConnecttest('read')
    currentrec = dbConnect("add",lat,long)
    return currentrec

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)