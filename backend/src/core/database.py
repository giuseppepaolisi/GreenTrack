import psycopg2
from psycopg2 import pool
from dotenv import load_dotenv
import os

load_dotenv()

class DBManager:
    
    def __init__(self):
        self._pool = None
        
    def create_connection(self):
        try:
            if not self._pool:
                self._pool = pool.SimpleConnectionPool(
                    1,
                    10,
                    database=os.getenv("DB_NAME"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD"),
                    host=os.getenv("DB_HOST"),
                    port=os.getenv("DB_PORT", 5432)
                )
        except Exception as e:
            raise e
        
    def get_conn(self):
        try:
            conn = self._pool.getconn()

            yield conn
            
            conn.commit()
        except Exception as e:
            conn.rollback()
            print("Errore connessione", e)
        finally:
            self._pool.putconn(conn)
            
    def close_all(self):
        self._pool.closeall()
        
    def init_db(self, schema_file="init.sql"):
        current_dir = os.path.dirname(__file__) 
        file_path = os.path.join(current_dir, schema_file)
        conn = self._pool.getconn() # Prende una connessione dal pool
        try:
            with conn.cursor() as cur:
                with open(file_path, "r") as f:
                    cur.execute(f.read())
                conn.commit()
                print("Database inizializzato con successo.")
        except Exception as e:
            print(f"Errore inizializzazione DB: {e}")
            conn.rollback()
        finally:
            self._pool.putconn(conn)
            
            
db_manager = DBManager()

if __name__ == "__main__":
    db_manager.create_connection()
    conn = db_manager.get_conn()