

def payRoll(hoursWorked, hourlyPay):
    if hoursWorked > 40:
        pay = hoursWorked * hourlyPay
        return pay
    else:
        pay = (40 * hourlyPay) + (hourlyPay * (hoursWorked-40))
        return pay

if __name__ == "__main__":
    userHoursWorked = int(input("Hours Worked: "))
    userHourlyPay = int(input("Hourly Pay: "))
    print(f"You have made {payRoll(userHoursWorked, userHourlyPay)} this week!")