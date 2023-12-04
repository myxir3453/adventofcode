using System;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace AdventOfCode.Day4
{

    public class Program
    {
        private record Card(int Number, int Matches);

        public static void Main()
        {
            new Program().Run();
        }

        private void Run()
        {
            Card[] cards = File.ReadLines("input")
                .Select(ProcessCard)
                .ToArray();

            // part 1
            int totalWorth = cards.Sum(card => card.Matches == 0 ? 0 : (1 << (card.Matches - 1)));
            Console.WriteLine(totalWorth);
        }

        private Card ProcessCard(string line)
        {
            Match match = Regex.Match(line, @"Card ([0-9 ]+): ([0-9 ]+) \| ([0-9 ]+)");
            int cardNumber = int.Parse(match.Groups[1].Value);
            int[] winningNumbers = match.Groups[2].Value
                .Split(' ', StringSplitOptions.RemoveEmptyEntries)
                .Select(int.Parse)
                .ToArray();
            int[] numbersYouHave = match.Groups[3].Value
                .Split(' ', StringSplitOptions.RemoveEmptyEntries)
                .Select(int.Parse)
                .ToArray();
            int[] winningNumbersFreq = new int[100];
            foreach (int winningNumber in winningNumbers)
            {
                winningNumbersFreq[winningNumber]++;
            }
            int[] numbersYouHaveFreq = new int[100];
            foreach (int numberYouHave in numbersYouHave)
            {
                numbersYouHaveFreq[numberYouHave]++;
            }
            int matches = 0;
            for (int i = 0;i < 100;i++)
            {
                matches += (winningNumbersFreq[i] & numbersYouHaveFreq[i]) > 0 ? 1 : 0;
            }
            //Console.WriteLine($"card {cardNumber}: {matches} matches");
            return new Card(cardNumber, matches);
        }
    }
}
