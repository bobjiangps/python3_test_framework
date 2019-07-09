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
        info = dict(default_info, **info)
        self.conn = pymysql.connect(host=info["host"], port=info["port"], user=info["username"], passwd=str(info["password"]), db=info["dbname"], charset=info["charset"])
        self.cur = self.conn.cursor()

    def execute_sql(self, sql, commit=False):
        try:
            self.cur.execute(sql)
            if commit:
                self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            self.close_connection()

    def get_first_result_from_database(self, sql):
        try:
            self.cur.execute(sql)
            # return dict
            return self.__convert_one_result_to_list(self.cur.fetchone())[0]
        finally:
            self.close_connection()

    def get_random_result_from_database(self, sql):
        try:
            self.cur.execute(sql)
            result = self.cur.fetchall()
            # return dict
            return self.__convert_one_result_to_list(result[random.randint(0, len(result)-1)])[0]
        finally:
            self.close_connection()

    def get_all_results_from_database(self, sql):
        try:
            self.cur.execute(sql)
            # return list
            return self.__convert_one_result_to_list(self.cur.fetchall())
        finally:
            self.close_connection()

    def insert_into_database(self, sql):
        self.execute_sql(sql, commit=True)

    def update_in_database(self, sql):
        self.execute_sql(sql, commit=True)

    def delete_from_database(self, sql):
        self.execute_sql(sql, commit=True)

    def close_connection(self):
        self.cur.close()
        self.conn.close()

    def __convert_all_results_to_list(self, results):
        fields = map(lambda x: x[0], self.cur.description)
        return [dict(zip(fields, row)) for row in results]

    def __convert_one_result_to_list(self, result):
        fields = map(lambda x: x[0], self.cur.description)
        return [dict(zip(fields, result))]


class MysqlConnection:

    def __init__(self):
        self.env_config = LoadConfig.load_config()["env"]

    def connect(self, name):
        return MysqlHelper(self.env_config[name])
