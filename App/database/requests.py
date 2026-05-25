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
    
async def add_user(tg_id: int, name: str, price: float, start_date: str):
    # 1. Открываешь соединение через async with aiosqlite.connect(DB_PATH) as db:
        async with aiosqlite.connect(DB_PATH) as db:    
        # 2. Выполняешь команду db.execute со строкой INSERT INTO... 
        # И передаешь в нее кортеж со всеми четырьмя переменными: (tg_id, name, price, start_date)
            await db.execute("""
                INSERT INTO users (tg_id, name, price, start_date, saved_money) VALUES (?, ?, ?, ?, 0)
            """, (tg_id, name, price, start_date))
        # 3. Делаешь await db.commit(), чтобы сохранить нового курильщика
            await db.commit()