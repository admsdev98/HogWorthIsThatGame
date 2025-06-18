from backend.db.sqlite import Database

DB_NAME = "hwitg.db"

def create_steam_games_table():
    db = Database(DB_NAME)
    db.cursor.execute("""
        CREATE TABLE IF NOT EXISTS steam_games (
            appid INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    db.con.commit()
    db.close()
    print("Tabla 'steam_games' creada (o ya existía).")

if __name__ == "__main__":
    create_steam_games_table()
