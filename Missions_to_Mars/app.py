# import dependancies
from flask import Flask, render_template, redirect
from scrape_mars import Mars_Scraper
# import pymongo 
# conn = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)

# # Declare the database
# db = client.scraper_db

# # Declare the collection
# collection = db.scraper_db

# Create an app, being sure to pass __name__
app = Flask(__name__)

#Define what to do when a user hits the index route
@app.route("/")
def home():
    scrape_data = collection.find()
    return render_template('index.html', scrape_data)

# Define what to do when a user hits the /about route
@app.route("/scrape")
def scrape():
    html_scraper = Mars_Scraper()
    scraper_dict = html_scraper.scrape()
    collection.insert_one(scraper_dict)

    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


if __name__ == "__main__":
    app.run(debug=True)
