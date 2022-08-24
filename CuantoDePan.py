# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	print("Bienvenido a la panaderia de la abuela")
	print("Cuantos panes llevo?")
	npanes = float(input())
	resultado_productoa = npanes*4
	print(" =$",resultado_productoa)
	ndonas = float(input())
	resultado_productob = ndonas*10
	print(" =$",resultado_productob)
	nempanadas = float(input())
	resultado_productoc = nempanadas*12
	print(" =$",resultado_productoc)
	resultado_suma = resultado_productoa+resultado_productob+resultado_productoc
	print("total a pagar=",resultado_suma)

