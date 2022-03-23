package com.javier.exam_midterm;

public class Question2 {

    public static void main(String[] args) {
        //outputs: 1 and 2
        System.out.println( distance( "kitten", "mitten") );
        System.out.println( distance( "kitten", "mitter") );

    }

    public static String tail(String s){
        char[] char_array = s.toCharArray();
        char[] char_array_edited = new char[char_array.length - 1];
        for (int i = 1; i< char_array.length; i++){
            char_array_edited[i-1]=char_array[i];
        }
        return String.valueOf(char_array_edited);
    }

    public static int min(int a, int b, int c){
        int biggest = Math.min(a, b);
        return Math.min(biggest, c);
    }

    public static int distance( String a, String b) {
        if (a.length() == 0){
            return b.length();
        }
        else if (b.length()==0){
            return a.length();
        }
        else if (a.charAt(0) == b.charAt(0)){
            return distance(tail(a), tail(b));
        }
        else{
            return 1+min(distance(tail(a),b), distance(a, tail(b)), distance(tail(a),tail(b)));
        }
    }









}
