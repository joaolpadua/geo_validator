from src.reader import read_files

data = read_files("data/")

for file_name, gdf in data:
    print(f"\nArquivo: {file_name}")
    print(gdf.head())
    print(gdf.is_valid.head())