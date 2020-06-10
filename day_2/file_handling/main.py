import csv

from winner import *

winners = []

with open("oscars.csv", "r") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader)
    for row in reader:
        current_winner = Winner(*row)
        winners.append(current_winner)

# with open("oscars.csv", "r") as csvfile:
#     reader = csv.reader(csvfile, skipinitialspace=True)
#     count = sum(1 for row in reader)
#
# with open("oscars.csv", "a") as csvfile:
#     writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
#     winner = Winner(count, 2020, 50, "Renee Zellweger", "Judy")
#     writer.writerow(winner.values())

with open("oscars.csv", "w") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    writer.writerow(["Index", "Year", "Age", "Name", "Movie"])

    for winner in winners:
        if winner.year == 2020:
            winner.age += 1
        writer.writerow(winner.values())

# for winner in winners:
#   print(f"{winner.name} won the oscar for {winner.movie} in {winner.year} aged {winner.age}")

  with open("oscars.csv", "r") as csvfile:
      reader = csv.reader(csvfile, skipinitialspace=True)
      next(reader)

      # eighties = []
      # for row in reader:
      #     row[1][0:3] == "198":
      #     winner = Winner(*row)
      #     eighties.append(winner)

eighties = [winner for winner]

print(eighties)
