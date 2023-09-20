def before_merge(dataframe):
    dataframe.drop(dataframe[dataframe['Location'].isnull()==True].index,inplace = True)#delete rows with null locations
    dataframe['Location'] = dataframe['Location'].apply(lambda x: x.upper()) #convert location names to uppercase
    dataframe.drop(dataframe[dataframe['Location'].str.contains('PHILIPPINES|REGION')].index,inplace=True) #remove PH and Regional values
    return dataframe.reset_index(drop=True)