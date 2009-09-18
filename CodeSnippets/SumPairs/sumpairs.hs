-- Haskell solution by Danie Roux

a = [1, 2, 3, 4, 5]
main = print (zipWith (+) a (tail a))
