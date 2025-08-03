# check_db.py
import sqlite3
import json

print("--- Checking contents of queries.db ---")

try:
    conn = sqlite3.connect('queries.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, timestamp, court_complex, case_type, case_number, case_year, raw_response FROM queries")
    rows = cursor.fetchall()

    if not rows:
        print("The 'queries' table is currently empty.")
    else:
        print(f"Found {len(rows)} entries:\n")
        for row in rows:
            # Unpack the row data
            entry_id, timestamp, complex_code, case_type, case_num, case_year, raw_response = row
            
            print(f"--- Entry ID: {entry_id} | Timestamp: {timestamp} ---")
            print(f"Query: Complex='{complex_code}', Type='{case_type}', Num='{case_num}', Year='{case_year}'")
            
            # THE FIX: Try to parse and pretty-print the raw_response
            try:
                # Parse the JSON string
                response_json = json.loads(raw_response)
                # Pretty-print the JSON with an indent of 4 spaces
                pretty_response = json.dumps(response_json, indent=4)
                print("Response:\n" + pretty_response)
            except json.JSONDecodeError:
                # If it's not JSON (e.g., an HTML error page), print it directly
                print("Response (not valid JSON):\n" + raw_response)
            
            print("-" * 40 + "\n")
    
    conn.close()

except sqlite3.OperationalError:
    print("Error: The database or table does not exist. Please run 'python init_db.py' first.")