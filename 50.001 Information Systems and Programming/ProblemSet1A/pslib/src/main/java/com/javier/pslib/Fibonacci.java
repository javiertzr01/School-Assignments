package com.javier.pslib;

public class Fibonacci{

    public static String fibonacci( int n ){
        int a = 0;
        int b = 1;
        int nextint;
        String fin = Integer.toString(a) + "," + Integer.toString(b);

        for(int i = 2; i < n; i++){
            nextint = a + b;
            fin += "," + Integer.toString(nextint);
            a = b;
            b = nextint;
        }
        return fin;
    }

}
