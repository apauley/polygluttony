// Solution by Etienne Labuschagne
// Edited by me to fit in with the other examples

public class SumOfNeighbours {
    public static int[] sumPairs(int[] a) {
	int[] newArray = new int[a.length-1];

	for (int i = 1; i < a.length; i++)
	    newArray[i-1] = a[i-1]+a[i];

	return newArray;
    }

    public static void main(String[] args) {
	int[] a = new int[]{1,2,3,4,5};
	sumPairs(a);
    }
}
