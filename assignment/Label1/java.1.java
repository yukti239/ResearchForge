public class SmallestLargest {
    public static void main(String[] args) {
        int[] arr = {10, 50, 40, 20, 5};

        int smallest = arr[0];
        int largest = arr[0];

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < smallest) {
                smallest = arr[i];
            }
            if (arr[i] > largest) {
                largest = arr[i];
            }
        }

        System.out.println("Smallest value = " + smallest);
        System.out.println("Largest value = " + largest);
    }
}
