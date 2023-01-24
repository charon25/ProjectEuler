namespace ProjectEuler;

class TestUtils {

    public static void RunAllTests() {
        TestDigitsSum();
        TestDigitsProduct();
        TestPythagoreanTriplets();

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

}
