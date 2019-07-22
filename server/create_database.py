import sqlite3

import server


ADD_EXAMPLE_WEIGHT_VALUES_QUERY = """INSERT INTO """ + server.TABLE_NAME + """
    (hour, minute, second, day, month, year, weight)
    VALUES
    (22, 37, 16, 25, 5, 2019, 73.4),
    (20, 12, 12, 1, 6, 2019, 73.5),
    (21, 35, 45, 6, 6, 2019, 73.2),
    (22, 45, 37, 15, 6, 2019, 74.1)
    """

SELECT_QUERY = "SELECT * FROM " + server.TABLE_NAME


def create_database():
    try:
        return sqlite3.connect(server.DATABASE)
    except Exception as e:
        print(e)

def get_cursor():
    return sqlite3.connect(server.DATABASE).cursor()

def create_weight_values_table(con):
    con.cursor().execute(server.CREATE_TABLE_QUERY)

def add_example_weight_values(con):
    con.cursor().execute(ADD_EXAMPLE_WEIGHT_VALUES_QUERY)

def print_all_weight_values(con):
    cur = con.cursor()
    cur.execute(SELECT_QUERY)
    weight_values = cur.fetchall()
    for weight_value in weight_values:
        print(weight_value)


if __name__ == "__main__":
    with server.flask_server.app_context():
        create_database()
        try:
            server.get_db().cursor().execute(server.CREATE_TABLE_QUERY)
        except Exception as e :
            print(e)
