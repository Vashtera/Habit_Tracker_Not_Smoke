import aiosqlite

DB_PATH = "App/database/habit_tracker.db"

async def create_tables():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                tg_id INTEGER UNIQUE,
                name TEXT,
                price REAL,
                start_date TEXT,
                saved_money REAL             
            )
        """)
        await db.commit()