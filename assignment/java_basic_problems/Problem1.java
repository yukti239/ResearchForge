import java.util.*;
public class Problem1 {
    static Random rand = new Random();
    static Scanner sc = new Scanner(System.in);
    static int generateGuess() {
        return rand.nextInt(100) + 1;
    }
    static String getFeedback(int guess) {
        System.out.println("Computer guesses: " + guess);
        System.out.print("Is it high, low, or correct? ");
        return sc.nextLine().toLowerCase();
    }
    public static void main(String[] args) {
        int guess;
        String feedback = "";
        while(!feedback.equals("correct")) {
            guess = generateGuess();
            feedback = getFeedback(guess);
        }
        System.out.println("Computer guessed correctly!");
    }
}