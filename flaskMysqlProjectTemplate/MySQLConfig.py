# config.py

# MySQL Configuration (Replace with your database details)
# Change to the same config in docker-compose.yml if using docker compose
class MySQLConfig:
    HOST = 'db'   # ip address if remote server; service name (db) if using docker compose
    USER = 'haoliu'
    PASSWORD = 'csit355_root'
    DATABASE = 'CSIT355'
