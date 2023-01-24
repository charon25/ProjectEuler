namespace ProjectEuler;

class Program
{
    static void Main(string[] args)
    {
        Utils.LoadPrimes();

        if (args.Length == 0) {
            P001_010.P010();
        } else if (args[0] == "test") {
            Console.WriteLine("Running tests...\n");
            TestUtils.RunAllTests();
        }
    }
}
