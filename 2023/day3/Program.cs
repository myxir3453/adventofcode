using System;
using System.Diagnostics;
using System.IO;
using System.Linq;

namespace AdventOfCode.Day3
{

    public class Program
    {
        private record Number(int Id, int Row, int Column, int Value);
        private record Symbol(int Id, int Row, int Column, char Character);

        public static void Main()
        {
            new Program().Run();
        }

        public void Run()
        {
            foreach (string line in File.ReadLines("testinput"))
            {
                MatchCollection numberMatches = Regex.Matches(line, @"[0-9]+");
                foreach (Match match in numberMatches)
                {
                    
                }
            }
        }
    }
}
