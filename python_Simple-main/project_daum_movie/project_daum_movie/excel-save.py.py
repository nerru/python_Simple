# DB에 저장되어 있는 수집 데이터를 Excel로 저장!
#python(Dict, List 컬렉션)
#
#Pandas의  DataFrame(표)
#
# File(CSV, Excel)

import pandas as pd
from db.movie_dao import get_reviews

reviews = get_reviews()
for item in reviews:
    print(item)

df_save = pd.DataFrame(reviews)
print(df_save)

now = datetime.now().strftime("%Y%m%d")
df_save.to_excel(f"./reviews_{now}.xlsx", index=False)