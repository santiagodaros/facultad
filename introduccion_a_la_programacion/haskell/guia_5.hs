-- 1)
-- a)
longitud :: [t] -> Integer
longitud [] = 0
longitud [x] = 1
longitud (x:xs) = 1 + longitud xs

-- b)
ultimo :: [t] -> [t]
ultimo [x] = [x]
ultimo (x:xs)   | longitud xs == 0 = [x]
                | otherwise = ultimo xs 
-- [1,2,3] -> [3]

-- c)
principio :: [t] -> [t]
principio [] = []
principio (x:xs)    | longitud xs /= 0 = x : principio xs
                    | longitud xs == 0 = principio []

-- d) 
reverso :: [t] -> [t]
reverso [x] = [x]
reverso (x:xs)  = reverso xs ++ [x]

-- [1,2,3] -> [3] ++ [2] ++ [1]

-- 2)
-- a)
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:ys)  | x == y = True
                    | otherwise = pertenece x ys

-- b)
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales (x:y:xs)   | x /= y = False
                        | x == y = todosIguales xs

-- [1,1,1,1] -> True

-- c) 
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:y:xs) | x /= y = todosDistintos xs
                        | x == y = False

-- d)
hayRepetidos ::  (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) | (pertenece x xs) == True = True
                    | otherwise = hayRepetidos xs

-- e)
quitar :: (Eq t) => t -> [t] -> [t]
quitar x (y:ys) | not(pertenece x (y:ys)) = (y:ys)
                | x == y = ys
                | x /= y = y:quitar x ys


-- f)
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos x [] = []
quitarTodos x (y:ys)    | not(pertenece x (y:ys)) = (y:ys)
                        | x == y = quitarTodos x ys
                        | x /= y = y: quitarTodos x ys

-- g)
eliminarRepetidos ::  (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs)    | hayRepetidos (x:xs) == False = (x:xs)
                            | pertenece x xs = x: quitarTodos x (eliminarRepetidos xs)
                            | otherwise = x : eliminarRepetidos xs

-- [1,1,1,2,3] -> [1,2,3]

-- h)
mismosElementos ::  (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos (x:xs) (y:ys)   | x == y = mismosElementos xs ys
                                | otherwise = False

-- i) 
capicua ::  (Eq t) => [t] -> Bool
capicua [] = True
capicua (x:xs)  | (x:xs) == reverso((x:xs)) = True
                | otherwise = False

-- 3)
-- a) 
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

-- b)
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * (productoria xs)

-- c)
maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:xs)   | x >= maximo xs = x
                | otherwise = maximo xs

-- d) 
sumarN ::  Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN x (y:ys)  = (x+y) : sumarN x ys

-- e) 
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [x] = [x]
sumarElPrimero (x:xs) = sumarN x (x:xs)

-- f)
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [x] = [x]
--sumarElUltimo (x:xs) = (sumarN (ultimo (x:xs)) (x:xs))

-- g)
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs)    | esPar x == True = x : pares xs 
                | esPar x == False = pares xs

esPar :: Integer -> Bool
esPar x | mod x 2 == 0 = True
        | otherwise = False

-- h)
multiplosDeN :: Integer -> [Integer] -> [Integer] 
multiplosDeN _ [] = []
multiplosDeN x (y:ys)   | mod y x == 0 = y: multiplosDeN x ys
                        | otherwise = multiplosDeN x ys

-- i)
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar [x] = [x]
ordenar (x:xs)  | (maximo (x:xs)) == x = (ordenar xs) ++ [x]
                | otherwise = ordenar (quitar (maximo (x:xs))(x:xs)) ++ [maximo(x:xs)]

ordenar2 :: [Integer] -> [Integer]
ordenar2 [] = []
ordenar2 (x:xs)  = ordenar2 (quitar (maximo (x:xs))(x:xs)) ++ [maximo(x:xs)]

-- 4)
-- a)
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs)  | x == y && x == ' ' = x : sacarBlancosRepetidos xs
                                | otherwise = x: sacarBlancosRepetidos (y:xs)

esBlanco :: Char -> Bool
esBlanco x  | x == ' '= True
            | otherwise = False

-- b)

contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras (x:xs) = contarEspacios (limpiarCadena xs) + 1

contarEspacios :: [Char] -> Integer
contarEspacios [] = 0
contarEspacios (x:xs)   | x == ' ' = 1 + contarEspacios xs
                        | otherwise = contarEspacios xs

sacarEspaciosInicio :: [Char] -> [Char]
sacarEspaciosInicio [] = []
sacarEspaciosInicio (x:xs)  | x == ' ' = xs
                            | otherwise = (x:xs)

sacarEspaciosInicio2 :: [Char] -> [Char]
sacarEspaciosInicio2 [] = []
sacarEspaciosInicio2 (x:xs) | x == ' ' = quitar ' ' (x:xs)


sacarEspacioFinal :: [Char] -> [Char]
sacarEspacioFinal [] = []
sacarEspacioFinal (x:[])    | x == ' ' = []
                            | otherwise = [x]

sacarEspacioFinal (x:xs) = x : sacarEspacioFinal xs

limpiarCadena :: [Char] -> [Char]
limpiarCadena xs = sacarEspaciosInicio(sacarEspacioFinal (sacarBlancosRepetidos xs))

-- ['h','o','l','a',' ','c','a','g','o','n']

-- c)
palabras :: [Char] -> [[Char]]
palabras [] = []
palabras xs = primeraPalabra xs : palabras (sacarPrimeraPalabra (limpiarCadena xs))

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (x:xs) | x ==' ' =[]
                      | otherwise = x:primeraPalabra xs

sacarPrimeraPalabra :: [Char] -> [Char]
sacarPrimeraPalabra [] =[]
sacarPrimeraPalabra (x:xs) | x==' ' = xs
                           | otherwise = sacarPrimeraPalabra xs
-- ['h','o','l','a',' ','c','a','g','o','n'] -> [['h','o','l','a'],['c','a','g','o','n']]

-- d) 
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [] = []
palabraMasLarga xs = palabraLongitud (limpiarCadena xs)

palabraLongitud :: [Char] -> [Char]
palabraLongitud [] = []
palabraLongitud xs      | sacarPrimeraPalabra xs == [] = primeraPalabra xs
                        | longitud (primeraPalabra xs) > longitud (palabraLongitud (sacarPrimeraPalabra xs)) = primeraPalabra xs
                        | otherwise = palabraLongitud (sacarPrimeraPalabra xs)

-- e) 
aplanar :: [String] -> String
aplanar [] = []
aplanar (xs:xss) = xs ++ aplanar xss

-- f) 
aplanarConBlancos :: [String] -> String
aplanarConBlancos [] = []
aplanarConBlancos (xs:xss)      | xss == [] = xs
                                | otherwise = xs ++ " " ++ aplanarConBlancos xss

-- g)
aplanarConNBlancos :: [String] -> Integer -> String
aplanarConNBlancos [] _ = []
aplanarConNBlancos (xs:xss) x   | xss == [] = xs
                                | otherwise = xs ++ agregarBlancos x ++ aplanarConNBlancos xss x


agregarBlancos :: Integer -> String
agregarBlancos 0 = []
agregarBlancos n = " " ++ agregarBlancos(n-1)

-- 5) 
-- a)
sumaAcumulada ::  (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada [x] = [x]
sumaAcumulada (x:xs)  = x : sumaAcumulada ((head(xs) + x):tail xs)


-- b)
descomponer :: Int -> Int -> [Int]
descomponer 1 _ = []
descomponer x divisor   | mod n divisor == 0 = divisor : descomponer (div x divisor) divisor
                        | otherwise = descomponer x (divisor + 1)

-- 6)
-- a)

enLosContactos :: String -> [(String,String)] -> [(String,String)]
enLosContactos n [] = []
enLosContactos n ((x,y):xs)     | n == x = [(x,y)]
                                | otherwise = enLosContactos n xs


-- b)
agregarContacto :: (String,String) -> [(String,String)] -> [(String,String)] 
agregarContacto (x,y) [] = [(x,y)]
agregarContacto (x,y) ((h1,h2):hs)      | x == h1 = (x,y) : hs
                                        | otherwise = (h1,h2) : agregarContacto (x,y) hs


-- c)
eliminarContacto :: String -> [(String,String)] -> [(String,String)]
eliminarContacto n [] = []
eliminarContacto n ((x,y):xs)   | n == x = (tail ((x,y):xs))
                                | otherwise = (x,y) : eliminarContacto n xs


-- 7) 
-- a)
existeElLocker :: Integer -> [(Integer,(Bool,String))] -> Bool -- [(Identificacion, (Disponibilidad,Ubicacion))]
existeElLocker n []  = False
existeElLocker n ((x,(disp,ubi)):xs)  | n == x = disp
                                      | otherwise = existeElLocker n xs


-- b)
ubicacionDelLocker :: Integer -> [(Integer,(Bool,String))] -> String
ubicacionDelLocker  n []  = "nada"
ubicacionDelLocker n ((x,(disp,ubi)):xs) | n == x = ubi
                                         | otherwise = ubicacionDelLocker n xs


-- c)
estaDisponibleElLocker :: Integer -> [(Integer,(Bool,String))] -> Bool
estaDisponibleElLocker n []  = False
estaDisponibleElLocker n ((x,(disp,ubi)):xs)    | n == x && disp == True = True
                                                | otherwise = estaDisponibleElLocker n xs


-- d)
ocuparLoocker :: Integer -> [(Integer,(Bool,String))] -> [(Integer,(Bool,String))]
ocuparLoocker n []  = []
ocuparLoocker n ((x,(disp,ubi)):xs)     | n == x && disp == True = (n,(False,ubi)) : xs
                                        | otherwise = (x,(disp,ubi)) : ocuparLoocker n xs
