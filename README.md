# Project Title

UX Design and Research Method toolkit

[Link to this repository](https://github.com/BingqingShan/507_finalproject)

---

## Project Description

My project creates a toolkit of UX Design/Research methods. This toolkit can show user a list of design and research methods to help them choose the right one they need in their design and research process. There are 3 routes users can explore. 1)The homepage will randomly select one design/research method and show it on the homepage. By clicking on the button, users will see details of the method. 2)All the methods will be shown on the 2nd route: "/all". 3)The 3rd route will have a form that users can use to add methods into our database and show it on the 2nd route.  

## How to run

1. First, you should install all requirements with `pip install -r requirements.txt`
2. Second, you should run `python SI507project_tests.py runserver`, and copy the route in your terminal to your browser
3. Third, try out different routes: / (home page);  /form;  /all.


## How to use
There are 3 ways of utilizing this toolkit.
1. The homepage can generate a random design/research method. Test if you are familiar with it! If not, it is time to learn a new method now. You can click on the button to see details about the method.
2. If you are doing a project and wondering what method you shall use, you can go to the second route to see different methods.
3. If you have some methods that this toolkit doesn't cover, feel free to add them by submitting a form to our database!

## Routes in this application
- `/ (home page)` -> this is the home page, on which only one random method will be shown
- `/all` -> this route will show all Design and Research methods to you
- `/form` -> this route has a form for user to input new method into the database

## How to run tests
1. First, access the repository and download the file SI507project_tests.py along with other files
2. Second, run file SI507project_tests.py in terminal through commend "python -m unittest SI507project_tests.py"

## In this repository:
- templates
  - index.html
  - all.html
  - form.html
  - formresult.html
- SI507project_tools.py
- SI507project_tests.py
- requirements.txt
- README.md
- diagram.jpg
- advanced_expiry_caching.py
- data.db
- data.csv
- db_populate.py
- finalproject_cache.json

---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [x] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [x] Project includes at least 1 test suite file with reasonable tests in it
- [x] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [ ] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [x] A many-to-many relationship in your database structure
- [x] At least one form in your Flask application
- [x] Templating in your Flask application
- [x] Inclusion of JavaScript files in the application
- [x] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [x] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [ ] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [x] Caching of data you continually retrieve from the internet in some way

### Submission
- [x] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [x] I included a summary of my project and how I thought it went **in my Canvas submission**!
