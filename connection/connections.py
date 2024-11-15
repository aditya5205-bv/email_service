from redis import Redis
from connection.MySqlConnection import MySqlConnection
from settings import DB_CONFIG, REDIS_CONFIG

db_connection = MySqlConnection(DB_CONFIG)

redis_connection = Redis(**REDIS_CONFIG)
