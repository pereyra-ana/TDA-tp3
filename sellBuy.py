def main(prices):
	print "Values {}".format(prices)

	if len(prices) < 2:
		print "no solution for less than two days\n"
		return

	if (prices[0] < prices[1]):
		buy = prices[0]
		buyIndex = 0
		auxBuyIndex = 0

	elif (prices[0] >= prices[1]):
		buy = prices[1]
		buyIndex = 1
		auxBuyIndex = 1

	sell = prices[1]
	sellIndex = 1
	auxBuy = buy

	for i in xrange(2, len(prices)):
		if (auxBuyIndex != buyIndex and auxBuyIndex < i and (prices[i] - auxBuy) > sell - buy):
			buy = auxBuy
			buyIndex = auxBuyIndex
			sell = prices[i]
			sellIndex = i

		elif (prices[i] - buy > sell - buy):
			sell = prices[i]
			sellIndex = i

		elif (prices[i] - buy < sell - buy):
			auxBuy = prices[i]
			auxBuyIndex = i

	if (sell - buy > 0):
		print "buy on day: {}, sell on day {} and gain ${}\n".format(buyIndex, sellIndex, sell - buy)
	else:
		print "no solution that makes u gain money :(\n"

main([2,3,5,7,8,22,4,56,1,100,2])
main([12,3,1,5,24,3])
main([3, 5, 1])
main([1])
main([12,1, 1,1,1,1,0])


# 4, 6, 7, 9, 1, 18, 20, 100
# 3, 5, 1

# 12,3,1,5,24,3
