import time
from termcolor import colored
import math
from data import *

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
	return amount / 10

def silver2gold(amount:int) -> float:
	return amount / 5

def copper2gold(amount:int) -> float:
	return silver2gold(copper2silver(amount))

def platinum2gold(amount:int) -> float:
	return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
	gold = 0
	gold += platinum2gold(personCash['platinum'])
	gold += personCash['gold']
	gold += silver2gold(personCash['silver'])
	gold += copper2gold(personCash['copper'])
	return gold

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
	return round(copper2gold(((people * COST_FOOD_HUMAN_COPPER_PER_DAY) + (horses * COST_FOOD_HORSE_COPPER_PER_DAY)) * JOURNEY_IN_DAYS), 2)

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
	test_lst = []
	for item in list:
		if item[key] == value:
			test_lst.append(item)

	return test_lst

def getAdventuringPeople(people:list) -> list:
	return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> list:
	return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
	return getFromListByKeyIs(friends, 'adventuring', True)

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
	return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
	return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
	return (horses * silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS) + (tents * (COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7)) )

##################### M04.D02.O7 #####################

def getItemsAsText(items: list) -> str:
	itemText = []
	for item in items:
		itemText.append(f"{item['amount']}{item['unit']} {item['name']}")
	return ', '.join(itemText)

def getItemsValueInGold(items: list) -> float:
	value = float()
	for item in items:
		amount = item['amount']
		price = item['price']['amount']

		if item['price']['type'] == 'copper':
			value += amount * copper2gold(price)
		elif item['price']['type'] == 'silver':
			value += amount * silver2gold(price)
		elif item['price']['type'] == 'platinum':
			value += amount * platinum2gold(price)
		else:
			value += price
	return value

##################### M04.D02.O8 #####################
def getCashInGoldFromPeople(people:list) -> float:
	priceGold = 0
	for person in people:
		if person['cash']['platinum'] != 0:
			priceGold += platinum2gold(person['cash']['platinum'])
		if person['cash']['gold'] != 0:
			priceGold += person['cash']['gold']
		if person['cash']['silver'] != 0:
			priceGold += silver2gold(person['cash']['silver'])
		if person['cash']['copper'] != 0:
			priceGold += copper2gold(person['cash']['copper'])

		return round(priceGold, 2)
##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
	

def getAdventuringInvestors(investors:list) -> list:
	pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
	pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
	pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
	pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
	pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:
	pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
	pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
	vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
	print(txt.format(*vars))

def print_title(name:str) -> None:
	print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
	nextStep(2)
	print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
	print('')
	time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
	text = yes if amount == 1 else no
	amount = single if amount == 1 else amount
	return '{} {}'.format(amount, text).lstrip()