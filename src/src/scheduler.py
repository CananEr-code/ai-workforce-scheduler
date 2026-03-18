def generate_schedule(df):
    schedules = []
    
    for _, row in df.iterrows():
        start = row["start_time"]
        
        # simple logic
        break_time = "00:30"
        end_time = "17:00"
        
        schedules.append({
            "name": row["name"],
            "start": start,
            "break": break_time,
            "end": end_time
        })
    
    return schedules
