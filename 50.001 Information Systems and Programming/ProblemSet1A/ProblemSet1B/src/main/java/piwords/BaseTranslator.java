package piwords;

import java.util.Arrays;

public class BaseTranslator {
    /**
     * Converts an array where the ith digit corresponds to (1 / baseA)^(i + 1)
     * digits[i], return an array output of size precisionB where the ith digit
     * corresponds to (1 / baseB)^(i + 1) * output[i].
     * 
     * Stated in another way, digits is the fractional part of a number
     * expressed in baseA with the most significant digit first. The output is
     * the same number expressed in baseB with the most significant digit first.
     * 
     * To implement, logically, you're repeatedly multiplying the number by
     * baseB and chopping off the most significant digit at each iteration:
     * 
     * for (i < precisionB) {
     *   1. Keep a carry, initialize to 0.
     *   2. From RIGHT to LEFT
     *   	a. x = multiply the jth digit by baseB and add the carry
     *          b. the new jth digit is x % baseA
     *          c. carry = x / baseA
     *   3. output[i] = carry
     * }
     * If digits[j] < 0 or digits[j] >= baseA for any j, return null
     * If baseA < 2, baseB < 2, or precisionB < 1, return null
     * 
     * @param digits The input array to translate. This array is not mutated.
     * @param baseA The base that the input array is expressed in.
     * @param baseB The base to translate into.
     * @param precisionB The number of digits of precision the output should
     *                   have.
     * @return An array of size precisionB expressing digits in baseB.
     */
    public static int[] convertBase(int[] digits, int baseA,
                                    int baseB, int precisionB) {
        // TODO: Implement (Problem c)
        if(precisionB < 1){
            return null;
        }
        int[] output = new int[precisionB];
        int[] new_digits;
        if (baseA < 2 || baseB < 2){
            return null;
        }
        for(int i = 0; i<digits.length;i++){
            if (digits[i]<0){
                return null;
            }
            if (digits[i]/baseA >= 1){
                return null;
            }
        }
        new_digits = Arrays.copyOf(digits, precisionB);
        for (int i=0; i < precisionB; i++) {
            int carry = 0;
            for (int j = new_digits.length - 1; j > -1; j--) {
                int x = new_digits[j] * baseB + carry;
                new_digits[j] = x % baseA;
                carry = x / baseA;
                if (new_digits[j] < 0 || new_digits[j] >= baseA) {
                    return null;
                }
            }
            output[i] = carry;
        }
        if (output.length != precisionB){
            return null;
        }

        return output;
    }
}
