import pandas as pd
import os
import logging
import boring_stuff
import numpy as np


DATA_PATH= os.path.join(boring_stuff.DATA_DIR, "cdr")
logger = logging.getLogger("inspect_cdr")
logger.setLevel(logging.DEBUG)


def sample_cdr(sample_size):
    colnames=['msisdn','sc','cc','rg','dur','usu','dsbr']
    filename = os.path.join(DATA_PATH, "2L3CCN_CCR_20201105.csv")
    df = pd.read_csv(filename, header=None, sep=',', names=colnames)
    df2 = df.sample(n=sample_size, replace=False)
    df2.to_csv(os.path.join(DATA_PATH, "sample.csv"), index=False)

def preprocess(df):
    size = df.shape[0]
    logger.info("Total number of record=={:d}".format(size))
    zero_size = df[df["usu"] == 0].shape[0]
    logger.info("No of record w/ usu=0 is {}, {:.2%}".format(zero_size, zero_size/size))

    logger.info("Change Byte to MB")
    df["usu"] = df["usu"].map(lambda x: x/1024/1024)
    return df

def get_4g(df):
    return df[ df["sc"] <5000 ]

def get_5g(df):
    return df[ (df["sc"] >= 5000) & (df["sc"] < 6000)]

def count_unique(arr):
    return np.unique(arr).size

def group_by_cc(df):
    grouped = df.groupby("cc", as_index=False)
    g1= grouped["cc"].size()
    g2= grouped["usu"].sum()
    g3= grouped["msisdn"].agg(count_unique)

    gg= pd.merge(g1, g2, on="cc")
    gg= pd.merge(gg, g3, on="cc")

    gg.rename(columns={"size": "cc no", "usu": "sum usu", "msisdn":"msisdn no"}, inplace=True)
    gg["avg usu"] = gg["sum usu"]/gg["msisdn no"]
    gg.sort_values(by=["avg usu"], inplace=True)

    return gg


def get_data_characteristic(df):
    # total ccr number
    total_ccr=  df.shape[0]
    # total unique sub number
    total_sub = df[df.duplicated(subset=["msisdn"])==False].shape[0]
    # usu sum
    sum_usu=df["usu"].sum()
    # averger ccr number
    avg_ccr = total_ccr/total_sub
    # averger usu
    avg_usu = sum_usu / total_sub
    return (total_ccr, total_sub, sum_usu, avg_ccr, avg_usu)

def inspect(sample_size=10000, re_sample=False):
    if re_sample:
        logger.info("Resampling...")
        sample_cdr(sample_size)

    filename = os.path.join(DATA_PATH, "sample.csv")
    df = pd.read_csv(filename, sep=',')
    df = preprocess(df)

    df_4g = get_4g(df)
    df_5g = get_5g(df)

    total_ccr_4g, total_sub_4g, sum_usu_4g, avg_ccr_4g, avg_usu_4g = get_data_characteristic(df_4g)
    total_ccr_5g, total_sub_5g, sum_usu_5g, avg_ccr_5g, avg_usu_5g = get_data_characteristic(df_5g)

    logger.info("Avg 4G usu: {:d} / {:d} = {:.2f} MB".format(total_ccr_4g, total_sub_4g, avg_usu_4g))
    logger.info("Avg 5G usu: {:d} / {:d} = {:.2f} MB".format(total_ccr_5g, total_sub_5g, avg_usu_5g))

    logger.info("Avg 5G vs 4G usu ratio: {:.2f}/{:.2f} = {:.2%}".format( avg_usu_5g, avg_usu_4g, avg_usu_5g/avg_usu_4g ))
    logger.info("Avg 5G vs 4G ccr no ratio: {:.2f}/{:.2f} = {:.2%}".format(avg_ccr_5g,avg_ccr_4g, avg_ccr_5g/avg_ccr_4g))
    result=pd.DataFrame()

    gg = group_by_cc(df)
    logger.info(" count by cc:")
    logger.info(gg.to_string(formatters={'sum usu': '{:,.2f} MB'.format, 'avg usu': '{:,.2f} MB'.format}))

if __name__ == "__main__":

    sample_sizes=[200000, 500000, 1000000]
    for i, sample_size in enumerate(sample_sizes):
        logger.info("===============================".format(i))
        logger.info("==         SAMPLE {:d}         ==".format(i+1))
        logger.info("===============================".format(i))
        inspect(sample_size, False)