import json
from apify_client import ApifyClient

API_TOKEN = ""  # Apify -> Settings -> API & Integrations
ACTOR = "clockworks/tiktok-scraper"
HASHTAGS = ["lugano", "zurich", "geneva"]
RESULTS_PER_TAG = 5

# Authenticate with API
client = ApifyClient(API_TOKEN)

# Initialize an empty list to store all the data
all_items = []

for tag in HASHTAGS:
    # Run the actor
    run = client.actor(ACTOR).call(run_input={
        "hashtags": [tag],
        "resultsPerPage": RESULTS_PER_TAG,
    })
    # Extract the data and append to our list
    all_items.extend(client.dataset(run["defaultDatasetId"]).iterate_items())

# Save the data
with open("tiktok_data.json", "w", encoding="utf-8") as f:
    json.dump(all_items, f, ensure_ascii=False, indent=2)
