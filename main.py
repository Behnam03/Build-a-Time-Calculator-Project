def add_time(start, duration, starting_day=None):
    
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    
    start_time, period = start.split()
    start_hours, start_minutes = map(int, start_time.split(':'))
    
    
    if period == "PM" and start_hours != 12:
        start_hours += 12
    elif period == "AM" and start_hours == 12:
        start_hours = 0
        
    
    duration_hours, duration_minutes = map(int, duration.split(':'))
    
    
    total_minutes = start_minutes + duration_minutes
    extra_hours = total_minutes // 60
    final_minutes = total_minutes % 60
    
    
    total_hours = start_hours + duration_hours + extra_hours
    days_later = total_hours // 24
    final_hours = total_hours % 24
    
    
    if final_hours == 0:
        final_hours = 12
        period = "AM"
    elif final_hours == 12:
        period = "PM"
    elif final_hours > 12:
        final_hours -= 12
        period = "PM"
    else:
        period = "AM"
    
    
    new_time = f"{final_hours}:{final_minutes:02d} {period}"
    
    
    if starting_day:
        current_day_index = days_of_week.index(starting_day.title())
        new_day_index = (current_day_index + days_later) % 7
        new_time += f", {days_of_week[new_day_index]}"
    
    
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
    
    return new_time