package com.javier.pslib;

public class PrimeNumberChecker{
    public static int isPrime(int num){
        int result = 1;
        for(int i = 2; i < num; i++){
            if(num % i == 0){
                result = 0;
            }
        }
        return result;
    }
}
