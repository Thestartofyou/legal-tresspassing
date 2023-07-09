class BorderCrossing:
    def __init__(self, country, date, legal):
        self.country = country
        self.date = date
        self.legal = legal

class BorderTracker:
    def __init__(self):
        self.crossings = []

    def track_crossing(self, country, date, legal):
        crossing = BorderCrossing(country, date, legal)
        self.crossings.append(crossing)
        self.display_crossing_info(crossing)

    def display_crossing_info(self, crossing):
        legality = "Legal" if crossing.legal else "Illegal"
        print(f"Country: {crossing.country}\nDate: {crossing.date}\nLegality: {legality}\n")

# Example usage
tracker = BorderTracker()
tracker.track_crossing("Canada", "2023-07-08", True)
tracker.track_crossing("Mexico", "2023-07-07", False)
tracker.track_crossing("Canada", "2023-07-06", True)
