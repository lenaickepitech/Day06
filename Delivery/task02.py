def get_towns(df, department: str | None = None) -> list[dict]:
    data = df

    if department is not None:
        if department not in df["Code departement"].astype(str).unique():
            return []
        data = df[df["Code departement"].astype(str) == department]

    towns = (
        data[["Nom commune", "Code commune"]]
        .dropna()
        .drop_duplicates()
        .astype(str)
        .sort_values("Code commune")
    )

    return [
        {"name": row["Nom commune"], "insee_code": row["Code commune"]}
        for _, row in towns.iterrows()
    ]

df = make_dataframe("./real_estate.csv")
print(get_towns(df))