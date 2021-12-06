main = do
  s <- readFile "input.txt"
  print $ solve 0 0 0 (words s)

solve :: Int -> Int -> Int -> [String] -> Int
solve x y a [] = x * y
solve x y a (z1:z2:zs) = solve x' y' a' zs
    where 
        z2' = read z2 :: Int
        (x', y', a') = case z1 of 
            "forward" -> (x + z2', y + (a * z2'), a)
            "up" -> (x, y, a - z2')
            "down" -> (x, y, a + z2')

     
