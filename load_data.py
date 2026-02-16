def save_processed(table, name):
    table.to_csv(f"data/processed/{name}.csv", index=False)
    table.to_json(f"data/processed/{name}.json", orient="records")
