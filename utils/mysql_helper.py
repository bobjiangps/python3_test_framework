import pymysql
import random


class MysqlHelper:

    def __init__(self, info):
        default_info = {
            "host": "localhost",
            "port": 3306,
            "charset": "utf8"
        }
        info = dict(default_info, **info)
        self.conn = pymysql.connect(host=info["host"], port=info["port"], user=info["user"], passwd=info["password"], db=info["db_name"], charset=info["charset"])
        self.cur = self.conn.cursor()

    @classmethod
    def execute_sql(cls, sql, commit=False):
        try:
            cls.cur.execute(sql)
            if commit:
                cls.conn.commit()
        except:
            cls.conn.rollback()
        finally:
            cls.close_connection()

    @classmethod
    def get_first_results_from_database(cls, sql):
        try:
            cls.cur.execute(sql)
            return cls.cur.fetchone()
        finally:
            cls.close_connection()

    @classmethod
    def get_random_results_from_database(cls, sql):
        try:
            cls.cur.execute(sql)
            result = cls.cur.fetchall()
            return result[random.randint(0, len(result)-1)]
        finally:
            cls.close_connection()

    @classmethod
    def get_all_results_from_database(cls, sql):
        try:
            cls.cur.execute(sql)
            return cls.cur.fetchall()
        finally:
            cls.close_connection()

    @classmethod
    def insert_into_database(cls, sql):
        cls.execute_sql(sql, commit=True)

    @classmethod
    def update_in_database(cls, sql):
        cls.execute_sql(sql, commit=True)

    @classmethod
    def delete_from_database(cls, sql):
        cls.execute_sql(sql, commit=True)

    @classmethod
    def close_connection(cls):
        cls.cur.close()
        cls.conn.close()
