using System;
using System.Collections;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace AdventOfCode.Day7
{

    public class Program
    {
        public enum CardType
        {
            FiveOfAKind = 7,
            FourOfAKind = 6,
            FullHouse = 5,
            ThreeOfAKind = 4,
            TwoPair = 3,
            OnePair = 2,
            HighCard = 1
        }

        public static readonly Dictionary<char, int> CardValues = new Dictionary<char, int>()
        {
            { 'A', 14 }, { 'K', 13 }, { 'Q', 12 }, { 'T', 10 },
            { '9', 9 },  { '8', 8 },  { '7', 7 },  { '6', 6 },  { '5', 5 },
            { '4', 4 },  { '3', 3 },  { '2', 2 }, { 'J', 1 }
        };

        public class Hand : IComparable
        {
            public char[] Cards { get; private set; }
            public int Bid { get; private set; }

            private CardType? _cardType = null;
            public CardType Type
            {
                get
                {
                    if (_cardType == null)
                    {
                        var charGroups = Cards
                            .GroupBy(c => c)
                            .Select(c => new  { Char = c.Key, Count = c.Count() })
                            .OrderByDescending(c => c.Count)
                            .ToArray();
                        if (charGroups.Count() == 1)
                        {
                            _cardType = CardType.FiveOfAKind;
                        }
                        else if (charGroups.Count() == 2)
                        {
                            if (charGroups[0].Count == 4)
                            {
                                if (charGroups[0].Char == 'J' || charGroups[1].Char == 'J')
                                {
                                    _cardType = CardType.FiveOfAKind;
                                }
                                else
                                {
                                    _cardType = CardType.FourOfAKind;
                                }
                            }
                            else
                            {
                                if (charGroups[0].Char == 'J' || charGroups[1].Char == 'J')
                                {
                                    _cardType = CardType.FiveOfAKind;
                                }
                                else
                                {
                                    _cardType = CardType.FullHouse;
                                }
                            }
                        }
                        else if (charGroups.Count() == 3)
                        {
                            if (charGroups[0].Count == 3)
                            {
                                if (charGroups[0].Char == 'J' ||
                                    charGroups[1].Char == 'J' ||
                                    charGroups[2].Char == 'J')
                                {
                                    _cardType = CardType.FourOfAKind;
                                }
                                else
                                {
                                    _cardType = CardType.ThreeOfAKind;
                                }
                            }
                            else
                            {
                                if (charGroups[0].Char == 'J' ||
                                    charGroups[1].Char == 'J')
                                {
                                    _cardType = CardType.FourOfAKind;
                                }
                                else if (charGroups[2].Char == 'J')
                                {
                                    _cardType = CardType.FullHouse;
                                }
                                else
                                {
                                    _cardType = CardType.TwoPair;
                                }
                            }
                        }
                        else if (charGroups.Count() == 4)
                        {
                            if (charGroups[0].Char == 'J')
                            {
                                _cardType = CardType.ThreeOfAKind;
                            }
                            else if (charGroups[1].Char == 'J' ||
                                     charGroups[2].Char == 'J' ||
                                     charGroups[3].Char == 'J')
                            {
                                _cardType = CardType.ThreeOfAKind;
                            }
                            else
                            {
                                _cardType = CardType.OnePair;
                            }
                        }
                        else
                        {
                            if (charGroups[0].Char == 'J' ||
                                charGroups[1].Char == 'J' ||
                                charGroups[2].Char == 'J' ||
                                charGroups[3].Char == 'J' ||
                                charGroups[4].Char == 'J')
                            {
                                _cardType = CardType.OnePair;    
                            }
                            else
                            {
                                _cardType = CardType.HighCard;
                            }
                        }
                    }
                    return _cardType.Value;
                }
            }

            public Hand(char[] cards, int bid)
            {
                Cards = cards;
                Bid = bid;
            }

            public int CompareTo(object? obj)
            {
                if (obj == null) return 1;

                Hand other = obj as Hand;
                if (other == null)
                    throw new ArgumentException("Object is not a Hand");
                if (this.Type < other.Type)
                    return -1;
                if (this.Type > other.Type)
                    return 1;
                if (CardValues[this.Cards[0]] < CardValues[other.Cards[0]])
                    return -1;
                if (CardValues[this.Cards[0]] > CardValues[other.Cards[0]])
                    return 1;
                if (CardValues[this.Cards[1]] < CardValues[other.Cards[1]])
                    return -1;
                if (CardValues[this.Cards[1]] > CardValues[other.Cards[1]])
                    return 1;
                if (CardValues[this.Cards[2]] < CardValues[other.Cards[2]])
                    return -1;
                if (CardValues[this.Cards[2]] > CardValues[other.Cards[2]])
                    return 1;
                if (CardValues[this.Cards[3]] < CardValues[other.Cards[3]])
                    return -1;
                if (CardValues[this.Cards[3]] > CardValues[other.Cards[3]])
                    return 1;
                if (CardValues[this.Cards[4]] < CardValues[other.Cards[4]])
                    return -1;
                if (CardValues[this.Cards[4]] > CardValues[other.Cards[4]])
                    return 1;
                return 0;
            }
        }

        public static void Main()
        {
            new Program().Run();
        }

        public void Run()
        {
            string[] lines = File.ReadAllLines("input");
            List<Hand> hands = new List<Hand>();
            foreach (string line in lines)
            {
                char[] cards = line.Split(' ')[0].ToCharArray();
                int bid = int.Parse(line.Split(' ')[1]);
                Hand hand = new Hand(cards, bid);
                hands.Add(hand);
            }

            hands[2].CompareTo(hands[3]);
            hands[1].CompareTo(hands[4]);

            var orderedHands = hands.Order().ToList();
            var handRanks = hands.Select(h => orderedHands.IndexOf(h) + 1).ToArray();

            int totalWinnings = 0;
            for (int i = 0;i < hands.Count;i++)
            {
                totalWinnings += hands[i].Bid * handRanks[i];
            }
            Console.WriteLine(totalWinnings);
        }
    }
}
