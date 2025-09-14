import java.util.*;
public class Problem9 {
    static int add(int a, int b) { return a+b; }
    static int subtract(int a, int b) { return a-b; }
    static int multiply(int a, int b) { return a*b; }
    static double divide(int a, int b) { return (double)a/b; }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        String op = sc.next();
        switch(op) {
            case "+": System.out.println(add(a,b)); break;
            case "-": System.out.println(subtract(a,b)); break;
            case "*": System.out.println(multiply(a,b)); break;
            case "/": System.out.println(divide(a,b)); break;
            default: System.out.println("Invalid");
        }
    }
}