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

    public static int DigitsSum(int n) {
        return DigitsSum(n.ToString());
    }
    public static int DigitsSum(long n) {
        return DigitsSum(n.ToString());
    }
    public static int DigitsSum(string str) {
        int sum = 0;
        foreach (char c in str) sum += (c - '0');
        return sum;
    }

    public static long DigitsProduct(int n) {
        return DigitsProduct(n.ToString());
    }
    public static long DigitsProduct(long n) {
        return DigitsProduct(n.ToString());
    }
    public static long DigitsProduct(string str) {
        long product = 1;
        foreach (char c in str) {
            if (c == '0') return 0;
            product *= (c - '0');
        }
        return product;
    }


    // NUMBERS
    public static int GCD(int a, int b) {
        while (b > 0) {
            (a, b) = (b, a % b);
        }
        return a;
    }
    public static long GCD(long a, long b) {
        while (b > 0) {
            (a, b) = (b, a % b);
        }
        return a;
    }

    public static int LCM(int a, int b) {
        return (a / GCD(a, b)) * b;
    }
    public static long LCM(long a, long b) {
        return (a / GCD(a, b)) * b;
    }


}
