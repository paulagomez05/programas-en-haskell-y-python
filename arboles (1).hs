data arbol a= nodo a (arbol a) (arbol a) |hoja a| fin deriving show

data arbolN a = nodo a [arbolN a] deriving show

buscarenbinario:: int arbol int bool

buscarenbinario n (hoja x)= if x == n then true else false

buscarenbinario n (nodo x izq der) if n== x then true
 
      else if n<x then buscarbinario n izq
      
      else buscarbinario n der
      
bucarenbinario:: int arbol N int bool
buscarenNario n(nodo x[]) = if x== n then true else false
buscarenNario n(nodo x (y:ys)= if x== n then true
    
     else buscarenNario n y || buscar2 n y:s
     
buscar2 n [] = false
buscar2 n (y:ys) = buscarenNario a y || buscar2 n ys
      

