""" Parquet utilities.

This will be used to write parquet files when needed. It looks
like a new parquet file must be written each time we use updated
data.

References:
  https://arrow.apache.org/docs/index.html
"""
from datetime import datetime
import os
import logging
from urllib.parse import urljoin

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


logger = logging.getLogger(__name__)


def write_parquet_table(table_name: str, query: str, db_dir: str,
                        dbs: list, batch_size: int):
    """ Write parquet table from sqlite database. 

    :param table_name: name of sqlite database table
    :param query: SQL query string
    :param db_dir: directory containing sqlite databases
    :param dbs: list of all sqlite database file names
    :param batch_size: int, number of rows in table written out, int(2e6)
    :return: parquet file written to db_dir location
    :rtype: None
    """
    logger.info("Writing parquet files for {}".format(table_name))
    df = None
    first = True
    datenow = datetime.now().strftime('%Y-%m-%d')
    table_format = table_name + "_{}_{}.parquet"
    
    subnum = 0
    for db in dbs:
        
        conn = 'sqlite:///' + db_dir + db
        
        if first:
            df = pd.read_sql(query, conn)
            first = False
        else:
            da = pd.read_sql(query, conn)
            df = df.append(da)
            
        if df.shape[0] > batch_size:
            
            table_name = table_format.format(datenow, subnum)
            table_path = urljoin(db_dir, table_name)
            df_out = df.iloc[0:batch_size]
            table = pa.Table.from_pandas(df_out)
            pq.write_table(table, table_path)
            logger.info("Wrote parquet file: {}".format(table_path))
            subnum += 1
            
            df = df.iloc[batch_size:]
            
    if df.shape[0] > 0:
        
        table_name = table_format.format(datenow, subnum)
        table_path = urljoin(db_dir, table_name)
        table = pa.Table.from_pandas(df)
        pq.write_table(table, table_path)
        logger.info("Wrote parquet file: {}".format(table_path))

def sqlite_to_parquet(tables: list, db_dir, batch_size):
    """ SQLite datase to parquet files. 

    :param tables: list of table names in each SQLite database
    :param db_dir: directory containing sqlite databases
    :param batch_size: int, number of rows in table written out, int(2e6)
    :return: parquet files for each table written out to db_dir
    :rtype: None
    """
    logger.info("STARTED converting all sqlite databases to parquet")
    dbs = [i for i in os.listdir(db_dir) if i[-3:] == ".db"]
    query_format = "SELECT * FROM {};"
    for table_name in tables:
       
        query = query_format.format(table_name)
        logger.info("Created query: {}".format(query))
        write_parquet_table(table_name, query, db_dir, dbs, batch_size)
        
    logger.info("FINISHED converting all sqlite databases to parquet")
