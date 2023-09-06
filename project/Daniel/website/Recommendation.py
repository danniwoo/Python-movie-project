import numpy as np
import pandas as pd
from . import df
from . import Top10, rules

search_history=['']
shoppingcart_list=['']
def generate_recommendations(search_history, shoppingcart_list, min_support=0.01, min_confidence=0.5):
    # 读取数据
    # 提取关联规则
    
    # get user search recommendations
    def get_recommendations(search_history, associate_rules):
        recommendations = set()

        for item in search_history:
            matching_rules =   associate_rules[ associate_rules['antecedents'].apply(lambda x: item in x)]

            for consequents in matching_rules['consequents']:
                recommendations.update(consequents)

        for item in search_history:
            recommendations.discard(item)
            
        return recommendations
    
    # get recommendations
    user_recommendations = get_recommendations(search_history, associate_rules)
    
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
associate_rules = rules[['antecedents','consequents']]
recommended_items = generate_recommendations(search_history, shoppingcart_list)

print("Recommended items for the user:")
print(recommended_items)
