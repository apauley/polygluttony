// Scala solution by Julian Exenberger
// http://dotneverland.blogspot.com/2009/09/quick-sample-of-lists-and-tuples-in.html

val numbers = List(1,2,3,4,5);
numbers.zip(numbers.tail).flatMap {
     value => {
          List(value._1+value._2);
      }
};
