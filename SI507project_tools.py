import requests
import json
from bs4 import BeautifulSoup
from advanced_expiry_caching import Cache
import csv
import os
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from db_populate import *
import random

# from sqlalchemy import Column, ForeignKey, Integer, String, REAL
# from sqlalchemy.orm import relationship
######

START_URL = "https://toolkits.dss.cloud/design/"
FILENAME = "finalproject_cache.json"

PROGRAM_CACHE = Cache(FILENAME)


def access_page_data(url):
    data = PROGRAM_CACHE.get(url)
    if not data:
        data = requests.get(url).text
        PROGRAM_CACHE.set(url, data)
    return data

#######


main_page = access_page_data(START_URL)

main_soup = BeautifulSoup(main_page, features="html.parser")
hrefs = [a["href"] for a in main_soup.select('div.flip-container a[href]')]
# print(hrefs)

# clean duplicate data
seen = set()
all_links = []
for item in hrefs:
    if item not in seen:
        seen.add(item)
        all_links.append(item)
# print(all_links)

# for link in all_links:
# print(link)

page_data = access_page_data('https://toolkits.dss.cloud/design/method-card/1-on-1-interview/')
soup_of_page = BeautifulSoup(page_data, features="html.parser")

f = open("data.csv", "w")
writer = csv.DictWriter(
    f, fieldnames=["Name", "Task","Image","Time","Stage","Purpose","When","Why","Note","Output","Next"])
writer.writeheader()
f.close()

stage_list=[]
purpose_list=[]
# all info in one page
def one_page():
    name = soup_of_page.find('div',{'class':'title'}).find('h1')
    # print(name.text)


    tasks= soup_of_page.find('div',{'class':'card_text'}).find('p')
    # print(tasks.text)

    image= soup_of_page.find('div',{'class':'icon'}).find('img')
    # print(image['src'])

    time= soup_of_page.find('div',{'class':'time'}).find('h2')
    # print(time.text)


    stage= soup_of_page.find('div',{'class':'cat-left'})
    stage_string=stage['class'][1]
    stage_name=stage_string[:-4]
    # print(stage_name)
    if stage_name not in stage_list:
        stage_list.append(stage_name)

    purpose= soup_of_page.find('div',{'class':'cat-right'})
    purpose_string=purpose['class'][1]
    purpose_name=purpose_string[:-4]
    # print(purpose_name)
    if purpose_name not in purpose_list:
        purpose_list.append(purpose_name)

    #grasp data
    feature= soup_of_page.find('section',{'class':'card_ww'}).find_all('div')
    #when
    when=feature[0].find('p')
    # print(when.text)
    #why
    why=feature[1].find('p')
    # print(why.text)
    #note
    note=feature[2].find('p')
    # print(note.text)
    #output
    output=feature[3].find('p')
    # print(output.text)
    #next
    next=feature[4].find('p')
    # print(next.text)

    one_page_rows=[name.text,tasks.text,image['src'],time.text,stage_name,purpose_name,when.text,why.text,note.text,output.text,next.text]
    with open('data.csv', "a") as f:
        writer = csv.writer(f)
        writer.writerow(one_page_rows)



topics_pages = []
for l in all_links:
    page_data = access_page_data(l)
    soup_of_page = BeautifulSoup(page_data, features="html.parser")
    one_page()




##################Flask and database ###########
# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./data.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy



##### Set up Models #####

# Set up association Table
collections = db.Table('collections',db.Column('stage_id',db.Integer, db.ForeignKey('Stages.id')),db.Column('purpose_id',db.Integer, db.ForeignKey('Purposes.id')))

class Stage(db.Model):
    __tablename__ = "Stages"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    purposes = db.relationship('Purpose',secondary=collections,backref=db.backref('stages',lazy='dynamic'),lazy='dynamic')
    approaches = db.relationship('Approach',backref='stage')


class Purpose(db.Model):
    __tablename__ = "Purposes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    approaches = db.relationship('Approach',backref='purpose')
    #
    # def __repr__(self):
    #     return "{} (ID: {})".format(self.lastname, self.firstname, self.id)


class Approach(db.Model):
    __tablename__ = "Approaches"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),unique=True) # Only unique title songs can exist in this data model
    stage_id = db.Column(db.Integer, db.ForeignKey("Stages.id")) # ok to be null for now
    purpose_id = db.Column(db.Integer, db.ForeignKey("Purposes.id")) #ok to be null for now
    time = db.Column(db.String(250))
    task = db.Column(db.String(250))
    when = db.Column(db.String(250))
    why = db.Column(db.String(250))
    note = db.Column(db.String(250))
    output = db.Column(db.String(250))
    next = db.Column(db.String(250))
    image = db.Column(db.String(250))

    # def __repr__(self):
    #     return "{} by {} | {}".format(self.title,self.director_id, self.distributor_id, self.major_genre)

# print(stage_list)
# print(purpose_list)


##### Helper functions #####
#
# def get_or_create_director(director_name):
#     director = Director.query.filter_by(name=director_name).first()
#     if director:
#         return director
#     else:
#         director = Director(name=director_name)
#         session.add(director)
#         session.commit()
#         return director
#
# def get_or_create_distributor(distributor_name):
#     distributor = Distributor.query.filter_by(name=distributor_name).first()
#     if distributor:
#         return distributor
#     else:
#         distributor = Distributor(name=distributor_name)
#         session.add(distributor)
#         session.commit()
#         return distributor
#
#
# ##### Set up Controllers (route functions) #####

@app.route('/')
def index():
    approach=random.choice(Approach.query.all())
    # print(approach["name"])
    print('test')
    return render_template('index.html', random_approach=approach)



# @app.route('/movie/new/<title>/<director>/<distributor>/<major_genre>/<us_gross>/<worldwide_gross>/<us_dvd_sales>/<production_budget>/')
# def new__movie(title, director, distributor, major_genre,us_gross,worldwide_gross,us_dvd_sales,production_budget):
#     if Movie.query.filter_by(title=title).first():
#         return "That movie already exists. Go back to the main app."
#     else:
#         director = get_or_create_director(director)
#         distributor = get_or_create_distributor(distributor)
#         movie = Movie(title=title, director_id=director.id,distributor_id=distributor.id,major_genre=major_genre,us_gross=us_gross,worldwide_gross=worldwide_gross,us_dvd_sales=us_dvd_sales,production_budget=production_budget)
#         session.add(movie)
#         session.commit()
#         return "New movie: {} directed by {}, distributed by {}, has been saved in the list. More info: Major Genre: {}; US Gross: {}, Worldwide Gross: {}, US DVD Sales: {}, Production Budget: {}. ".format(movie.title, director.name,distributor.name,movie.major_genre,movie.us_gross,movie.worldwide_gross,movie.us_dvd_sales,movie.production_budget)
#
# @app.route('/')
# def index():
#     movies = Movie.query.all()
#     num_movies = len(movies)
#     return render_template('index.html', num_movies=num_movies)
#
# @app.route('/all_movies')
# def see_all():
#     all_movies = []
#     movies = Movie.query.all()
#     for i in movies:
#         all_movies.append((i.title))
#     return render_template('all_movies.html',all_movies=all_movies)
#
# @app.route('/all_directors')
# def see_director():
#     all_directors = []
#     directors = Director.query.all()
#     for i in directors:
#         all_directors.append((i.name))
#     return render_template('all_directors.html',all_directors=all_directors)
#
#
# if __name__ == '__main__':
#     db.create_all()
#     app.run()

# print("hello")



if __name__ == '__main__':
    db.create_all()
    # add_data()
    main_populate("data.csv")
    app.run()
