def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    days = {1: "Sunday",2: "Monday", 3: "Tuesday",4: "Wednesday", 5:"Thursday",6:"Friday",7:"Saturday"}
    if list(range(1,8)).count(day_of_week) == 1:
         return days.get(day_of_week) 