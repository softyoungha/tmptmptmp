import pymysql
import pandas as pd


def get_connection():
    return pymysql.connect(
        host='13.124.136.61',
        port=9306,
        user='aims',
        password='Cnxaims321!',
        database='test'
    )


def execute_sql(sql: str):
    conn = get_connection()

    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        conn.rollback()
        raise
    else:
        conn.commit()
    finally:
        conn.close()

    return result


def df_from_query(sql: str):
    conn = get_connection()
    return pd.read_sql(sql, con=conn)
