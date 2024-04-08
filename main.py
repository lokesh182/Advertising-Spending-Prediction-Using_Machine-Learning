from src.data_ingest import DataIngestion
from src.data_preprocess import DataPreprocessing
from src.build_model import SimpleLinearRegression


if __name__ == "__main__":
    data_ingest = DataIngestion("data/advertising.csv")
    
    X,y,df = data_ingest.getx_y()
    df.to_csv("./data/simple_df.csv",index = False)
    print(df)

data_process = DataPreprocessing(df)
outliers = data_process.identify_outliers_zscore(df["TV"])
print(outliers)

model = SimpleLinearRegression(X,y)
lr_model = model.summary()
print(lr_model)