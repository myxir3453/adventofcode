using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace AdventOfCode.Day2
{
    public record GameSubset(int Red, int Green, int Blue);
    public record Game(int Id, GameSubset[] Subsets);

    public class Program
    {
        public static void Main()
        {
            new Program().Run();
        }

        public void Run()
        {
            var sw = new Stopwatch();
            sw.Start();

            Game[] games = File.ReadLines("input")
                .Select(ParseGame)
                .ToArray();

            // part 1
            List<Game> possibleGames = GetPossibleGames(games, 12, 13, 14);
            int sumOfPossibleGamesId = possibleGames
                .Select(game => game.Id)
                .Sum();
            Console.WriteLine(sumOfPossibleGamesId);

            // part 2
            int part2Value = games.Select(game =>
                {
                    int maxRed = game.Subsets.Select(subset => subset.Red).Max();
                    int maxGreen = game.Subsets.Select(subset => subset.Green).Max();
                    int maxBlue = game.Subsets.Select(subset => subset.Blue).Max();
                    int power = maxRed * maxGreen * maxBlue;
                    return power;
                }
            )
            .Sum();
            Console.WriteLine(part2Value);

            sw.Stop();
            var elapsedTime = sw.Elapsed.TotalMilliseconds;

            Console.WriteLine($"Elapsed time: {elapsedTime} ms");
        }

        public List<Game> GetPossibleGames(Game[] games, int maxRedCubes, int maxGreenCubes, int maxBlueCubes)
        {
            List<Game> possibleGames = new List<Game>();
            foreach (Game game in games)
            {
                bool possible = true;

                foreach (GameSubset gameSubset in game.Subsets)
                {
                    if (gameSubset.Red > maxRedCubes ||
                        gameSubset.Green > maxGreenCubes ||
                        gameSubset.Blue > maxBlueCubes)
                        {
                            possible = false;
                            break;
                        }
                }

                if (possible)
                {
                    possibleGames.Add(game);                    
                }
            }
            return possibleGames;
        }

        public Game ParseGame(string line)
        {
            Match match = Regex.Match(line, @"Game (?<gameNumber>\d+): (?<gameSubsets>.*)");
            int gameNumber = int.Parse(match.Groups["gameNumber"].Value);                
            GameSubset[] gameSubsets = match.Groups["gameSubsets"].Value
                .Split(';')
                .Select(ParseGameSubset)
                .ToArray();

            var game = new Game(gameNumber, gameSubsets);

            return game;
        }

        public GameSubset ParseGameSubset(string strGameSubset)
        {
            MatchCollection matches = Regex.Matches(strGameSubset, @"(?<cubeNumber>[0-9]+) (?<cubeColor>[a-z]+)");
            
            int red = 0;
            int green = 0;
            int blue = 0;

            foreach (Match match in matches)
            {
                int cubeNumber = int.Parse(match.Groups["cubeNumber"].Value);
                string cubeColor = match.Groups["cubeColor"].Value;
                
                if (cubeColor == "red")
                    red = cubeNumber;
                else if (cubeColor == "green")
                    green = cubeNumber;
                else if (cubeColor == "blue")
                    blue = cubeNumber;
            }

            return new GameSubset(red, green, blue);
        }
    }
}
