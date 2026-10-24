class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Days in each month for a non-leap year
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def convert_to_day_number(date_str: str) -> int:
            month, day = map(int, date_str.split("-"))
            # Sum days of all previous completed months plus the current day
            total_days = sum(days_in_months[:month - 1]) + day
            return total_days
        
        # Convert all four date strings to day numbers (1 to 365)
        a_arrive = convert_to_day_number(arriveAlice)
        a_leave = convert_to_day_number(leaveAlice)
        b_arrive = convert_to_day_number(arriveBob)
        b_leave = convert_to_day_number(leaveBob)
        
        # Overlap interval: latest arrival and earliest departure
        overlap_start = max(a_arrive, b_arrive)
        overlap_end = min(a_leave, b_leave)
        
        # Calculate overlapping days if a valid range exists
        if overlap_start <= overlap_end:
            return (overlap_end - overlap_start) + 1
        
        return 0