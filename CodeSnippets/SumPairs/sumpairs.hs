{- Haskell solution by Danie Roux -}

let x = [1, 2, 3, 4, 5]
zipWith (+) x (tail x)
