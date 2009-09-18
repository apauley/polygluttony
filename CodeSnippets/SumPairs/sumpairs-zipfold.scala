// Scala solution by Julian Exenberger
// http://dotneverland.blogspot.com/2009/09/quick-sample-of-lists-and-tuples-in.html

object SumPairs extends Application {

val numbers = List(1,2,3,4,5);
val result = numbers.zip(numbers.tail)
             .foldLeft(List[Int]()) (
                (list, y) => {
                   y._1 + y._2 :: list
                }
              )
             .reverse;
println(result);

}
