import json
import csv

def process_and_merge():
    # 1. Load the Pro Tips Database
    pro_tips = {}
    try:
        with open('pro_tips.csv', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                pro_tips[row['station_name']] = {
                    "gates": row['gates'].split(','),
                    "coachTip": row['coach_tip'],
                    "platform": row['platform_info']
                }
    except FileNotFoundError:
        print("pro_tips.csv not found, proceeding with basic data.")

    # 2. Build final config
    config = {
        "version": 3,
        "stations": pro_tips
    }
    
    # 3. Export to your App
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)
    print("Pipeline Success: config.json merged with pro_tips.csv")

if __name__ == "__main__":
    process_and_merge()
