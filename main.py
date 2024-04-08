from src.data_ingest import DataIngestion

if __name__ == "__main__":
    data_ingest = DataIngestion("data/advertising.csv")
    
    X,y,df = data_ingest.getx_y()
    df.to_csv("./data/simple_df.csv",index = False)
    print(df)