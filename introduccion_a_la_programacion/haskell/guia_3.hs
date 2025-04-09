absoluto :: Integer -> Integer
absoluto x | x >= 0 = x
           | x < 0 = -x

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z   | x >= y && x >= z = x 
                | y >= x && y >= z = y
                | otherwise = z


algunoEs0 :: Float -> Float -> Bool

---algunoEs0 x y   | x == 0 = True
---                | y == 0 = True
---                | otherwise = False 

algunoEs0 0 y = True
algunoEs0 x 0 = True
algunoEs0 x y = False


---ambosSon0:: Float -> Float -> Bool
---ambosSon0 x y   | x && y == 0 = True
---                | otherwise  = False

{-
ambosSon0 0 0 = True
ambosSon0 x y = False
-}

mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y  | x <= 3 && y <= 3 = True
                    | x > 3 && y > 3 && x <= 7 && y <= 7 = True
                    | x > 7 && y > 7 = True
                    | otherwise = False


sumaDistinto :: Integer -> Integer -> Integer -> Integer
sumaDistinto x y z  | x /= y && x /= z && y /= z = x + y + z 
                    | x /= y && x /= z && y == z = x + y
                    | x /= y && x == z = x + y
                    | x == y && x /= z = x + z
                    | otherwise = 0 

esMultiploDe :: Int -> Int -> Bool 
esMultiploDe x y    | mod x y == 0 = True
                    | otherwise = False

digitoUnidades :: Integer -> Integer
digitoUnidades x = mod (absoluto x) 10

digitoDecenas :: Integer -> Integer
digitoDecenas x = div (absoluto x) 10

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados x y   | mod x y == 0 = True
                        | otherwise = False

prodInt :: (Float,Float) -> (Float,Float) -> Float
prodInt (x1,x2) (y1,y2) = (x1 * y1) + (x2 * y2) 

todoMenor :: (Float,Float) -> (Float,Float) -> Bool
todoMenor (x1,x2) (y1,y2)   | x1 < y1 && x2 < y2 = True
                            | otherwise = False

distanciaPuntos :: (Float,Float) -> (Float,Float) -> Float
distanciaPuntos (x1,x2) (y1,y2) = sqrt(((x1-y1)^2)+((x2-y2)^2))

sumaTerna :: (Integer,Integer,Integer)->Integer
sumaTerna (x1,x2,x3) = x1 + x2 + x3

{-
sumarSoloMultiplos :: (Integer,Integer,Integer) -> Integer -> Integer
sumarSoloMultiplos (x1,x2,x3) y   | esMultiploDe x1 y == True && esMultiploDe x2 y == True && esMultiploDe x3 y == True = x1 + x2 + x3
                                | esMultiploDe x1 y == False && esMultiploDe x3 y == True && esMultiploDe x2 y == False = x1 + x3
                                | esMultiploDe x1 y == True && esMultiploDe x3 y == False && esMultiploDe x2 y = x1 + x2
                                | esMultiploDe x1 y == False && esMultiploDe x3 y == True && esMultiploDe x2 y == True = x2 + x3
                                | esMultiploDe x1 y == False && esMultiploDe x3 y == False && esMultiploDe x2 y == True  = x2
                                | esMultiploDe x1 y == True && esMultiploDe x3 y == False && esMultiploDe x2 y == False  = x1
                                | esMultiploDe x1 y == False && esMultiploDe x3 y == True && esMultiploDe x2 y == False  = x3
                                | otherwise = 0
-}
posPrimerPar :: (Integer,Integer,Integer) -> Integer
posPrimerPar (x1,x2,x3) | mod x1 2 == 0 && mod x2 2 /= 0 && mod x3 2 /= 0 = 0
                        | mod x1 2 /= 0 && mod x2 2 == 0 && mod x3 2 /= 0 = 1
                        | mod x1 2 == 0 && mod x2 2 /= 0 && mod x3 2 == 0 = 2
                        | mod x1 2 == 0 = 0
                        | mod x1 2 /= 0 && mod x2 2 == 0  = 1
                        | mod x1 2 /= 0 && mod x2 2 /= 0 && mod x3 2 == 0 = 2
                        | otherwise = 4

crearPar :: a -> b -> (a,b)
crearPar x y = (x,y)

invertir :: (a,b) -> (b,a)
invertir (x,y) = (y,x)


todosMenores :: (Integer,Integer,Integer) -> Bool
todosMenores (x,y,z) = f3(x) > g3(x) && f3(y) > g3(y) && f3(z) > g3(z)


f3 :: Integer -> Integer
f3 n    | n <= 7 = n^2
        | otherwise = (2*n) -1

g3 :: Integer -> Integer
g3 n    | mod n 2 == 0 = div n 2
        | otherwise = (3*n)+1

-- preguntar porq con 1900 es False y con 2000 es True
bisiesto :: Int -> Bool 
bisiesto año    | mod año 4 == 0 && mod año 100 /= 0 = True
                | mod año 4 == 0 && mod año 400 == 0 = True
                | otherwise = False

distanciaManhattan :: (Float,Float,Float) -> (Float,Float,Float) -> Float
distanciaManhattan (x1,x2,x3) (y1,y2,y3) = (abs (x1-y1))+(abs(x2-y2))+(abs(x3-y3))

comparar :: (Integer,Integer) -> Integer
comparar (a,b)  | sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b) = 1
                | sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b) = -1
                | sumaUltimosDosDigitos(a) == sumaUltimosDosDigitos(b) = 0

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = mod (abs x) 10 + mod (div (abs x) 10) 10