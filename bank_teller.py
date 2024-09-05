# STEP 1 Initializing savings and checking account values.
# Creates two variables, one named checking_balance and the other savings_balance. Assign them both the value of zero. Use these as your starting bank balances.

#STEP 1 Int variables checking balance and savings balance
checking_balance = 0
savings_balance = 0

#STEP 2 Create a function to check the Balance

#Step 1 Check account_type and return the respective balance.
#Define a function named check_balance() that accepts three parameters account_type, checking_balance and savings_balance. account_type represents a string which can either be "savings" or "checking". checking_balance and savings_balancerepresent the respective number balances.

#Step 2 Check account_type and return the respective balance
#Within the function named check_balance(), create an if...elif...else statement. Within each if statement return the customers balance based on the type of account_type they requested.

#Step 3 Assigning the savings_balance
#Within the first if statement use an equal operator to check whether account_type is the same as "savings". If that is true, set the new variable balance to the value of savings_balance.

#Step 4 Assigning the checking_balance
#Within the second elif statement use an equal operator to check whether account_type is the same as "checking". If that is true, set the variable balance to the value of checking_balance.

#Step 5 Return an error statement if there are no matching account_type
#Within the else statement, return an error statement given that there were no matches for the previous if...elif statements. Within the else statement, return "Unsuccessful, please enter \"checking\" or \"savings\""

#Step 6 Create a balance statement
#Under the if statements, create a new variable called balance_statement and assign it a value that consists of strings and variables. Concatenate the variables account_type and balance into the account statement. Remember to cast balance to a string using str() in the statement. The statement should be: "Your account_type balance is balance".

#Step 7 Return balance statement
#Under the balance_statement assignment, close out the check_balance() function by adding a return statement that returns the balance_statement variable.

#STEP 2 Create a function to check balance 

def check_balance(account_type, checking_balance, savings_balance):
  if account_type == "savings":
    balance = savings_balance
  elif account_type == "checking":
    balance = checking_balance
  else: 
    print("Unsuccessful, please enter \"checking\" or \"savings\"")
  balance_statement = "Your " + account_type + " balance is: " + str(balance)
  return balance_statement 

#STEP 3 Calling and Printing the check_balance() function for Checking Account
#Now that you have completed the check_balance() function, call it inside a print() function. Call the check_balance() function with these arguments; "checking", checking_balance and savings_balance. The latter two were already initialized at the start of the project. Your checking balance should print.

#Step 3
print(check_balance("checking", checking_balance, savings_balance))   

#STEP 4  Calling and Printing the check_balance() function for Savings Account
# On the next line, inside a print() function call the check_balance() function with these arguments; "savings", checking_balance and savings_balance. Your savings balance should print.

#Step 4
print(check_balance("savings", checking_balance, savings_balance))

#STEP 5 Create a function to make a deposit

#Step 1 Define a funcion
#Define a function named make_deposit() that accepts four parameters account_type, amount, checking_balance and savings_balance. The amount represents the amount to be deposited.

#Step 2 Initialize deposit_status variable
#Inside the deposit function, start by creating a variable named deposit_status and assign it to a an empty string

#Step 3 Ensure deposit is greater than 0
#Write an if statement that checks whether the passed in amount is greater than 0. Step 5 will continue putting code inside this if statement if amount is greater than 0.

#Step 4 Error if amount is less than 0
#Write a corresponding else statement if the if statement fails. Within that else, assign the variable deposit_status to the string value "unsuccessful, please enter an amount greater than 0"

#Step 5 Checking account_type
#Within the if statement that ensures that the amount is greater than 0, write inner if...elif...else statements. Within each if statement add the passed in amount to the customers balance based on the type of account_type they requested and also set deposit_status to "successful" or an error message.

#Step 6 Deposit to Savings account
#Within the first nested if statement check whether account_type is equivalent to "savings". Then within this if statement on the next line add amount to savings_balance using the += assignment operator. On the next line assign the string value "successful" to the variable deposit_status.

#Step 7 Deposit to Checking account
#Within the next nested elif statement check whether account_type is equivalent to "checking". Then within this elif statement on the next line add amount to checking_balance using the += assignment operator. On the next line assign the string value "successful" to the variable deposit_status.

#Step 8 Assign an error statement if there are not matching account type
#Within the next nested else statement, assign the string value "Unsuccessful, please enter \"checking\" or \"savings\"" to the variable deposit_status.

#Step 9 Create a deposit statement
#Outside of all the if statements but still in the function, compose a statement composing of strings and variables used in this function. Then assign it to the new deposit_statement variable. The statement should be: "Deposit of amount to your account_type account was deposit_status".

#Step 10 Print deposit statement
#On the next line, write a print statement with the deposit_statement as an argument. This will print the deposit statement anytime the deposit function is called.

#Step 11 return savings_balance and checking_balance
#On the next line return both the savings_balance and checking_balance. This will conclude the make_deposit() function.

#Step 1 Define function make deposit 

def make_deposit(account_type, amount, checking_balance, savings_balance):
  #Step 2 Int deposit status variable 
  deposit_statuts = ""
  #Step 3 Ensure deposit in greater than 0
  if amount > 0:
    #Step 5 Checking account type 
    #Step 6 deposit to savings account
    if account_type == "savings":
      savings_balance += amount
      deposit_statuts = "successful"
    #Step 7 Deposit checking account
    elif account_type == "checking":
      checking_balance += amount
      deposit_statuts = "successful"
      #Step 4 Error if amount is less than 0
    else:
      deposit_statuts = "Unsuccessful, please enter \"checking\" or \"savings\""    
    #Step 8 Error statement if there are no matching account type
  else: 
    deposit_statuts = "unsuccessful, please enter an amount greater than 0"   
  #Step 9 Deposit statement
  deposit_statement = "Deposit of " + str(amount) + " dollars to your " + account_type + " account was " + deposit_statuts + "."
  #Step 10 Print deposit statement
  print(deposit_statement)
  #Step 11 Return saving balance and checking balance
  return savings_balance, checking_balance   

#STEP 6 Call deposit function and make a savings deposit 
savings_balance, checking_balance = make_deposit("savings", 10, checking_balance, savings_balance)

#STEP 7 Print savings balance call after making a savings deposit
print(check_balance("savings", checking_balance, savings_balance))

#STEP 8 Call deposit function and make a checking deposit
savings_balance, checking_balance = make_deposit("checking", 200, checking_balance, savings_balance)

#STEP 9 Print checking balance call after makinga checking deposit
print(check_balance("checking", checking_balance, savings_balance))



#STEP 10 Create a function to make withdrawal

#Step 1. Define function
#Define a function named make_withdrawal() that accepts four parameters account_type, amount, checking_balance and savings_balance. The amount represents the withdrawal amount.

#Step 2. Initialize withdrawal_status variable
#Inside the withdrawal function, start by creating a variable named withdrawal_status and assign it to an empty string.

#Step 3. Initialize an error message
#On the next line create a variable named fail and assign it to the value "unsuccessful, please enter amount less than balance"

#Step 4. Checking account_type
#Write if...elif...else statements. Within each if statement check whether the account_type is equivalent to savings_balance or checking_balance. If neither, throw an error in the else statement.

#Step 5. Withdrawal from savings account
#The first if statement should check whether account_type is equivalent to "savings".

#Step 6. Ensure withdrawal is less than savings account
#Then write an inner if...else that checks if the withdrawal amount is greater than the savings balance. If the amount is indeed greater, in the else statement, assign withdrawal_status to the variable fail.

#Step 7. Subtract amount from savings account
#Within the inner if statement, subtract amount from the savings_balance using the -= assignment operator. On the next line assign the string value "successful" to the variable withdrawal_status.

#Step 8. Withdrawal from checking account
#The next elif statement should check whether account_type is equivalent to "checking".

#Step 9. Ensure withdrawal is less than checking account
#Then write an inner if...else that checks if the withdrawal amount is greater than the checking balance. If the amount is indeed greater, in the else statement, assign withdrawal_status to the variable fail.

#Step 10. Subtract amount from checking account
#Within the inner if statement, subtract amount from the checking_balance using the -= assignment operator. On the next line assign the string value "successful" to the variable withdrawal_status.

#Step 11. Assign an error statement if there are no matching account_type
#Within the last else statement, assign the string value "unsuccessful, please enter \"checking\" or \"savings\"" to the variable withdrawal_status.

#Step 12. Create a withdrawal statement
#Outside of all the if statements but still in the function, create a statement composing of strings and variables used in this function. Then assign it to the new withdrawal_statement variable. The withdrawal statement should be: "Withdrawal of amount from your account_type was withdrawal_status".

#Step 13. Print withdrawal statement
#On the next line, write a print statement with the withdrawal_statement as an argument. This will print the withdrawal statement anytime the deposit function is called.

#Step 14. Return savings_balance and checking_balance
#On the next line return both the savings_balance and checking_balance. This will conclude the make_withdrawal() function.

#Step 1 Define function

def make_withdrawal(account_type, amount, checking_balance, savings_balance):
  
  #Step 2 Int withdrawal_status
  withdrawal_status = ""
  
  #Step 3 Int error message
  fail = "unsuccessful, please enter amount less than balance"
  
  #Step 4 Checking account type
  #Step 5 Withdrawal from savings account
  if account_type == "savings":
  #Step 6 Ensure withdrawal is less than savings account
    if amount <= savings_balance:
  #Step 7 Substract amount from savings account
      savings_balance -= amount 
      withdrawal_status = "successful"
    else:
      withdrawal_status = fail 
  #Step 8 Withdrawal from checking account    
  elif account_type == "checking":
  #Step 9 Ensure withdrawal is less than checking account  
    if amount <= checking_balance:
  #Step 10 Substract amount from checking account    
      checking_balance -= amount
      withdrawal_status = "successful"      
    else: 
      withdrawal_status = fail
  else:
  #Step 11 asign an error statement if there are no matching account type  
    withdrawal_status = "unsuccessful, please enter \"checking\" or \"savings\"" 
  
  #Step 12 Create a withdrawal statement
  withdrawal_statement = "Withdrawal of " + str(amount) +  " dollars from your " +  account_type +  " was " + withdrawal_status + "."
  print(withdrawal_statement)
  return savings_balance, checking_balance

#STEP 11 Call withdrawal function and make a savings withdrawal
savings_balance, checking_balance = make_withdrawal("savings", 11, checking_balance, savings_balance)

#STEP 12 Print savings balance call, after making a savings withdrawal
print(check_balance("savings", checking_balance, savings_balance))

#STEP 13 Call withdrawal function and make a checking withdrawal
savings_balance, checking_balance = make_withdrawal("checking", 170, checking_balance, savings_balance)

#STEp 14 Print checking balance call, after making a checking withdrawal
print(check_balance("checking", checking_balance, savings_balance))

#STEP 15 Create a function to make transfer between accounts

#Step 1. Define function
#Define a function named acc_transfer() that accepts five parameters acc_from, acc_to, amount, checking_balance and savings_balance.

#step 2. Initialize transaction_status variable
#Inside the transfer function, start by creating a variable named transaction_status and assign it to a an empty string.

#Step 3. Initialize an error message
#On the next line create a variable named trans_error and assign it to the value "unsuccessful, please enter amount less than "

#Step 4. Account Transfer
#Write if...elif...else statements. The if statement will check if the transfer is from savings to checking account. The elif statement will check if the transfer is from checking to savings account. If neither, throw an error in the else statement.

#Step 5. Ensure transfer is less than savings account
#Within the first if statement, write an inner if...else that checks if the transfer amount is greater than the savings balance. If the amount is indeed greater, in the else statement, assign transaction_status to the variable trans_error + str(savings_balance).

#Step 6. Transfer amount from savings to checking account
#Within the inner if statement, subtract amount from the savings_balance using the -= assignment operator. On the next line, add amount to the checking_balance using the += assignment operator. Then on the next line assign the string value "successful" to the variable transaction_status.

#Step 7. Ensure transfer is less than checking account
#Within the following elif statement, write an inner if...else that checks if the transfer amount is greater than the checking balance. If the amount is indeed greater, in the else statement, assign transaction_status to the variable trans_error + str(checking_balance).

#Step 8. Transfer amount from checking to savings account
#Within the inner if statement, subtract amount from the checking_balance using the -= assignment operator. On the next line, add amount to the savings_balance using the += assignment operator. Then on the next line assign the string value "successful" to the variable transaction_status.

#Step 9. Assign an error statement if there are no matching account_type
#Within the last else statement, assign the string value "unsuccessful, please enter \"checking\" or \"savings\"" to the variable transaction_status.

#Step 10. Create a transfer statement
#Outside of all the if statements but still in the function, compose a statement composing of strings and variables used in this function. Then assign it to the new transaction_statement variable. The transfer statement should be; "Transfer of amount from your cc_from to your acc_to account was transaction_status".

#Step 11. Print transfer statement
#On the next line, write a print statement with the transaction_statement as an argument. This will print the transfer statement anytime the transfer function is called.

#Step 12. Return savings_balance and checking_balance
#On the next line return both the savings_balance and checking_balance. This will conclude the acc_transfer() function.

#Step 1 Define function

def acc_transfer(acc_from, acc_to, amount, checking_balance, savings_balance):
  
#Step 2 Int transaction variable
  transaction_status = ""

#Step 3 Int error message
  trans_error = "unsuccessful, please enter amount less than "    

#Step 4 Account Transfer
  if acc_from == "savings" and acc_to == "checking": 
    #Step 5 Ensure transfer is less than savings account
    if amount <= savings_balance:
      #Step 6 Transfer amount from savings to checking account
       savings_balance -= amount
       checking_balance += amount
       transaction_status = "successful" 
    else :
      #Step 6
      transaction_status = trans_error + str(savings_balance)
    
  elif acc_from == "checking" and acc_to == "savings":
      #Step 7 Ensure transfer is less than checking account
    if amount <= checking_balance:
      #Step 8 Transfer amount from checking to savings accoun
        checking_balance -= amount
        savings_balance += amount
        transaction_status = "successful"
    else :
      #Step 7
      transaction_status = trans_error + str(checking_balance)
        
    
  else :
      #Step 9  Assign an error statement if there are no matching account_type 
      transaction_status = "unsuccessful, please enter \"checking\" or \"savings\""
  
  #Step 10 Create a transfer statement
  
  transaction_statement = "Transfer of " + str(amount) + " dollars from your " + acc_from + " to your " + acc_to + " account was " + transaction_status + "."     
  # Step 11 Print transfer statement
  print(transaction_statement)
  
  #Step 12 Return savings balance and checking balance
  return savings_balance, checking_balance     

#STEP 16 Call transfer function and make a checking to savings transfer

savings_balance, checking_balance = acc_transfer("checking", "savings", 40, checking_balance, savings_balance)

#STEP 17 Print checking balance after making a checking to savings transfer

print(check_balance("checking", checking_balance, savings_balance))

#STEP 18 Print savings balance after making a checking to savings transfer

print(check_balance("savings", checking_balance, savings_balance))

#STEP 19 Call transfer function and make a savings to checking transfer

savings_balance, checking_balance = acc_transfer("savings", "checking", 5, checking_balance, savings_balance)

#STEP 20 Print checking balance after making a savings to checking transfer

print(check_balance("checking", checking_balance, savings_balance))

#STEP 21 Print saving balance after making a savings to checking transfer

print(check_balance("savings", checking_balance, savings_balance))

