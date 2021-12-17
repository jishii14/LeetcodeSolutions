import java.io.*;
import java.util.*;

// PROBLEM STATEMENT: Find length of longest substring without repeating characters
public class Solution {
    public int lengthOfLongestSubstring(String s) {        
        int max = 1;
        char sChars[] = s.toCharArray();
        if (sChars.length == 0)
            return 0;
        for (int i = 0; i < sChars.length - 1; i++) {
            int arr[] = new int[256];
            for(int k = 0; k < 256; k++) {
                arr[k] = 0;
            }
            arr[sChars[i]] = 1;
            
            int j;
            for (j = i + 1; j < sChars.length; j++) {
                arr[sChars[j]] += 1;
                
                // First check whether next character already in sequence
                if (arr[sChars[j]] > 1) {
                    if (j - i > max) {
                        System.out.println("i " + i + " j " + j);
                        max = j - i;
                    }
                    break; // Slide window over
                }
            }
            if (j == sChars.length) {
                arr[sChars[i]] -= 1; // Slide
                if (j - i > max) {
                    System.out.println("i " + i + " j " + j);
                    max = j - i;
                }
            }
        }
        
        return max;
    }
}