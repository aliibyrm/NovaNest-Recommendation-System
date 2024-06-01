# from fastapi import FastAPI
# from fastapi.responses import JSONResponse
# import pandas as pd
# from mlxtend.preprocessing import TransactionEncoder
# from mlxtend.frequent_patterns import apriori, association_rules

# app = FastAPI()

# df = pd.read_csv('/Users/alibayram/Desktop/SepetAnalizi/NovaNestData.csv', names=['products'], sep='*')
# data = list(df["products"].apply(lambda x: x.split(',')))
# te = TransactionEncoder()
# te_data = te.fit(data).transform(data)
# df_encoded = pd.DataFrame(te_data, columns=te.columns_)

# frequent_itemsets = apriori(df_encoded, min_support=0.02, use_colnames=True)
# rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

# @app.get("/get_recommendations/{product_id}")
# def get_recommendations(product_id: str):
#     recommendations = rules[rules['antecedents'].apply(lambda x: product_id in x)]['consequents']
#     return JSONResponse(content={"recommendations": recommendations.to_list()})

# main.py

from fastapi import FastAPI
from typing import List
from recommendation_model import get_recommendations
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware ekleyin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5005"],  # İzin verilen etki alanları
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_recommendations/{product_id}")
def read_root(product_id: str):
    recommendations = get_recommendations(product_id)
    return {"recommendations": recommendations.to_list()}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=3000)
