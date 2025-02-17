#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 13:32:54 2022

@author: guljahan
"""

Filename: main.cpp

#include <iostream>
using namespace std;
    
int main() {
    int a = 10, b = 20; 
  
    int maximum = max(a, b); 
  
    cout << "maximum is " << maximum; 
    return 0; 
}
int max(int a, int b) 
{ 
    if (a > b) 
    return a; 
    else
    return b; 
} 


###########################


     Please follow the code and sample output along with screenshot

 

please note assignment short cut code. You can use alternate also:

 

result+= nextNumber; is equals to the statement result = result + nextNumber; lowerLimit+=1; is equals to the statement

 

 lowerLimit = lowerLimit + 1;

 

Code:



public class NumbersLoop {
    private int lowerLimit;
    private int upperLimit;

    // this method set the lower limit value
    public void setLowerLimit(int l) {
        lowerLimit = l;
    }

    // this method set the lower limit value
    public void setUpperLimit(int u) {
        upperLimit = u;
    }

    /*
    * Here nextNumber and result are local variables.
    * First we assign the lowerLimit value to the nextNumber and then increment by 1 each time.
    * will store this addition in to result variable */

    public int addLowerAllTheWayToUpper(){
        int nextNumber =lowerLimit;
        int result=0;

        for (int i = lowerLimit; i <= upperLimit ; i++) {

            //System.out.println("Number came : " +lowerLimit);
            //System.out.println("now result of ("+result+"+"+nextNumber+") = " +(result+nextNumber));
            result+= nextNumber;

            lowerLimit+=1;
            //System.out.println("Incrementing lowerLimit value by 1 :" +lowerLimit);
            nextNumber++;

        }
        return  result;

    }

    public static void main(String[] args) {
        NumbersLoop numbersLoop = new NumbersLoop();
        numbersLoop.setLowerLimit(1);;
        numbersLoop.setUpperLimit(10);
        System.out.println("Result of addLowerAllTheWayToUpper is: " +numbersLoop.addLowerAllTheWayToUpper());
    }
}
 

 

public class NumbersLoop {

   private int lowerLimit;

   private int upperLimit;

 

   // this method set the lower limit value    public void setLowerLimit(int l) {        lowerLimit = l;

    }  

 

  // this method set the lower limit value

   public void setUpperLimit(int u) {        upperLimit = u;

    }  

 

  /*    

* Here nextNumber and result are local variables.   

 * First we assign the lowerLimit value to the nextNumber and then increment by 1 each time.   

 * will store this addition in to result variable */    

 

public int addLowerAllTheWayToUpper(){        int nextNumber =lowerLimit;       

 int result=0;       

 

 for (int i = lowerLimit; i <= upperLimit ; i++) {

           //System.out.println("Number came : " +lowerLimit);   

         //System.out.println("now result of ("+result+"+"+nextNumber+") = " +(result+nextNumber));  

          result+= nextNumber;    

 

        lowerLimit+=1;    

        //System.out.println("Incrementing lowerLimit value by 1 :" +lowerLimit);   

         nextNumber++;   

 

     }        return  result;

 

   }   

 

 public static void main(String[] args) {  

      NumbersLoop numbersLoop = new NumbersLoop();   

     numbersLoop.setLowerLimit(1);;

        numbersLoop.setUpperLimit(10);       

 

 System.out.println("Result of addLowerAllTheWayToUpper is: "

 +numbersLoop.addLowerAllTheWayToUpper());    } }

