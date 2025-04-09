nDigito :: Integer -> Integer -> Integer
nDigito n x = mod(div x (10^(n-1)))10
-- 1)
fibonacci:: Integer -> Integer
fibonacci x | x == 0 = 0
            | x == 1 = 1
            | otherwise = fibonacci(x-1) + fibonacci (x-2)

-- 2)
parteEntera :: Float -> Integer
parteEntera x   | x < (-1) && x < 0 = -1
                | x >= 0 && x < 1 = 0
                | x >= 1 = parteEntera(x-1) +1
                | otherwise = parteEntera(x+1) -1

-- 3)
esDivisible :: Integer -> Integer -> Bool
esDivisible x y | mod x y == 0 = True
                | otherwise = False

-- 4)
sumaImpares :: Integer -> Integer
sumaImpares x   | x == 1 = 1
                | otherwise = sumaImpares(x-1) + 2*x -1

-- 5) 
medioFact :: Integer -> Integer
medioFact x | x == 0 = 1
            | x == 1 = 1
            | otherwise = medioFact(x-2) * x

-- 6) 
sumaDigitos :: Integer -> Integer
sumaDigitos 0 = 0
sumaDigitos x = sumaDigitos(div x 10)+(mod x 10)

-- 7)
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales x   | x < 10 = True
                        | otherwise = ultimoDigito x == ultimoDigito(sacarUltimoDigito x) && todosDigitosIguales(sacarUltimoDigito x)

                        -- otherwise = (mod x 10) == (mod (div x 10) 10) && todosDigitosIguales(div x 10)

ultimoDigito :: Integer -> Integer
ultimoDigito x = mod x 10

sacarUltimoDigito :: Integer -> Integer
sacarUltimoDigito x = div x 10

-- 8)
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito x y = mod (div x (10^(cantDigitos(x)-y))) 10

cantDigitos :: Integer -> Integer
cantDigitos x   | x < 10 = 1 
                | otherwise = cantDigitos(div x 10) + 1


-- 10)
-- a)
f1 :: Integer -> Integer
f1 n    | n == 0 = 2^0
        | otherwise = 2^n + f1(n-1)

-- b)
f2 :: Integer -> Integer -> Integer
f2 n q  | q == 0 = 0
        | n == 1 = q
        | otherwise = (q^n) + (f2 (n-1)q) 

-- c)
f3 :: Integer -> Integer -> Integer
f3 n q = f2(2*n) q

-- d)
f4 :: Integer -> Integer -> Integer
f4 n q = f3 n q - f2 (n-1) q

-- 11) CONSULTAR PRACTICA: fromIntegral como se usa y entender esta funcion
eAprox :: Integer -> Float
eAprox 0 = 1
eAprox n = 1 / fromIntegral (factorial n) + eAprox (n - 1)

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

e :: Float
e = eAprox 10

-- 12) 
raizDe2Aprox :: Integer -> Float
raizDe2Aprox 1 = 1
raizDe2Aprox n = 1 + 1/sucesion(n-1)

sucesion :: Integer -> Float
sucesion 1 = 2
sucesion n = 2 + 1 / sucesion(n-1)

-- 16)
-- a)
menorDivisor :: Integer -> Integer
menorDivisor 0 = 0
menorDivisor 1 = 1
menorDivisor n = compararDivisores n 2

compararDivisores :: Integer -> Integer -> Integer
compararDivisores n i   | mod n i == 0 = i
                        | otherwise = (compararDivisores n (i+1))


-- b) 
esPrimo :: Integer -> Bool
esPrimo n   | menorDivisor n == n = True
            | otherwise = False 

-- c)
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos n x | n == x = False
                | esPrimo n && esPrimo x = True
                | mod x n == 0 || mod n x == 0 = False
                | menorDivisor x == menorDivisor n = False
                | menorDivisor x /= menorDivisor n = True
                | otherwise = False

-- d) 
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo 1 = 2
nEsimoPrimo n = proximoPrimo(nEsimoPrimo(n-1))

proximoPrimo :: Integer -> Integer
proximoPrimo n  | esPrimo(n+1) = n+1
                | otherwise = proximoPrimo(n+1)

-- 17)
esFibonacci :: Integer -> Bool
esFibonacci x  = fibonacciAux x 0

fibonacciAux :: Integer -> Integer -> Bool
fibonacciAux x i    | n == fibonacci i = True
                    | fibonacci i > n = False
                    | otherwise = fibonacciAux n (i+1)


