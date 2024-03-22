import random


class Match:

  def __init__(self, player1, player2):
    self.player1 = player1
    self.player2 = player2


def create_matches(players):
  random.shuffle(players)
  if len(players) % 2 != 0:
    players.append('Bye')  # Add a 'Bye' player if the number of players is odd
  matches = []

  # Pair players
  for i in range(0, len(players), 2):
    match = Match(players[i], players[i + 1])
    matches.append(match)

  return matches


def print_matches(matches):
  print("Match Pairings:")
  for i, match in enumerate(matches, 1):
    print(f"Match {i}: {match.player1} vs {match.player2}")


def write_results_to_file(filename, round_number, matches, winners):
  with open(filename, 'a') as file:
    file.write(f"--- Round {round_number} Results ---\n")
    for i, match in enumerate(matches, 1):
      file.write(
          f"Match {i}: {match.player1} vs {match.player2} - Winner: {winners[i - 1]}\n"
      )
    file.write('\n')


if __name__ == "__main__":
  # Input player names
  num_players = int(input("Enter the number of players: "))
  players = [input(f"Enter player {i+1} name: ") for i in range(num_players)]

  # Initialize lists
  Still_Winning = players.copy()
  Not_Winning = []

  # Keep track of rounds
  round_number = 1
  while len(Still_Winning) > 1:
    print(f"\n--- Round {round_number} ---")
    matches_round = create_matches(Still_Winning)
    print_matches(matches_round)

    # Get winners for the current round matches
    winners_round = []
    for i, match in enumerate(matches_round, 1):
      winner = input(f"Enter winner for Match {i}: ")
      winners_round.append(winner)
    # Pair winning players for the next round
    Still_Winning = winners_round
    # Move non-winning players to Not_Winning
    for player in players:
      if player not in Still_Winning and player not in Not_Winning:
        Not_Winning.append(player)
    # Write results to file
    write_results_to_file('tournament_results.txt', round_number,
                          matches_round, winners_round)
    round_number += 1
  print("\nWinner:", Still_Winning[0])
  print("Players not winning:", Not_Winning)
  # New rounds for Not_Winning players until only one remains
  while len(Not_Winning) > 1:
    print(f"\n--- Not Winning Players Round {round_number} ---")
    matches_not_winning = create_matches(Not_Winning)
    print_matches(matches_not_winning)
    # Get winners for the Not_Winning round
    winners_not_winning = []
    for i, match in enumerate(matches_not_winning, 1):
      winner = input(f"Enter winner for Match {i}: ")
      winners_not_winning.append(winner)
    # Reset Not_Winning list and increment round number
    Not_Winning = winners_not_winning
    # Write results to file
    write_results_to_file('tournament_results.txt', round_number,
                          matches_not_winning, winners_not_winning)
    round_number += 1
  print("\nLast Player in Not Winning:", Not_Winning[0])
