class Solution:

  def countDaysTogether(
      self,
      arriveAlice: str,
      leaveAlice: str,
      arriveBob: str,
      leaveBob: str,
  ) -> int:
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def to_day_of_year(date: str) -> int:
      # Indented 4 spaces inside to_day_of_year
      month = int(date[:2])
      day = int(date[3:])
      return sum(days_in_months[: month - 1]) + day

    start_alice = to_day_of_year(arriveAlice)
    end_alice = to_day_of_year(leaveAlice)
    start_bob = to_day_of_year(arriveBob)
    end_bob = to_day_of_year(leaveBob)

    start_together = max(start_alice, start_bob)
    end_together = min(end_alice, end_bob)

    return max(0, end_together - start_together + 1)