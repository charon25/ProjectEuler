namespace ProjectEuler;

class TestUtils {

    public static void RunAllTests() {
        TestDigitsSum();
        TestDigitsProduct();

        Console.WriteLine("");
    }

    private static void AssertEqual(object A, object B, string test) {
        if (!A.Equals(B)) throw new Exception($"Test {test} fail : {A} is not equal to {B}.");
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

}
