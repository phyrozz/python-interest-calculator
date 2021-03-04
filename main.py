from fractions import Fraction


def choose_interest_type():
    interest_type = input("Please choose what type of interest you'd wish to calculate:\n1 - Simple Interest"
                          "\n2 - Compound Interest\n3 - Exit: ")

    if interest_type == "1":
        calculate_simple()
    elif interest_type == "2":
        calculate_compound()
    elif interest_type == "3":
        return 0
    else:
        print("Invalid input. Please try again.")
        choose_interest_type()


def calculate_simple():
    # print("Calculating simple interest involves three important variables:\nPrincipal - the initial amount of "
    #       "money that you have deposited in a bank or any other investing establishments.\nInterest Rate - is "
    #       "the percentage amount of money that you'll earn from your principal, which is a part of the interest "
    #       "the bank gives you.\nTime - the amount of time the principal has stayed in your account, which "
    #       "will be crucial in finding the amount of interest the bank will give you.\n\nAll of these three "
    #       "variables form the formula for the simple interest, which is expressed as such:\n\n"
    #       "I = Prt\n\nWhere:\nI = Interest\nP = Principal\nr = Interest Rate\nt = Interest Period (must be in "
    #       "year unit)\n\n")
    p = input("\nEnter your principal (P): ")
    r = input("Enter interest rate (in decimal form) (r): ")
    t = input("Enter interest period (in years) (t): ")

    t.split('/')
    i = float(p) * float(r) * float(Fraction(t))
    a = i + float(p)
    print("\nYour simple interest is %.2f" % i)
    print("The future value of your principal is %.2f" % a)

    prompt_continue()


def calculate_compound():
    p = input("\nEnter your principal (P): ")
    r = input("Enter your annual interest rate (in decimal form) (r): ")
    n = input("Enter the number of compounding periods per year (n): ")
    t = input("Enter the number of years (t): ")

    n.split('/')
    t.split('/')
    a = float(p) * (1 + (float(r) / float(Fraction(n)))) ** (float(Fraction(n)) * float(Fraction(t)))
    i = a - float(p)
    print("\nYour compound interest is %.2f" % i)
    print("Your compounded amount is %.2f" % a)

    prompt_continue()


def prompt_continue():
    confirm = input("\nDo you want to continue calculating?\ny - Yes\nn - No: ")
    if confirm == 'y':
        choose_interest_type()
    elif confirm == 'n':
        return 0
    else:
        print("Invalid input. Please try again.")
        prompt_continue()


if __name__ == "__main__":
    choose_interest_type()
