import java.util.*;
public class Problem2 {
    static Scanner sc = new Scanner(System.in);
    static int inputNumber() {
        return sc.nextInt();
    }
    static int maxOfThree(int a, int b, int c) {
        return Math.max(a, Math.max(b, c));
    }
    public static void main(String[] args) {
        int a = inputNumber();
        int b = inputNumber();
        int c = inputNumber();
        System.out.println("Maximum: " + maxOfThree(a, b, c));
    }
}