namespace ProjectEuler;

class P001_010 {

    public static void P001() {
        int somme = 0;
        for (int i = 1; i < 1000 ; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                somme += i;
            }
        }
        Console.WriteLine(somme);
    }

    public static void P002() {
        int a = 0, b = 1;
        int somme = 0;
        while (b < 4_000_000) {
            if (b % 2 == 0) somme += b;
            (a, b) = (b, a + b);
        }
        
        Console.WriteLine(somme);
    }

    public static void P003() {
        const long TARGET = 600851475143L;
        List<int> factors = Utils.GetPrimeFactors(TARGET);
        Console.WriteLine(factors.Last());
    }

    public static void P004() {
        int biggest = 0;
        for (int a = 100; a < 1000; a++) {
            for (int b = 100; b < 1000; b++) {
                if (a * b <= biggest) continue;
                if (Utils.IsPalindrome(a * b)) {
                    biggest = a * b;
                }
            }
        }

        Console.WriteLine(biggest);
    }

    public static void P005() {
        int n = Utils.LCM(1, 2);
        for (int i = 3; i <= 20; i++) {
            n = Utils.LCM(n, i);
        }
        Console.WriteLine(n);
    }

}
