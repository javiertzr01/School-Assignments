package com.javier.exam_midterm;

import java.util.ArrayList;

public class Question1 {

    public static void main(String[] args) {

        //output: 25
        int[] values = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        System.out.println(sumThreeAndSeven(values));

        // output: shnydys
        System.out.println( dropVowelsAndCase("SHINYDays")); //shnydys

        // output: [3, 0, 2, 2, 4, 6, 10]
        System.out.println(someSequence(6));
        // output: [3, 0, 2, 2]
        System.out.println(someSequence(3));
    }

    public static int sumThreeAndSeven( int[] values){
        //values have 1 - 100 elements
        //each element between 1-99
        //not sorted
        int sum = 0;
        for (int i: values){
            if( i%3==0 || i%7==0 ){
                sum += i;
            }
        }
        return sum;

    }

    public static String dropVowelsAndCase(String s){
        ArrayList<Character> char_array = new ArrayList<Character>();
        for (char c: s.toCharArray()){
            if (c == 'a' || c == 'e' || c =='i' || c =='o' || c =='u' || c == 'A' || c=='E' || c=='I' || c =='O' || c=='U'){
                continue;
            }
            else{
                char_array.add(Character.toLowerCase(c));
            }
        }
        char[] result = new char[char_array.size()];
        for (int i = 0; i<char_array.size(); i++){
            result[i] = char_array.get(i);
        }

        return String.valueOf(result);

    }

    public static ArrayList<Integer> someSequence(int n){
        ArrayList<Integer> initial = new ArrayList<>();
        initial.add(3);
        initial.add(0);
        initial.add(2);

        if (n==0){
            return new ArrayList<Integer>();
        }
        else if (n==1){
            ArrayList<Integer> one = new ArrayList<>();
            one.add(3);
            one.add(0);
            return one;
        }
        else if (n==2){
            ArrayList<Integer> two = new ArrayList<>();
            two.add(3);
            two.add(0);
            two.add(2);
            return two;
        }
        else if (n==3){
            ArrayList<Integer> three = new ArrayList<>();
            three.add(3);
            three.add(0);
            three.add(2);
            three.add(2);
            return three;
        }
        else{
            for (int i = 3; i<n+1; i++){
                Integer p_n1 = initial.get(i-1);
                Integer p_n2 = initial.get(i-2);
                initial.add(p_n1 + p_n2);
            }
            return initial;
        }
    }


}

