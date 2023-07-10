# path-logger

Minimal Flask application for testing and evaluating
candidate Python skills and their ability to understand
new packages, documentation and computer science skills.

Setup
=====

Install Python dependencies from requirements.txt file with:

```
    pip3 install requirements.txt
```


Run the Application
===================

Once all requirements are installed you can run the service with:

```
    python3 -m flask --app app/server run
```

Now open a browser and to go `http://127.0.0.1:5000` 


Assignment
==========

The application has two endpoints, `/` root and `/<subpath`. The subpath endpoint in `server.py` file is where you will have to work. The syntax `<subpath>` in the `app.route` decorator is capturing any string passed to the URL: `http://127.0.0.1:5000/<subpath>`. A quik introduction to Flask can be found here: https://flask.palletsprojects.com/en/2.3.x/quickstart/.

The purpose of the assignment is for you to work on both files `server.py` and `database.py`. You will have to make the nnecessary changes to the application's code so start storing and counting how many times a given `subpath` string is being passed to the URL `http://127.0.0.1:5000/<subpath>`. You will also need to write a bit of SQL code to store and find subpath strings in the database. The assignment code is already using an in-memory database SQLite, you can read about the python intregration here: https://docs.python.org/3/library/sqlite3.html.

In fewer words, the application is expected to work on as follows:

1) Run the application
2) Open a browser and navigate (make a request) to http://127.0.0.1:5000/foo
3) Now navigate to http://127.0.0.1:5000/bar
4) Now navigate to http://127.0.0.1:5000/baz
5) Now navigate to http://127.0.0.1:5000 and in the JSON response you should see the folling structure:

```
{
    "data": {"foo": 1, "bar": 1, "baz": 1}
}
```

assignment submission
---------------------

You can either fork and create a Pull-request with your changes to this repository or email a zipped version of the code.

Happy coding !