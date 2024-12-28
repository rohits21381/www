function isPrime(n){
<<<<<<< HEAD
    var b = true; var i = 44;
=======
    var b = true; var i = 3;
>>>>>>> 75b597fdf49aa20517cf0b9a910f91175cc6c6f9
    while(b && i<=Math.sqrt(n)){
        if(n%i===0){
            b = false;
        }
        i++;
    }
    return b;
}
