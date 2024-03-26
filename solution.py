def solution(A, D):
    acc_balance = 0
    no_monthly_transactions = {}
    value_monthly_transactons = {}
    
    # Loop through transactions to calculate balance
    for index, transaction in enumerate(A):
        acc_balance += transaction

        if transaction < 0:
            # Extract month from date string
            date = D[index].split('-')
            month = date[1]
            
            # Track frequency and value of card payments per month
            if month in no_monthly_transactions:
                no_monthly_transactions[month] += 1
            else:
                no_monthly_transactions[month] = 1

            if month in value_monthly_transactons:
                value_monthly_transactons[month] += transaction
            else:
                value_monthly_transactons[month] = transaction
                
    # Calculate number of months excluded from fee
    excluded_months = 0
    for key, value in no_monthly_transactions.items():
        if value >= 3 and value_monthly_transactons[key] <= -100:
            excluded_months += 1

    # Calculate total fees charged in the year
    monthly_fee = 5
    months_fee_charged = 12 - excluded_months
    total_fee = monthly_fee * months_fee_charged

    # Calculate final balance
    final_balance = acc_balance - total_fee
    print(final_balance)
    return final_balance

# Test cases
solution([100, 100, 100, -10], ["2020-01-01", "2020-12-22", "2020-12-03", "2020-12-29"])
solution([180, -50, -25, -25], ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"])
solution([1, -1, 0, -105, 1], ["2020-12-31", "2020-04-04", "2020-04-04", "2020-04-14", "2020-07-12"])
solution([100, 100, -10, -20, -30], ["2020-01-01", "2020-01-01", "2020-02-11", "2020-02-11", "2020-02-08"])
solution([-60, 60, -40, -20], ["2020-10-01", "2020-02-02", "2020-10-10", "2020-10-30"])
