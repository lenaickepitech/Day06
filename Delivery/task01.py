from xml import dom
import task00


def get_departments(df) -> list[str]:
    departments = df["Code departement"].dropna().astype(str).unique()
    return sorted(departments)

dom task00 import make_dataframe
from task01 import get_departments
df = make_dataframe("./real_estate.csv")
d = get_departments(df)
print(d)