import pandas as pd
import numpy as np

from math import nan

def give_path_aim(path_origin: str) -> str:
    """Extract the path where the file should be saved."""
    return '../data/processed/' + path_origin[12:-4] + '_processed.csv'

DATES = ['2019-01-31', '2019-02-28', '2019-03-31', '2019-04-30', '2019-05-31', '2019-06-30',
         '2019-07-31', '2019-08-31', '2019-09-30', '2019-10-31', '2019-11-30', '2019-12-31',
         '2020-01-31', '2020-02-29', '2020-03-31', '2020-04-30', '2020-05-31', '2020-06-30',
         '2020-07-31', '2020-08-31', '2020-09-30', '2020-10-31', '2020-11-30', '2020-12-31',
         '2021-01-31', '2021-02-28', '2021-03-31', '2021-04-30', '2021-05-31', '2021-06-30',
         '2021-07-31', '2021-08-31', '2021-09-30', '2021-10-31', '2021-11-30', '2021-12-31',
         '2022-01-31', '2022-02-28', '2022-03-31', '2022-04-30', '2022-05-31', '2022-06-30',
         '2022-07-31', '2022-08-31', '2022-09-30', '2022-10-31', '2022-11-30', '2022-12-31',
         '2023-01-31', '2023-02-28', '2023-03-31', '2023-04-30', '2023-05-31', '2023-06-30',
         '2023-07-31', '2023-08-31', '2023-09-30', '2023-10-31', '2023-11-30', '2023-12-31',
         '2024-01-31', '2024-02-29', '2024-03-31', '2024-04-30', '2024-05-31', '2024-06-30',
         '2024-07-31', '2024-08-31', '2024-09-30', '2024-10-31', '2024-11-30', '2024-12-31',
         '2025-01-31', '2025-02-28', '2025-03-31', '2025-04-30', '2025-05-31', '2025-06-30',
         '2025-07-31', '2025-08-31', '2025-09-30', '2025-10-31', '2025-11-30', '2025-12-31']


def prepare_monatsbericht(path_origin: str, path_aim: str):
    """Preprocess files with name 'Monatsbericht' such that the index is given by the month"""
    df = pd.read_csv(path_origin, skiprows =7,
            skipfooter = 4, sep = ';'
            )
    #Adapt column names
    df.columns = ['Steller', 'Produkt', 'Betriebe', 'Betriebe_ep', 'Beschäftigte',
       'Beschäftigte_ep', 'Geleistete Arbeitsstunden', 'Geleistete Arbeitsstunden_ep',
       'Bruttolohn- und -gehaltssumme', 'Bruttolohn- und -gehaltssumme_ep', 'Umsatz', 'Umsatz_ep',
       'Inlandsumsatz', 'Inlandsumsatz_ep', 'Auslandsumsatz', 'Auslandsumsatz_ep',
       'Auslandsumsatz mit der Eurozone', 'Auslandsumsatz mit der Eurozone_ep',
       'Auslandsumsatz mit dem sonstigen Ausland', 'Auslandsumsatz mit dem sonstigen Ausland_ep']
    different_steller = df['Steller'].unique().tolist()
    num_diff_steller = len(different_steller)-12-7-1
    #Add date
    df['month']=0
    for year in range(7):
        k = 2 + (1+(num_diff_steller +1)*12)*year
        for month in range(1,13): 
            for i in range(1,num_diff_steller+1):
                df.iloc[k+i+(month-1)*(num_diff_steller +1),-1] = month
    for year in range(7):
        k = 2 + (1+(num_diff_steller +1)*12)*year
        for month in range(0,12): 
            df =  df.drop(k + month * (num_diff_steller+1),axis=0)
    df['year']=0
    for year in range(7):
        for i in range(1 + 12 * num_diff_steller):
            df.iloc[1 + year* (1 + 12 * num_diff_steller) + i, -1] = year + 2019
    for year in range(7):
        df =df.drop(1 + year*(1 + 12 * (num_diff_steller+1)), axis=0)
    df =df.drop(0,axis = 0)
    df['day']=1
    df['date']=pd.to_datetime(df_1082[['year', 'month', 'day']])

    df = df.drop('month', axis=1)
    df = df.drop('year', axis=1)
    df = df.drop('day', axis=1)
    #Include multiplicities
    for column in ['Betriebe', 'Beschäftigte', 'Geleistete Arbeitsstunden', 'Bruttolohn- und -gehaltssumme', 
            'Inlandsumsatz', 'Auslandsumsatz', 'Auslandsumsatz mit der Eurozone', 'Umsatz',
            'Auslandsumsatz mit dem sonstigen Ausland']:
        df[column]=df[column].replace('...', nan)
        df[column]=df[column].astype('float64')
    df['Geleistete Arbeitsstunden'] = df['Geleistete Arbeitsstunden'] * 1000
    df['Bruttolohn- und -gehaltssumme'] = df['Bruttolohn- und -gehaltssumme'] * 1000
    df['Umsatz'] = df['Umsatz'] * 1000
    df['Inlandsumsatz'] = df['Inlandsumsatz'] * 1000
    df['Auslandsumsatz'] = df['Auslandsumsatz'] * 1000
    df['Auslandsumsatz mit der Eurozone'] = df['Auslandsumsatz mit der Eurozone'] * 1000
    df['Auslandsumsatz mit dem sonstigen Ausland'] = df['Auslandsumsatz mit dem sonstigen Ausland'] * 1000
    #Divide df in a df for each different Steller
    different_steller = df['Steller'].unique().tolist()
    df_separated = []
    for steller in different_steller:
        mask = (df['Steller'] == steller)
        df_help = df.loc[mask,:]
        df_help = df_help.drop('Steller', axis=1)
        df_help = df_help.drop('Produkt', axis=1)
        new_columns = []
        for col in df_help.columns.values[:-1]:
            new_columns.append(col + '_' + steller)
        new_columns.append('date')
        df_help.columns = new_columns
        df_help['date'] = DATES
        df_help = df_help.set_index('date')
        df_separated.append(df_help)
    df_prepared = pd.concat(df_separated, axis = 1)
    df_prepared.to_csv(path_aim)


def prepare_GP(path_origin, path_aim, praefix = ''):
    """Preprocess files with name 'GP' such that the index is given by the month"""
    df= pd.read_csv(path_origin, 
                skiprows =6,
                skipfooter = 3, sep = ';', decimal = ','
                )
    for i in range(3, 171, 2):
        zahl = str(i)
        df = df.drop('Unnamed: '+zahl, axis=1)
    df = df.transpose()
    columns = df.iloc[1,:]
    columns.values[0] = 'Month'
    for i in range(1,len(columns)):
        columns.values[i] = praefix + '_' + columns.values[i]
    df.columns = columns
    df = df.drop('Unnamed: 0', axis = 0)
    df = df.drop('Unnamed: 1', axis = 0)
    list_year = []
    for year in range(7):
        list_year = list_year + np.full(12,year+2019).tolist()
    df['Year'] = list_year
    df['Day'] = 1
    df['Month'] = df['Month'].replace({'Januar':1, 'Februar':2, 'März': 3, 'April':4, 'Mai':5, 
                                   'Juni': 6, 'Juli': 7, 'August': 8, 'September': 9, 'Oktober': 10, 'November': 11, 'Dezember': 12})

    df['date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
    df = df.drop('Month', axis = 1)
    df = df.drop('Year', axis = 1)
    df = df.drop('Day', axis = 1)
    df['date'] = DATES
    df = df.set_index('date')
    for col in df.columns:
        df[col]=df[col].astype('float64')
    df.to_csv(path_aim)


def prepare_globalprice(path_origin, path_aim):
    """Preprocess files with globalprices such that the index is given by the month"""
    df= pd.read_csv(path_origin, 
                skiprows =0,
                skipfooter = 0, sep = ','
                )
    df.columns = ['date', df.columns[1]]
    df = df.iloc[:84,:]
    df['date'] = DATES
    df = df.set_index('date')
    df = df.iloc[-84:, :]
    df.to_csv(path_aim)
