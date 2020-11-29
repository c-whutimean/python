import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--type")					#  ("--type", choices=["annuity", "diff"], required=True, help= "type of payment)
parser.add_argument("--principal", type=float)	#  type=non_negative_float
parser.add_argument("--periods", type=float)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=float)

args = parser.parse_args()

if args.type == "diff" and args.principal and args.periods and args.interest:
	if args.principal < 0 or args.periods < 0 or args.interest < 0:
		print("Incorrect parameters")
		exit()
	i = 1
	overpay = 0
	interest = args.interest / (12 * 100)

	while i < args.periods + 1:
		total = math.ceil((args.principal / args.periods) + interest * (args.principal - ((args.principal * (i - 1)) / args.periods)))
		print(f'Month {i}: payment is {total}')
		overpay += total
		i += 1

	print("\nOverpayment = ", int(overpay - args.principal))

elif args.type == "annuity" and args.principal and args.periods and args.interest:
	if args.principal < 0 or args.periods < 0 or args.interest < 0:
		print("Incorrect parameters")
		exit()
	i = args.interest / (12 * 100)
	p = math.pow(1 + i, args.periods)
	annuity = math.ceil(args.principal * ((i * p) / (p - 1)))
	print(f'Your annuity payment = {annuity}!')
	print("Overpayment =", abs(int(args.principal - (annuity * args.periods))))

elif args.type == "annuity" and args.payment and args.periods and args.interest:
	if args.payment < 0 or args.periods < 0 or args.interest <  0:
		print("Incorrect parameters")
		exit()
	i = args.interest / (12 * 100)
	p = math.pow(1 + i, args.periods)
	denom = (i * p) / (p - 1)
	principal = int(args.payment / denom)
	print(f'Your loan principal = {principal}!')
	overpayment = math.ceil(principal - (args.payment * args.periods))
	print("Overpayment =", abs(int(overpayment)))

elif args.type == "annuity" and args.principal and args.payment and args.interest:
	if args.principal < 0 or args.payment < 0 or args.interest < 0:
		print("Incorrect parameters")
		exit()
	i = args.interest / (12 * 100)
	n = math.ceil(math.log(args.payment / (args.payment - i * args.principal), 1 + i))
	yrs = n // 12
	print(f'It will take {yrs} years to repay this loan!')

	overpayment = args.principal - (args.payment * (yrs * 12))
	print("Overpayment =", abs(int(overpayment)))
else:
	print("Incorrect parameters.")

