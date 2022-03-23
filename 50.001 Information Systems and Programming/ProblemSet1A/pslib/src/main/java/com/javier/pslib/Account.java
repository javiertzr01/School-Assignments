package com.javier.pslib;

// ATTENTION
// just edit this file
// TestAccount.java contains the test cases provided in the problem set
// Put in any import statements that you need


import java.util.Date;

public class Account {
    private int id = 0;
    private double balance = 0;
    private static double annualInterestRate = 0; //in percentage
    private Date dateCreated;
    Account(){

    }
    Account(int new_id, double new_balance){
        id = new_id;
        balance = new_balance;
    }


    //Accessor and mutator methods for id
    int getId(){
        return id;
    }
    void setId(int new_id){
        id = new_id;
        return;
    }

    //Accessor and mutator methods for balance
    double getBalance(){
        return balance;
    }
    void setBalance(double new_balance){
        balance = new_balance;
        return;
    }

    //Accessor and mutator methods for annualInterestRate
    static double getAnnualInterestRate(){
        return annualInterestRate;
    }
    static void setAnnualInterestRate(double new_annualInterestRate){
        annualInterestRate = new_annualInterestRate;
        return;
    }

    //Accessor method for dateCreated
    Date getDateCreated(){
        return dateCreated;
    }

    //Method for monthly interest rate
    double getMonthlyInterestRate(){
        return annualInterestRate/12;
    }

    //Method for monthly interest
    double getMonthlyInterest(){
        return (getMonthlyInterestRate()/100*balance);
    }

    //Method for withdraw
    void withdraw(double amt){
        balance -= amt;
        return;
    }

    //Method for deposit
    void deposit(double amt){
        balance += amt;
        return;
    }
}

// **HINT**
// The problem set says "assume all accounts have the same interest rate".
// What does that tell you about the variable(s) and/or method(s) relating to the interest rate?
