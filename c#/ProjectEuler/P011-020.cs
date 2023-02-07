using System.Numerics;

namespace ProjectEuler;

class P011_020 {


    public static int BiggestProductOnRow(int[,] grid) {
        int biggest = 0;
        for (int col = 0; col < grid.GetLength(1); col++) {
            for (int row = 0; row < grid.GetLength(0) - 4; row++) {
                int s = grid[row, col] * grid[row + 1, col] * grid[row + 2, col] * grid[row + 3, col];
                if (s > biggest) biggest = s;
            }
        }
        return biggest;
    }
    public static void P011() {
        const int SIZE = 20;
        int[,] grid = new int[SIZE, SIZE];
        string[] lines = File.ReadAllLines("data\\011.txt");
        for (int row = 0; row < SIZE; row++) {
            string[] values = lines[row].Split(" ");
            for (int col = 0; col < SIZE; col++) {
                grid[row, col] = int.Parse(values[col]);
            }
        }

        int biggest = 0;

        int[,] left_shifted_grid = new int[SIZE, 2 * SIZE - 1];
        int[,] right_shifted_grid = new int[SIZE, 2 * SIZE - 1];
        for (int row = 0; row < SIZE; row++) {
            for (int col = 0; col < SIZE; col++) {
                if (col < SIZE - 4) {
                    int s = grid[row, col] * grid[row, col + 1] * grid[row, col + 2] * grid[row, col + 3];
                    if (s > biggest) biggest = s;
                }
                left_shifted_grid[row, col + SIZE - 1 - row] = grid[row, col];
                right_shifted_grid[row, col + row] = grid[row, col];
            }
        }
        biggest = Math.Max(biggest, BiggestProductOnRow(grid));
        biggest = Math.Max(biggest, BiggestProductOnRow(right_shifted_grid));
        biggest = Math.Max(biggest, BiggestProductOnRow(left_shifted_grid));


        Console.WriteLine(biggest);
    }

    public static void P012() {
        const int TARGET = 500;
        int n = 1;
        while (true) {
            int t = (n * (n + 1)) / 2;
            if (Utils.GetDivisorCount(t) > TARGET) {
                Console.WriteLine(t);
                break;
            }
            n++;
        }
    }

    public static void P013() {
        string[] lines = File.ReadAllLines("data\\013.txt");
        BigInteger sum = 0;
        foreach (string line in lines) {
            sum += BigInteger.Parse(line);
        }

        Console.WriteLine(sum.ToString().Substring(0, 10));
    }

    public static int CollatzSequenceLength(long n) {
        int length = 0;
        while (n > 1) {
            if (n % 2 == 0) {
                n /= 2;
                length++;
            } else {
                n = (3 * n + 1);// / 2;
                length++;
            }
        }
        return length;
    }
    public static void P014() {
        const int LIMIT = 1_000_000;
        int biggest = 0, longest = 0;
        for (int n = 1 ; n < LIMIT; n++) {
            int length = CollatzSequenceLength((long)n);
            if (length > longest) {
                longest = length;
                biggest = n;
            }
        }

        Console.WriteLine(biggest);
    }

    public static void P015() {
        BigInteger factorial_40 = Utils.Factorial(40);
        BigInteger factorial_20 = Utils.Factorial(20);
        Console.WriteLine(factorial_40 / (factorial_20 * factorial_20));
    }

    public static void P016() {
        BigInteger n = new BigInteger(2);
        n = BigInteger.Pow(n, 1000);

        Console.WriteLine(Utils.DigitsSum(n));
    }

    private static int LettersCount(int n) {
        int[] UNITS = {0, 3, 3, 5, 4, 4, 3, 5, 5, 4};
        int[] TEENS = {3, 6, 6, 8, 8, 7, 7, 9, 8, 8};
        int[] TENS = {0, 0, 6, 6, 5, 5, 5, 7, 6, 6};

        if (n < 10) return UNITS[n];
        if (n < 20) return TEENS[n - 10];
        if (n < 100) return TENS[(n - n % 10) / 10] + UNITS[n % 10];
        if (n == 1000) return 3 + 8;

        int c = n / 100;
        if (n % 100 == 0) {
            return UNITS[c] + 7;
        } else {
            return UNITS[c] + 7 + 3 + LettersCount(n % 100);
        }
    }

    public static void P017() {
        Console.WriteLine(Enumerable.Range(1, 1000).Sum(n => LettersCount(n)));
    }

    public static void P018() {
        string[] lines = File.ReadAllLines("data\\018.txt");
        int N = lines.Length;
        int[,] triangle = new int[N, N];
        for (int y = 0; y < N; y++) {
            string[] values = lines[y].Split(' ');
            for (int x = 0; x < N; x++) {
                if (x < values.Length) triangle[y, x] = int.Parse(values[x]);
                else triangle[y, x] = -1;
            }
        }

        for (int y = 1; y < N; y++) {
            for (int x = 0; x <= y; x++) {
                if (x == 0)
                    triangle[y, x] = triangle[y, x] + triangle[y - 1, x];
                else if (x == y)
                    triangle[y, x] = triangle[y, x] + triangle[y - 1, x - 1];
                else
                    triangle[y, x] = triangle[y, x] + Math.Max(triangle[y-1, x - 1], triangle[y - 1, x]);
            }
        }

        int max = 0;
        for (int x = 0; x < N; x++) {
            if (triangle[N - 1, x] > max) max = triangle[N - 1, x];
        }

        Console.WriteLine(max);
    }

    public static void P019() {
        DateTime date = new DateTime(1901, 1, 1);
        TimeSpan oneDay = new TimeSpan(1, 0, 0, 0);

        int total = 0;
        while (date.Year <= 2000) {
            if (date.Day == 1 && date.DayOfWeek == DayOfWeek.Sunday)
                total += 1;
            date = date.Add(oneDay);
        }

        Console.WriteLine(total);
    }

    public static void P020() {
        Console.WriteLine(Utils.DigitsSum(Utils.Factorial(100)));
    }

}
