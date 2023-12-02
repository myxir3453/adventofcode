using System;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace AdventOfCode.Day2
{
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

            // part 1
            int part1Value = 0;
            int part2Value = 0;
            int gameNumber = 1;
            foreach (string line in File.ReadAllLines("input"))
            {
                int maxRedValue = Regex.Matches(line, @"([0-9]+) red")
                    .Select(match => match.Value.Split(' ')[0])
                    .Select(int.Parse)
                    .Max();
                int maxGreenValue = Regex.Matches(line, @"([0-9]+) green")
                    .Select(match => match.Value.Split(' ')[0])
                    .Select(int.Parse)
                    .Max();
                int maxBlueValues = Regex.Matches(line, @"([0-9]+) blue")
                    .Select(match => match.Value.Split(' ')[0])
                    .Select(int.Parse)
                    .Max();

                if (maxRedValue <= 12 &&
                    maxGreenValue <= 13 &&
                    maxBlueValues <= 14)
                {
                    part1Value += gameNumber;
                }

                part2Value += maxRedValue * maxGreenValue * maxBlueValues;

                gameNumber++;
            }

            Console.WriteLine(part1Value);
            Console.WriteLine(part2Value);

            sw.Stop();
            var elapsedTime = sw.Elapsed.TotalMilliseconds;

            Console.WriteLine($"Elapsed time: {elapsedTime} ms");
        }
    }
}
