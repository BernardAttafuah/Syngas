def NumberOfColumns(df): 
    for number, names in enumerate(df.columns):
        count = print(number, names)
    print(f'The shape of the data is: ',df.shape)
