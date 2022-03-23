package com.javier.problemset2A;

import java.util.Arrays;

public class Palindrome {
    public static boolean isPalindrome (char[] S) {
        char last_char = S[S.length - 1];
        char first_char = S[0];
        if (S.length == 2){
            if (first_char == last_char){
                return true;
            }
            else{
                return false;
            }
        }
        else if (S.length == 1){
            return true;
        }
        else{
            char[] new_S = Arrays.copyOfRange(S, 1, S.length-1);
            return isPalindrome(new_S);
        }
    }
}


/* ATTENTION
The method isPalindrome() returns true if the input string is a palindrome, and false otherwise.
It is NOT NECESSARY to do any System.out.println() of "abba is a palindrome" etc.
*/