namespace ProjectEuler;

class Utils {

    public static int PRIME_COUNT = 200_000;
    public static int[] PRIMES = new int[PRIME_COUNT];

    public static void LoadPrimes() {
        string[] lines = File.ReadAllLines("primes.txt");
        PRIMES = Array.ConvertAll<string, int>(lines, new Converter<string, int>(line => int.Parse(line)));
    }


    // PRIMES
    public static List<int> GetPrimeFactorsFast(int n) {
        List<int> factors = new List<int>();
        int index = 0;
        while (n > 1) {
            int p = PRIMES[index];
            while (n % p == 0) {
                factors.Add(p);
                n /= p;
            }
            index++;
        }
        return factors;
    }
    public static List<int> GetPrimeFactors(int n) {
        return GetPrimeFactors((long)n);
    }
    public static List<int> GetPrimeFactors(long n) {
        List<int> factors = new List<int>();
        int p = 2;
        while (n > 1) {
            while (n % p == 0) {
                factors.Add(p);
                n /= p;
            }
            p++;
        }
        return factors;
    }


    // STRING
    public static bool IsPalindrome(long n) {
        string n_str = n.ToString();
        return n_str.Equals(new string(n_str.Reverse().ToArray()));
    }


    // NUMBERS
    public static int GCD(int a, int b) {
        while (b > 0) {
            (a, b) = (b, a % b);
        }
        return a;
    }

    public static int LCM(int a, int b) {
        return (a / GCD(a, b)) * b;
    }
    public static long GCD(long a, long b) {
        while (b > 0) {
            (a, b) = (b, a % b);
        }
        return a;
    }
    public static long LCM(long a, long b) {
        return (a / GCD(a, b)) * b;
    }


}
