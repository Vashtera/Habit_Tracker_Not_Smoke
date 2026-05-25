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