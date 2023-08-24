class Match:
    def __init__(self, location, team_01, team_02, timing):
        self.location = location
        self.team_01 = team_01
        self.team_02 = team_02
        self.timing = timing

    def __str__(self):
        return f"{self.location} {self.team_01} {self.team_02} {self.timing}"

class FlightTable:
    def __init__(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def search_by_team(self, team_name):
        results = [match for match in self.matches if match.team_01 == team_name or match.team_02 == team_name]
        return results

    def search_by_location(self, location):
        results = [match for match in self.matches if match.location == location]
        return results

    def search_by_timing(self, timing):
        results = [match for match in self.matches if match.timing == timing]
        return results

def main():
    # Initializing the flight table and adding matches
    table = FlightTable()
    table.add_match(Match("Mumbai", "India", "Sri Lanka", "DAY"))
    table.add_match(Match("Delhi", "England", "Australia", "DAY-NIGHT"))
    table.add_match(Match("Chennai", "India", "South Africa", "DAY"))
    table.add_match(Match("Indore", "England", "Sri Lanka", "DAY-NIGHT"))
    table.add_match(Match("Mohali", "Australia", "South Africa", "DAY-NIGHT"))
    table.add_match(Match("Delhi", "India", "Australia", "DAY"))

    while True:
        print("\nOptions to search by:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            team = input("Enter Team Name: ")
            results = table.search_by_team(team)
            if results:
                for match in results:
                    print(match)
            else:
                print("No matches found for the given team.")
                
        elif choice == 2:
            location = input("Enter Match Location: ")
            results = table.search_by_location(location)
            if results:
                for match in results:
                    print(match)
            else:
                print("No matches found for the given location.")

        elif choice == 3:
            timing = input("Enter Match Timing (DAY or DAY-NIGHT): ")
            results = table.search_by_timing(timing)
            if results:
                for match in results:
                    print(match)
            else:
                print("No matches found for the given timing.")
                
        elif choice == 4:
            print("Exiting program.")
            break

        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()
