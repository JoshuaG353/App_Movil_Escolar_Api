import os

# Solo usar pymysql para MySQL en desarrollo local
# En producción (Render) con PostgreSQL, no se ejecutará
if os.environ.get('DATABASE_URL') is None:
    import pymysql
    pymysql.install_as_MySQLdb()