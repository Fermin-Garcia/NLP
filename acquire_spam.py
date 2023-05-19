from env import user, password, host
import acquire_spam
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


def get_db_url(database, host=host, user=user, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{database}'


def get_spam_data():
    url = get_db_url("spam_db")
    sql = "SELECT * FROM spam"

    df = pd.read_sql(sql, url)

    return df