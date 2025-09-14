import java.util.*;
public class Problem5 {
    static boolean isPalindrome(String s) {
        String rev = new StringBuilder(s).reverse().toString();
        return s.equalsIgnoreCase(rev);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        System.out.println(isPalindrome(str) ? "Palindrome" : "Not Palindrome");
    }
}