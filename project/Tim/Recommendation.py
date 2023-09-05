import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\Admin\Desktop\project\shoppingcart.csv")
search_history=['']
shoppingcart_list=['']
def generate_recommendations(search_history, shoppingcart_list, min_support=0.01, min_confidence=0.5):
    # 读取数据
    from mlxtend.frequent_patterns import apriori, association_rules
    Product = df.copy()
    
    #過濾帳單出現次數小於2次的record
    item_counts = df['Itemname'].value_counts(ascending=False)
    filtered_items = item_counts.loc[item_counts > 1].reset_index()['index']
    Product = Product[Product['Itemname'].isin(filtered_items)]
    
    bill_counts = Product['BillNo'].value_counts(ascending=False)
    filtered_bills = bill_counts.loc[bill_counts > 1].reset_index()['index']
    Product = Product[Product['BillNo'].isin(filtered_bills)]
    
    # Create pivot_table for encoding
    pivot_table = pd.pivot_table(Product[['BillNo','Itemname']], index='BillNo', columns='Itemname', aggfunc=lambda x: True, fill_value=False)
    
    # Creaete Frequent table
    frequent_itemsets = apriori(pivot_table, min_support=min_support, use_colnames=True)
    
    # 生成關聯規則
    rules = association_rules(frequent_itemsets, "confidence", min_threshold=min_confidence)
    
    # Based on support sorting
    rules_sorted_by_support = rules.sort_values(by='support', ascending=False)
    
    rules = rules.sort_values(['confidence', 'lift'], ascending=[False, False])
    
    Top10=list(df.groupby('Itemname')['Quantity'].sum().sort_values(ascending=False).head(10).index)
    
    # 提取关联规则
    associate_rules = rules[['antecedents','consequents']]
    
    # get user search recommendations
    def get_recommendations(search_history, association_rules):
        recommendations = set()

        for item in search_history:
            matching_rules =   associate_rules[ associate_rules['antecedents'].apply(lambda x: item in x)]

            for consequents in matching_rules['consequents']:
                recommendations.update(consequents)

        for item in search_history:
            recommendations.discard(item)
            
        return recommendations
    
    # get recommendations
    user_recommendations = get_recommendations(search_history, association_rules)
    
    # 
    while len(user_recommendations) <5:
        for i in Top10:
            if len(user_recommendations) < 5:
                user_recommendations.add(i)
            if i in shoppingcart_list:
                user_recommendations.discard(i)
    
    
    user_recommendations = list(user_recommendations)[:6]
    
    return user_recommendations

# 示例使用

recommended_items = generate_recommendations(search_history, shoppingcart_list)

print("Recommended items for the user:")
print(recommended_items)