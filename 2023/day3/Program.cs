using System;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace AdventOfCode.Day3
{

    public class Program
    {
        private record Number(int Row, int Column, int Value);
        private record Symbol(int Row, int Column, char Character);

        public static void Main()
        {
            new Program().Run();
        }

        public void Run()
        {
            List<Number> numbers = new List<Number>();
            List<Symbol> symbols = new List<Symbol>();
            int lineNumber = 0;
            int lineLength = 0;

            // build number structure and symbol structure linked lists
            foreach (string line in File.ReadLines("input"))
            {
                lineLength = line.Length;

                numbers.AddRange(Regex.Matches(line, @"[0-9]+")
                    .Select(match => new Number(
                        Row: lineNumber,
                        Column: match.Index,
                        Value: int.Parse(match.Value))));

                symbols.AddRange(Regex.Matches(line, @"[^.0-9]")
                    .Select(match => new Symbol(
                        Row: lineNumber,
                        Column: match.Index,
                        Character: match.Value[0]
                    )));

                lineNumber++;
            }

            // build number matrix for easy lookup
            Number[,] numberMatrix = new Number[lineLength, lineLength];
            foreach (Number number in numbers)
            {
                int numberLength = number.Value.ToString().Length;
                int row = number.Row;
                for (int column = number.Column;column < Math.Min(lineLength, number.Column + numberLength);column++)
                {
                    numberMatrix[row, column] = number;
                }
            }

            // search for numbers adjacent to each symbol
            HashSet<Number> partNumbers = new HashSet<Number>();
            foreach (Symbol symbol in symbols)
            {
                //Console.WriteLine(symbol);
                for (int row = Math.Max(0, symbol.Row - 1);row < Math.Min(lineLength, symbol.Row + 2); row++)
                {
                    for (int column = Math.Max(0, symbol.Column - 1); column < Math.Min(lineLength, symbol.Column + 2); column++)
                    {
                        //Console.WriteLine($"searching for number at ({row}, {column})");
                        if (numberMatrix[row, column] != null)
                        {
                            partNumbers.Add(numberMatrix[row, column]);
                        }
                    }
                }
            }

            int partNumberSum = partNumbers.Sum(number => number.Value);
            Console.WriteLine(partNumberSum);
        }
    }
}
