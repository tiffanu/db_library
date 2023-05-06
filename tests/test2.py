import os
import pytest
from . import execute_sql_to_df
from . import read_sql


@pytest.fixture()
def select_script():
    path = os.getenv("SCRIPT_PATH")
    return read_sql(path)


@pytest.fixture()
def select_df(select_script, sqlalchemy_conn):
    return execute_sql_to_df(
        conn=sqlalchemy_conn,
        sql=select_script
    )


def test2(select_df):
    assert select_df.query("name == 'Тимур'")['surname'].iloc[0] == 'Муцураев'
    assert select_df.query("name == 'Тимур'")['begin_date'].iloc[0] == '1994-12-11'
    assert select_df.query("name == 'Тимур'")['end_date'].iloc[0] == '1996-08-31'
    
