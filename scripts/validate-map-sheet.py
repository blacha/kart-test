# /// script
# dependencies = [
#   "pyarrow",
# ]
# ///
import pyarrow.parquet as pq

table = pq.read_table("./nz_topo_map_sheet.parquet")

sheet_code_column = table.column('sheet_code')
sheet_code_values = sheet_code_column.to_pylist()

for code in sheet_code_values:
    print(f"sheet {code}")
