# recommendation_model.py

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Load the data and preprocess it
#df = pd.read_csv('//Users/alibayram/Desktop/SepetAnalizi/NovaNestData.csv', names=['products'], sep=' ')
df = pd.read_csv('/Users/alibayram/Desktop/BitirmeProjesiFinal/SepetAnalizi/NovaNestData.csv', names=['products'], sep=' ')
data = list(df['products'].apply(lambda x: x.split(',')))
te = TransactionEncoder()
te_data = te.fit(data).transform(data)
df_encoded = pd.DataFrame(te_data, columns=te.columns_)

# Apply the Apriori algorithm
frequent_itemsets = apriori(df_encoded, min_support=0.02, use_colnames=True)
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.6)

# Function to get recommendations
def get_recommendations(product_id):
    recommendations = rules[rules['antecedents'].apply(lambda x: product_id in x)]['consequents']
    return recommendations
