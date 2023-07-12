from flask import Flask
from .database import get_db_connection

app = Flask(__name__)


@app.route('/')
def index():
    """
    Showing all subpaths and their count as stores in database
    """
    conn = get_db_connection()
    subpaths = conn.execute('SELECT subpath, count FROM subpaths').fetchall()
    conn.close()

    return {
        "status": "OK",
        "data": {subpath: count for subpath, count in subpaths}
    }


@app.route('/<subpath>')
def register(subpath):
    """
    TODO: save `subpath` in database or increment it's count when
          it already exists.
    """

    conn = get_db_connection()
    subpaths = conn.execute('SELECT subpath, count FROM subpaths WHERE subpath == "' + subpath + '"').fetchall()

    if subpaths: # List not empty
        conn.execute('UPDATE subpaths SET count = count + 1 WHERE subpath == "' + subpath + '"')
        conn.commit()
        conn.close()

        return {
            "status": "+1"
        }
    else: # List empty
        conn.execute('INSERT INTO subpaths (subpath, count) VALUES ("' + subpath + '", 1)')
        conn.commit()
        conn.close()

        return {
            "status": "New subpath",
        }