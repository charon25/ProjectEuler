using System.Numerics;

namespace ProjectEuler;

class TestUtils {

    public static void RunAllTests() {
        TestDigitsSum();
        TestDigitsProduct();
        TestPythagoreanTriplets();
        TestGetDivisorCountNotProper();
        TestFactorial();

        Console.WriteLine("");
    }

    private static void AssertEqual(object A, object B, string test) {
        if (!A.Equals(B)) throw new Exception($"Test {test} fail : {A} is not equal to {B}.");
        Console.Write(".");
    }
    private static void AssertLongArrayEqual(long[] A, long[] B, string test) {
        if (A.Length != B.Length)  throw new Exception($"Test {test} fail : arrays with different lengths : {A.Length} is not equal to {B.Length}.");
        for (int i = 0; i < A.Length; i++) {
            if (!A[i].Equals(B[i])) throw new Exception($"Test {test} fail : arrays with different elements at index {i} : {A[i]} is not equal to {B[i]}.");
        }
        Console.Write(".");
    }

    public static void TestDigitsSum() {
        AssertEqual(Utils.DigitsSum(123456), 1 + 2 + 3 + 4 + 5 + 6, "TestDigitsSum[int]");
        AssertEqual(Utils.DigitsSum(888888888888), 8 * 12, "TestDigitsSum[long]");
        AssertEqual(Utils.DigitsSum("123456"), 1 + 2 + 3 + 4 + 5 + 6, "TestDigitsSum[string]");
        AssertEqual(Utils.DigitsSum(new BigInteger(123456)), 1 + 2 + 3 + 4 + 5 + 6, "TestDigitsSum[BigInteger]");
    }

    public static void TestDigitsProduct() {
        AssertEqual(Utils.DigitsProduct(123456), (long)(1 * 2 * 3 * 4 * 5 * 6), "TestDigitsProduct[int]");
        AssertEqual(Utils.DigitsProduct(888888888888), 68719476736L, "TestDigitsProduct[long]");
        AssertEqual(Utils.DigitsProduct("123456"), (long)(1 * 2 * 3 * 4 * 5 * 6), "TestDigitsProduct[string]");
    }

    public static void TestPythagoreanTriplets() {
        long[] v = {3, 4, 5};
        long[] result = {5, 12, 13};
        AssertLongArrayEqual(Utils.MultiplyTriplet(v, Utils.R1), result, "TestPythagoreanTriplets[multiply]");

        long LIMIT = 700L;
        List<long[]> triplets = Utils.GeneratePythagoreanTriples(LIMIT);
        foreach (long[] triplet in triplets)
        {
            if (triplet[0] + triplet[1] + triplet[2] > LIMIT) throw new Exception("Test TestPythagoreanTriplets[limit:700] fail : triplet greater than limit.");
            AssertEqual(triplet[0] * triplet[0] + triplet[1] * triplet[1], triplet[2] * triplet[2], "TestPythagoreanTriplets[limit:700]");
        }
    }

    public static void TestGetDivisorCountNotProper() {
        AssertEqual(Utils.GetDivisorCount(6), 4, "TestGetDivisorCountNotProper[6]");
        AssertEqual(Utils.GetDivisorCount(25), 3, "TestGetDivisorCountNotProper[25]");
        AssertEqual(Utils.GetDivisorCount(1), 1, "TestGetDivisorCountNotProper[1]");
        AssertEqual(Utils.GetDivisorCount(17), 2, "TestGetDivisorCountNotProper[1]");
    }

    public static void TestGetDivisorCountProper() {
        AssertEqual(Utils.GetDivisorCount(6, true), 3, "TestGetDivisorCountProper[6]");
        AssertEqual(Utils.GetDivisorCount(25, true), 2, "TestGetDivisorCountProper[25]");
        AssertEqual(Utils.GetDivisorCount(1, true), 0, "TestGetDivisorCountProper[1]");
        AssertEqual(Utils.GetDivisorCount(17, true), 1, "TestGetDivisorCountProper[1]");
    }

    public static void TestFactorial() {
        AssertEqual(Utils.Factorial(0), new BigInteger(1), "TestFactorial[0]");
        AssertEqual(Utils.Factorial(1), new BigInteger(1), "TestFactorial[1]");
        AssertEqual(Utils.Factorial(3), new BigInteger(6), "TestFactorial[3]");
        AssertEqual(Utils.Factorial(10), new BigInteger(3628800), "TestFactorial[10]");
    }

}
