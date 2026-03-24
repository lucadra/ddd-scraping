import json, sys, os

input_path = sys.argv[1]
output_path = os.path.splitext(input_path)[0] + ".json"

data = [json.loads(line) for line in open(input_path) if line.strip()]

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Saved {len(data)} items to {output_path}")
