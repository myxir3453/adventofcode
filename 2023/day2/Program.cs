public record Game(int red, int green, int blue);

public static class Program
{
    public static void Main()
    {
        Game game1 = new(2, 4, 1);

        Console.WriteLine(game1);
    }
}