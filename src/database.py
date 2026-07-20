from sqlalchemy import create_engine
from src.config import DB_CONFIG
from src.logger import logger

class Database:

    def connect(self):

        connection_string = (
            f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
            f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        )

        engine = create_engine(connection_string)

        logger.info("Database Connected Successfully.")
        print("Database Connected Successfully.")

        return engine