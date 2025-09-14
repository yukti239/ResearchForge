import java.util.Scanner;
public class Program8 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        int sum = 0, temp = number;
        while (temp > 0) {
            sum += temp % 10;
            temp /= 10;
        }
        if (number % sum == 0) System.out.println("Harshad Number");
        else System.out.println("Not Harshad Number");
    }
}