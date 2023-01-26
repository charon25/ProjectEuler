namespace ProjectEuler;

class Program
{
    static void Main(string[] args)
    {
        Utils.LoadPrimes();

        if (args.Length == 0) {
            P011_020.P015();
        } else if (args[0] == "test") {
            Console.WriteLine("Running tests...\n");
            TestUtils.RunAllTests();
        }
    }
}
