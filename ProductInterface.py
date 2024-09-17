from Product import Product
from Purchase import Purchase
from Sale import Sale

from Inventory import Inventory
from TextUtils import *

def listProducts(inventory:Inventory):
	clearScreen()
	printTitle(" Listing products ", BLUE, WHITE)

	products = inventory.getProducts()
	h = len(products) + 3
	drawBox(1,4,120,h,BLUE)
	gotoxy(2,5); printBrightBlue(f"{'Id':5} | {'Name':50} |    {'Buy price':10} |    {'Sell Price':10}")
	for i in range(len(products)):
		p:Product = products[i]
		gotoxy(2,6+i); printBrightBlue(f"{p.id:5} | {p.name:50} | R$ {p.buyPrice:10.2f} | R$ {p.sellPrice:10.2f}")
	gotoxy(1,4+h+1); input()

def addProduct(inventory:Inventory):
	clearScreen()
	printTitle(" Adding new product ", BLUE, WHITE)
	drawEditField("Name: ", line=4, boxColor=BLUE, textColor=WHITE)
	drawEditField("Buy Price (R$): ", line=7, boxColor=BLUE, textColor=WHITE)
	drawEditField("Sell Price (R$): ", line=10, boxColor=BLUE, textColor=WHITE)
	drawInfoBox()

	gotoxy(22,5);  name = input()
	gotoxy(22,8);  buyPrice = float(input())
	gotoxy(22,11); sellPrice = float(input())

	product = Product(0, name, buyPrice, sellPrice)
	inventory.addProduct(product)
	drawInfoBox("Product Sucessfully Added!", GREEN)
	input()

def updateProduct(inventory:Inventory):
	clearScreen()
	drawInfoBox()

	printTitle(" Updating product ", BLUE, WHITE)
	drawEditField("Product Id:", line=4, boxColor=BLUE, textColor=WHITE)
	drawEditField("Name: ", line=7, boxColor=BLUE, textColor=WHITE)
	drawEditField("Buy price: ", line=10, boxColor=BLUE, textColor=WHITE) 
	drawEditField("Sell price: ", line=13, boxColor=BLUE, textColor=WHITE)

	productExists = False

	gotoxy(22,5); id = int(input())
	selectedProduct = inventory.getProductById(id)
	if selectedProduct is None:
		drawInfoBox("ERROR: Product doesn't exist!",RED)
		input()
		return

	gotoxy(22,8);  printDarkGray(selectedProduct.name)
	gotoxy(22,11); printDarkGray(f"{selectedProduct.buyPrice:.2f}")
	gotoxy(22,14); printDarkGray(f"{selectedProduct.sellPrice:.2f}")

	gotoxy(22,8);  name = input()
	gotoxy(22,11); buyPrice = float(input())
	gotoxy(22,14); sellPrice = float(input())
	
	product = Product(id, name, buyPrice, sellPrice)
	inventory.updateProduct(product)

	drawInfoBox("SUCCESS: Product updated! Press ENTER to proceed...", GREEN)
	input()

def deleteProduct(inventory:Inventory):
	clearScreen()
	printTitle(" Deleting product ",BLUE, WHITE)
	drawEditField("Product Id:", line=4, boxColor=BLUE, textColor=WHITE)
	drawInfoBox()

	gotoxy(22,5); id = int(input())
	selectedProduct = inventory.getProductById(id)
	if selectedProduct is None:
		drawInfoBox("ERROR: Product doesn't exist!",RED)
		input()
		return

	inventory.deleteSalesByProduct(id)
	inventory.deletePurchasesByProduct(id)
	inventory.deleteProduct(id)
	
	drawInfoBox("SUCCESS: All Product data was removed! Press ENTER to proceed...", GREEN)
	input()

def printProductDetails(inventory:Inventory):
	clearScreen()
	printTitle(" Printing product details ", BLUE, WHITE)
	drawEditField("Product Id:", line=4, boxColor=BLUE, textColor=WHITE)
	drawInfoBox()

	gotoxy(22,5); id = int(input())
	selectedProduct = inventory.getProductById(id)
	if selectedProduct is None:
		drawInfoBox("ERROR: Product doesn't exist!",RED)
		input()
		return

	drawBox(1,7,120,19, BLUE)
	product:Product = selectedProduct

	gotoxy(2,8); printBlue("Name: ",end=""); print(product.name)
	gotoxy(32,8); printBlue("Buy Price: ",end=""); print(f"R$ {product.buyPrice:.2f}")
	gotoxy(62,8); printBlue("Sell Price: ",end=""); print(f"R$ {product.sellPrice:.2f}")
	gotoxy(92,8); printBlue("Stock: ",end=""); print(f"{inventory.getStockByProduct(id)}")
	#from here, as we are using loops, 
	# i'm gonna count and save the current printing line
	line = 9

	purchases = inventory.getPurchasesByProduct(id)
	gotoxy(2,line); printBlue("Purchases: ", end=""); print(len(purchases))
	gotoxy(32,line); printBlue("Total Purchased: ", end=""); print(inventory.getItensPurchasedByProduct(id))
	gotoxy(62,line); printBlue("Expenses: ", end=""); print(f"R$ {inventory.getTotalSpentByProduct(id):.2f}")
	line += 1
	for purchase in purchases:
		gotoxy(5,line)
		printLightGray(f"[{purchase.id}] {purchase.date}: {purchase.quantity} itens from {purchase.supplierId}([SupplierName]) with {purchase.discount:.2f}% discount")
		line+=1

	sales = inventory.getSalesByProduct(id)
	gotoxy(2,line); printBlue("Sales: ", end=""); print(len(sales))
	gotoxy(32,line); printBlue("Total Sold: ", end=""); print(inventory.getItensSoldByProduct(id))
	gotoxy(62,line); printBlue("Receipt: ", end=""); print(f"R$ {inventory.getTotalSoldByProduct(id):.2f}")
	line +=1
	for sale in sales:
		gotoxy(5,line)
		printLightGray(f"[{sale.id}] {sale.date}: {sale.quantity} items to {sale.clientId}([ClientName]) with {sale.discount:.2f}% discount")
		line += 1
	input()