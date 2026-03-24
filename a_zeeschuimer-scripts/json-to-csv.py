import json, sys, csv, os


def flatten(obj, parent_key="", sep="."):
    """Recursively flatten nested dicts/lists into dot-notation keys."""
    items = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            items.update(flatten(v, new_key, sep))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            new_key = f"{parent_key}{sep}{i}" if parent_key else str(i)
            items.update(flatten(v, new_key, sep))
    else:
        items[parent_key] = obj
    return items


input_path = sys.argv[1]
output_path = os.path.splitext(input_path)[0] + ".csv"

with open(input_path, encoding="utf-8") as f:
    rows = json.load(f)

if not rows:
    sys.exit(0)

flat_rows = [flatten(row) for row in rows]

# collect all keys across all rows (not every row may have the same fields)
fieldnames = list(dict.fromkeys(k for row in flat_rows for k in row))

with open(output_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(flat_rows)

print(f"Saved {len(flat_rows)} rows ({len(fieldnames)} columns) to {output_path}")
