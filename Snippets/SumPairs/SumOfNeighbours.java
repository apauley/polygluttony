// Solution by Etienne Labuschagne

public class SumOfNeighbours
{
       public static void main(String[] args)
       {
               int[] originalArray = new int[]{1,2,3,4,5};
               int[] newArray = new int[4];

               for (int i = 1; i < originalArray.length; i++)
                       newArray[i-1] = originalArray[i-1]+originalArray[i];


               for (int i : newArray)
                       System.out.println(i);
       }
}
