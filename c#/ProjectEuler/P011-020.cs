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

}
