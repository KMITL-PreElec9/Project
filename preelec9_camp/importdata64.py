#%%
from .models import Campdata
import pandas as pd
import datetime

def cvtime(oldtime):
    time = datetime.datetime.strptime(oldtime, "%d/%m/%Y").strftime("%Y-%m-%d")
    return(time)

data = pd.read_csv ('preelec9_camp/64Data.csv')   
fields = ["name","self_telephone_num","line_id","birth_date","email","nickname"]
Campdata.objects.all().delete()
for j in range(0,len(data)):
    db = Campdata( \
        name = data[fields[0]][j], self_telephone_num =data[fields[1]][j], \
        line_id = data[fields[2]][j], birth_date = cvtime(data[fields[3]][j]),\
        email = data[fields[4]][j] , nickname = data[fields[5]][j])
    db.save()
# %%
