from .models import Staff_auth
import pandas as pd

def importdata():
    data = pd.read_csv ('preelec9_camp/63Data.csv')   
    Staff_auth.objects.all().delete()
    for j in range(0,len(data)):
        db = Staff_auth( 
            email = "{}@kmitl.ac.th".format(data["Id"][j]))
        db.save()
if __name__ == "__main__":
    importdata()