from src.reader import read_files
from src.validator import validate_invalid_geometry
import pandas as pd

data = read_files("data/")

all_errors = []



for file_name, gdf in data:
    errors = validate_invalid_geometry(file_name, gdf)
    all_errors.extend(errors)

df = pd.DataFrame(all_errors)
print(df)

print(all_errors)