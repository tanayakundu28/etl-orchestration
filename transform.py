import pandas as pd

def transform_data(df):
    
    #transform columns
    df['price_total'] = df['price'].apply(lambda x: x['total'])

    #drop columns
    df = df.drop(['position', 'images', 'hostThumbnail', 'rareFind', 'userId', 'amenityIds', 'previewAmenities', 'price', 'deeplink', 'city', 'cancelPolicy'], axis = 1)
    
    return df

def convert_to_csv(df) :

    # transform the loaded data
    data = transform_data(df)

    # save as csv file
    data.to_csv('data.csv')