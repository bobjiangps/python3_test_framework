from configuration.config import LoadConfig
import pymysql
import random


class MysqlHelper:

    def __init__(self, info):
        default_info = {
            "host": "localhost",
            "port": 3306,
            "charset": "utf8"
        }
        self.info = dict(default_info, **info)
        self.conn = None
        self.cur = None

    def get_cur(self):
        self.conn = pymysql.connect(host=self.info["host"], port=self.info["port"], user=self.info["username"], passwd=str(self.info["password"]), db=self.info["dbname"], charset=self.info["charset"])
        self.cur = self.conn.cursor()

    def execute_sql(self, sql, commit=False):
        try:
            self.get_cur()
            self.cur.execute(sql)
            if commit:
                self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            self.close_connection()

    def get_first_result_from_database(self, sql):
        try:
            self.get_cur()
            self.cur.execute(sql)
            # return dict
            return self.__convert_one_result_to_dict(self.cur.fetchone())
        finally:
            self.close_connection()

    def get_random_result_from_database(self, sql):
        try:
            self.get_cur()
            self.cur.execute(sql)
            result = self.cur.fetchall()
            # return dict
            return self.__convert_one_result_to_dict(result[random.randint(0, len(result)-1)])
        finally:
            self.close_connection()

    def get_all_results_from_database(self, sql):
        try:
            self.get_cur()
            self.cur.execute(sql)
            # return list
            return self.__convert_all_results_to_list(self.cur.fetchall())
        finally:
            self.close_connection()

    def insert_into_database(self, sql):
        self.execute_sql(sql, commit=True)

    def update_in_database(self, sql):
        self.execute_sql(sql, commit=True)

    def delete_from_database(self, sql):
        self.execute_sql(sql, commit=True)

    def close_connection(self):
        if self.cur:
            self.cur.close()
            self.cur = None
        if self.conn:
            self.conn.close()
            self.conn = None

    def __convert_all_results_to_list(self, results):
        column = self.cur.description
        return [dict(zip(map(lambda x: x[0], column), row)) for row in results]

    def __convert_one_result_to_dict(self, result):
        fields = map(lambda x: x[0], self.cur.description)
        return dict(zip(fields, result))


class MysqlConnection:

    def __init__(self):
        self.env_config = LoadConfig.load_config()["env"]

    def connect(self, name):
        return MysqlHelper(self.env_config[name])
