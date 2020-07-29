
def credit_card_payoff(n,balance,annualInterestRate):
    '''
    Monthly payment to payoff a credit card in a given number of months,
    using geometric series.
    
    Parameters
    ----------
    n : int
        number of months.
    balance : floar or int
        initial balance.
    annualInterestRate : float
        annual interest rate in decimals.

    Returns
    -------
    int or float
        monthly payment.

    '''
    a=1+(annualInterestRate/12) 
    monthlyPayment=(balance*(1-a)*(a**n))/(a-a**(n+1))  
    return print('Monthly payment: '+str(monthlyPayment))

def cc_minimum_payoff(n,balance,annualInterestRate):
    '''    
    Minimum monthly payment to payfoff a credit card in a given 
    number of months using bisection search.
    
    Parameters
    ----------
    n : int
        number of months.
    balance : floar or int
        initial balance.
    annualInterestRate : float
        annual interest rate in decimals.

    Returns
    -------
    int or float
        monthly payment.

    '''
    original_balance=balance
    monthlyPayment=0    
    while True:
        for month in range(n):
            balance=(balance-monthlyPayment)*(1+(annualInterestRate/12))
        if balance >=0:
            for month in range(n):
                balance=original_balance
            monthlyPayment+=10
        else:
            break
          
    return print('Lowest Payment: '+str(monthlyPayment))    
   

def mortgage_payoff(n,loan,annualInterestRate):
    '''
    Monthly payment to payoff a mortgage using geometric series.
    Parameters
    ----------
    n : int
        number of months.
    loan : floar or int
        loan amount.
    annualInterestRate : float
        annual interest rate in decimals.

    Returns
    -------
    int or float
        monthly payment.

    '''
    a=1+(annualInterestRate/12) 
    monthlyPayment=(loan*(1-a)*(a**n))/(1-a**(n))
    return print('Monthly payment: '+str(monthlyPayment))
