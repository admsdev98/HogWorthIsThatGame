import sqlite3

class Database:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.cursor = self.con.cursor()

    def select(self, table, params=None):
        sql = f"SELECT * FROM {table}"
        values = []
        conditions = []

        if params:
            for param in params:
                conditions.append(f"{param['cond']} = ?")
                values.append(param['value'])

            sql += " WHERE " + " AND ".join(conditions)

        try:
            result = self.cursor.execute(sql, values).fetchall()
            return result if result else []
        except Exception as e:
            print(f"Error occurred: {e}")
            return []

    def insert_many(self, table, columns, values_list):
        placeholders = ", ".join(["?"] * len(columns))
        columns_formatted = ", ".join(columns)
        sql = f"INSERT OR REPLACE INTO {table} ({columns_formatted}) VALUES ({placeholders})"

        try:
            self.cursor.executemany(sql, values_list)
            self.con.commit()
            return True
        except Exception as e:
            print(f"Error inserting data: {e}")
            return False

    def close(self):
        self.con.close()
