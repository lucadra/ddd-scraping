import json
from apify_client import ApifyClient

API_TOKEN = ""    # Insert your API token here (you can find it in Apify -> Settings -> API & Integrations)
ACTOR = ""        # Insert user/actor you want to use here (e.g. "clockworks/tiktok-scraper")
OUTPUT_FILE = ""  # Insert the name of the output file here (e.g. "tiktok_data.json")
PARAMETERS = {}   # Insert the parameters here (you can find them in the actor's documentation, 
                  # e.g. for "clockworks/tiktok-scraper": {"hashtags": ["lugano"], "resultsPerPage": 5})

# Authenticate with API
client = ApifyClient(API_TOKEN)

# Run the actor
run = client.actor(ACTOR).call(run_input=PARAMETERS)

# Extract the data
dataset_id = run["defaultDatasetId"]
dataset_client = client.dataset(dataset_id)
items = list(dataset_client.iterate_items())

# Save the data
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

