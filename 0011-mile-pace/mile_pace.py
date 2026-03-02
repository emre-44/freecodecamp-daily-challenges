"""
Given a number of miles ran, and a time in "MM:SS" (minutes:seconds) it took to run those miles, 
return a string for the average time it took to run each mile in the format "MM:SS".

Add leading zeros when needed.
"""
def mile_pace(miles, duration):
    """
    Generate average time from user inputs
    Args:
        miles(int): The total number of miles run
        duration(str): The total time taken in "MM:SS" format 
    Returns:
        str: The average time per mile in "MM:SS" format with leading zeros 

    """
    m, s = map(int, duration.split(":"))
    
    total_seconds = m * 60 + s
    avg_seconds = total_seconds / miles
    
    avg_minutes = int(avg_seconds // 60)
    avg_seconds = int(avg_seconds % 60)

    return f"{avg_minutes:02d}:{avg_seconds:02d}"

#Test Stage
print(mile_pace(3, "24:00"))