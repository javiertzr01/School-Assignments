package com.javier.problemset2A;


import java.util.ArrayList;

public class Permutation {
    private final String in;
    private ArrayList<String> a = new ArrayList<String>();
    // additional attribute if needed
    private char[] in_char_arr;


    Permutation(final String str){
        in = str;
        // additional initialization if needed
        in_char_arr = str.toCharArray();
    }

    public void permute(){
        // produce the permuted sequence of 'in' and store in 'a', recursively
        for (char c: in_char_arr){
            String left_str = new String();
            String right_str = new String();
            left_str += c;
            for (char x: in_char_arr){
                if (x != c) {
                    right_str += x;
                }
            }

            if(right_str.length() > 1) {
                Permutation next = new Permutation(right_str);
                next.permute();
                for (String s : next.getA()) {
                    a.add(left_str + s);
                }
            }
            else{
                a.add(left_str+right_str);
            }
        }
    }

    public ArrayList<String> getA(){
        return a;
    }
}
