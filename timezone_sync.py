def calculate_global_times(lagos_hour, lagos_minute):
    """
    Calculates international team meeting times based on Nigeria local time.
    Lagos (WAT) is UTC+1.
    Kuala Lumpur (MYT) is UTC+8 (+7 hours from Lagos).
    Dili, Timor-Leste (TLT) is UTC+9 (+8 hours from Lagos).
    """
    offsets = {
        "Kuala Lumpur (Southeast Asia)": 7,
        "Dili (Timor-Leste)": 8
    }
    
    print(f"\n--- Maxfront Global Sync Times for {lagos_hour:02d}:{lagos_minute:02d} WAT (Nigeria) ---")
    
    for region, offset in offsets.items():
        raw_hour = lagos_hour + offset
        converted_hour = raw_hour % 24  # Modulo constraints constraint handling
        
        day_status = ""
        if raw_hour >= 24:
            day_status = " (Next Day)"
            
        print(f"🌍 {region}: {converted_hour:02d}:{lagos_minute:02d}{day_status}")

def main():
    print("=========================================")
    print("  MAXFRONT REMOTE TIME-ZONE SYNCHRONIZER ")
    print("=========================================")
    
    while True:
        try:
            user_input = input("\nEnter proposed meeting time in Lagos (Format HH:MM e.g., 14:30) or 'q' to quit: ")
            
            if user_input.lower() == 'q':
                print("Exiting synchronizer. Have a great productive day!")
                break
                
            hour_str, minute_str = user_input.split(":")
            hour = int(hour_str)
            minute = int(minute_str)
            
            if not (0 <= hour <= 23 and 0 <= minute <= 59):
                print("❌ Invalid time! Hours must be 0-23 and minutes 0-59.")
                continue
                
            calculate_global_times(hour, minute)
            
        except ValueError:
            print("❌ Invalid format! Please use the HH:MM format (e.g., 09:15 or 16:00).")

if __name__ == "__main__":
    main()