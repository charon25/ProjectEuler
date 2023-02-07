using System.Numerics;

namespace ProjectEuler;

class Utils {

    public static int PRIME_COUNT = 200_000;
    public static int[] PRIMES = new int[PRIME_COUNT];

    public static long[,] R1 = {{1, -2, 2}, {2, -1, 2}, {2, -2, 3}};
    public static long[,] R2 = {{1, 2, 2}, {2, 1, 2}, {2, 2, 3}};
    public static long[,] R3 = {{-1, 2, 2}, {-2, 1, 2}, {-2, 2, 3}};

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
    public static int GetDivisorCount(int n, bool proper = false) {
        return GetDivisorCount((long)n, proper);
    }
    public static int GetDivisorCount(long n, bool proper = false) {
        int count = 0;
        long sqrt_n = (long)Math.Sqrt(n);

        for (int d = 1; d <= sqrt_n; d++) {
            if (n % d == 0) count += 2;
        }
        if (sqrt_n * sqrt_n == n) count -= 1;

        return proper ? count - 1 : count;
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
    public static int DigitsSum(BigInteger n) {
        return DigitsSum(n.ToString());
    }
    public static int DigitsSum(string str) {
        return str.Sum(c => c - '0');
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

    public static BigInteger Factorial(int n) {
        BigInteger product = 1;
        for (int i = 2; i <= n; i++) product *= i;
        return product;
    }


    // OTHERS
    public static long[] MultiplyTriplet(long[] triplet, long[,] matrix) {
        long[] result = new long[3];
        for (int i = 0; i < 3; i++) {
            result[i] = matrix[i, 0] * triplet[0] + matrix[i, 1] * triplet[1] + matrix[i, 2] * triplet[2];
        }
        return result;
    }
    public static List<long[]> GeneratePythagoreanTriples(long limit) {
        List<long[]> triplets = new List<long[]>();
        Queue<long[]> triplets_to_do = new Queue<long[]>();
        long[] v = {3, 4, 5};
        triplets_to_do.Enqueue(v);

        while (triplets_to_do.Count > 0) {
            long[] triplet = triplets_to_do.Dequeue();
            if (triplet[0] + triplet[1] + triplet[2] > limit) continue;
            triplets.Add(triplet);
            triplets_to_do.Enqueue(MultiplyTriplet(triplet, R1));
            triplets_to_do.Enqueue(MultiplyTriplet(triplet, R2));
            triplets_to_do.Enqueue(MultiplyTriplet(triplet, R3));
        }

        return triplets;
    }


}
