from sqlalchemy import text
import app

def getsize():
    return float(app.db.session.execute(text('SELECT SUM(data_length + index_length) AS "size" FROM information_schema.TABLES WHERE table_schema = "' + app.Config.ENV_DB_NAME + '" GROUP BY table_schema;')).fetchall()[0][0]) 