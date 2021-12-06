main = do
  s <- readFile "input.txt"
  print $ solve 0 0 (words s)

solve :: Int -> Int -> [String] -> Int
solve x y [] = x * y
solve x y (z1:z2:zs) = solve x' y' zs
    where 
        z2' = read z2 :: Int
        (x', y') = case z1 of 
            "forward" -> (x + z2', y)
            "up" -> (x, y - z2')
            "down" -> (x, y + z2')

     
