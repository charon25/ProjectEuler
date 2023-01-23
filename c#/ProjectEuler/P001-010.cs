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

}
