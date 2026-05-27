import aiosqlite
from App.database.db import DB_PATH  # Импортируем путь к нашей БД

async def get_user_by_tg_id(tg_id: int):
    # 1. Открываем соединение с базой через async with aiosqlite.connect...
    async with aiosqlite.connect(DB_PATH) as db:
        # 2. Выполняем SQL запрос SELECT и сохраняем в переменную-курсор.
        # Не забудь, что кортеж аргументов с одним элементом пишется как (tg_id,)
        cursor = await db.execute("""
            SELECT * FROM users WHERE tg_id = ?
        """, (tg_id,))
        # 3. Читаем строку через await cursor.fetchone()
        user = await cursor.fetchone()
        # 4. Возвращаем полученную строку (или None)
        return user
    
async def add_user(
          tg_id: int, 
          name: str, 
          price: float, 
          start_date: str, 
          cigarettes_in_pack: int, 
          cigarettes_per_day: int):
    # 1. Открываем соединение через async with aiosqlite.connect(DB_PATH) as db:
        async with aiosqlite.connect(DB_PATH) as db:    
        # 2. Выполняем команду db.execute со строкой INSERT INTO... 
        # И передаем в нее кортеж со всеми переменными
            await db.execute("""
                INSERT INTO users (
                             tg_id, 
                             name, 
                             price, 
                             start_date, 
                             saved_money, 
                             cigarettes_in_pack,
                             cigarettes_per_day
                             ) 
                VALUES (?, ?, ?, ?, 0, ?, ?)
            """, (tg_id, name, price, start_date, cigarettes_in_pack, cigarettes_per_day))
        # 3. Делаем await db.commit(), чтобы сохранить нового курильщика
            await db.commit()

async def change_price_in_db(tg_id: int, new_price: float, new_date, new_balance: float):
    async with aiosqlite.connect(DB_PATH) as db:
            await db.execute(""" 
                UPDATE users SET 
                                price = ?,
                                price_change_date = ?,
                                saved_money = ?
                                WHERE tg_id = ?   
            """, (new_price, new_date, new_balance, tg_id))
            await db.commit()

async def reset_user_progress(tg_id: int, new_date):
    async with aiosqlite.connect(DB_PATH) as db:
            await db.execute("""
                UPDATE users SET
                            saved_money = 0,
                            start_date = ?,
                            price_change_date = ?
                            WHERE tg_id = ?
            """, (new_date, new_date, tg_id))
            await db.commit()