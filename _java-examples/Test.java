public class Test {
    static public void test(int x, int y) {
        int z = x - y;

        if (x > y && y > 0) {
            if (z > 0) {
                System.out.println("z>0");
            } else {
                System.out.println("z<=0");
            }
        }


    }

    /* ----- Test Driver ----- */
    public static void main(String[] args) {
        test(1, 2);
    }
}