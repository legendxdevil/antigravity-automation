import os
import csv
import sys

def get_next_day_and_topic(csv_path, state_path):
    if not os.path.exists(state_path):
        os.makedirs(os.path.dirname(state_path), exist_ok=True)
        with open(state_path, 'w') as f:
            f.write('0')
        last_day = 0
    else:
        with open(state_path, 'r') as f:
            last_day = int(f.read().strip())
    
    next_day = last_day + 1
    
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at {csv_path}", file=sys.stderr)
        sys.exit(1)
        
    topic = None
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row['Day']) == next_day:
                topic = row['Topic']
                break
                
    if not topic:
        print(f"Error: Topic for Day {next_day} not found in CSV", file=sys.stderr)
        sys.exit(1)
        
    return next_day, topic

if __name__ == '__main__':
    csv_path = 'dsa_365_roadmap.csv'
    state_path = 'state/last_posted_day.txt'
    
    day, topic = get_next_day_and_topic(csv_path, state_path)
    print(f"DAY:{day}")
    print(f"TOPIC:{topic}")
