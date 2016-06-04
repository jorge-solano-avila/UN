import sys

language = 	{ 	'+': "+", '-': "-", '*': "*", '/': "/", '%': "%", '=': "=", '<': "<", '>': ">", '&': "&", '|': "|", '!': "!",
				'\'': "\'", '\"': "\"", ';': ";", ':': ":", ',': ",", '.': ".", '(': "(", ')': ")", ' ': " ", '\t': "\t" }

reservedWords = {	'funcion_principal': "funcion_principal", 'fin_principal': "fin_principal",
                    'booleano': "booleano", 'verdadero': "verdadero", 'falso': "falso", 'caracter': "caracter",
                    'entero': "entero", 'real': "real", 'cadena': "cadena", 'leer': "leer",
                    'imprimir': "imprimir", 'si': "si", 'entonces': "entonces", 'fin_si': "fin_si",
                    'si_no': "si_no", 'mientras': "mientras", 'hacer': "hacer", 'fin_mientras': "fin_mientras",
                    'para': "para", 'fin_para': "fin_para", 'seleccionar': "seleccionar", 'entre': "entre",
                    'caso': "caso", 'romper': "romper", 'defecto': "defecto", 'fin_seleccionar': "fin_seleccionar",
                    'estructura': "estructura", 'fin_estructura': "fin_estructura", 'funcion': "funcion",
                    'retornar': "retornar", 'fin_funcion': "fin_funcion"
                }

symbols = 	{	'+': "tk_mas", '-': "tk_menos", '*': "tk_mult", '/': "tk_div", '%': "tk_mod", '=': "tk_asig",
            	'<': "tk_menor", '>': "tk_mayor", '<=': "tk_menor_igual", '>=': "tk_mayor_igual", '==': "tk_igual",
            	'&&': "tk_y", '||': "tk_o", '!=': "tk_dif", '!': "tk_neg", ':': "tk_dosp", '\'': "tk_comilla_sen", 
            	'\"': "tk_comilla_dob", ';': "tk_pyc", ',': "tk_coma", '.': "tk_punto", '(': "tk_par_izq", ')': "tk_par_der"
            }

def isInt( c ):
	return len( c ) == 1 and ord( c ) >= 48 and ord( c ) <= 57

def isChar( c ):
	return len( c ) == 1 and ( ( ord( c ) >= 48 and ord( c ) <= 57 ) or ( ord( c ) >= 65 and ord( c ) <= 90 ) or ( ord( c ) >= 97 and ord( c ) <= 122 ) or ord( c ) == 95 )

def lexicalAnalyzer( lines ):
	result = []
	comment = False
	identificator = False
	real = False
	lenLines = len( lines )
	for i in xrange( lenLines ):
		lenLine = len( lines[i].strip( "\n" ).strip( "\r" ) )
		lexema = ""
		iterable = iter( xrange( lenLine ) )
		line, column, k = 0, 0, 0
		commentOne = False
		for j in iterable:
			###### Comments, div and mul ######

			# Comments and div
			if not comment and not commentOne and lines[i][j] == '/':
				if lenLine > j + 1 and lines[i][j + 1] == '*':
					comment = True
					[iterable.next() for x in xrange( 1 )]
					continue
				elif lenLine > j + 1 and lines[i][j + 1] == '/':
					commentOne = True
				else:
					#print "<%s,%d,%d>" % ( symbols[lines[i][j]], i + 1, j + 1 )
					result.append( tuple( [lines[i][j], i + 1, j + 1] ) )
					continue
			# End comment and mul
			elif lines[i][j] == '*':
				if comment and lenLine > j + 1 and lines[i][j + 1] == '/':
					comment = False
					[iterable.next() for x in xrange( 1 )]
					continue
				elif not comment and not commentOne:
					#print "<%s,%d,%d>" % ( symbols[lines[i][j]], i + 1, j + 1 )
					result.append( tuple( [lines[i][j], i + 1, j + 1] ) )
					continue

			###### Strings and characters ######

			# Strings
			if not comment  and not commentOne and lines[i][j] == '\"' and lenLine > j + 1:
				"""index = lines[i][j + 1:].find( '' )
				if index != -1:
					result.append( ">>> Error lexico(linea: %d, posicion: %d)" % ( i + 1, index + j + 2 )
					return"""
				index = lines[i][j + 1:].find( '\"' )
				if index != -1:
					lexema = lines[i][j:j + index + 2]
					lenLexema = len( lexema )
					for k in xrange( 1, lenLexema - 1 ):
						if not ( isChar( lexema[k] ) or lexema[k] == ' ' ):
							#print ">>> Error lexico(linea: %d, posicion: %d)" % ( i + 1, j + k + 1 )
							result.append( tuple( [">>> Error lexico", i + 1, j + k + 1] ) )
							return result
					#print "<%s,%s,%d,%d>" % ( "tk_cadena", lexema, i + 1, j + 1 )
					result.append( tuple( [lexema, i + 1, j + 1] ) )
					lexema = ""
					[iterable.next() for x in xrange( index + 1 )]
					continue

			# Characters
			elif not comment and not commentOne and lines[i][j] == '\'' and lenLine > j + 1:
				if lenLine > j + 2 and lines[i][j + 2] == '\'':
					lexema = lines[i][j:j + 3]
					if isChar( lexema[1] ) or lexema[1] == ' ':
						#print "<%s,%s,%d,%d>" % ( "tk_caracter", lexema, i + 1, j + 1 )
						result.append( tuple( [lexema, i + 1, j + 1] ) )
						lexema = ""
						[iterable.next() for x in xrange( 2 )]
						continue
					elif lexema[1] != '\'':
						#print ">>> Error lexico(linea: %d, posicion: %d)" % ( i + 1, j + 2 )
						result.append( tuple( [">>> Error lexico", i + 1, j + 2] ) )
						return result

			###### Symbols ######

			# Single symbol
			if not comment and not commentOne and symbols.has_key( lines[i][j] ) and ( ( lenLine > j + 1 and not symbols.has_key( str( lines[i][j] + lines[i][j + 1] ) ) ) or lenLine == j + 1 ):
				#print "<%s,%d,%d>" % ( symbols[lines[i][j]], i + 1, j + 1 )
				result.append( tuple( [lines[i][j], i + 1, j + 1] ) )
				continue
			# Double symbol
			elif not comment and not commentOne and lenLine > j + 1 and symbols.has_key( str( lines[i][j] + lines[i][j + 1] ) ):
				#print "<%s,%d,%d>" % ( symbols[str( lines[i][j] + lines[i][j + 1] )], i + 1, j + 1 )
				result.append( tuple( [str( lines[i][j] + lines[i][j + 1] ), i + 1, j + 1] ) )
				[iterable.next() for x in xrange( 1 )]
				continue

			###### Integers and floats ######

			if lexema == "":
				line = i + 1
				column = j + 1
			lexema += lines[i][j]
			lenLexema = len( lexema )
			if lexema == " ":
				lexema = ""
				continue
			if not symbols.has_key( lines[i][j] ) and not isChar( lines[i][j] ) and not isInt( lines[i][j] ) and not language.has_key( lines[i][j] ):
				#print ">>> Error lexico(linea: %d, posicion: %d)" % ( i + 1, j + 1 )
				result.append( tuple( [">>> Error lexico", i + 1, j + 1] ) )
				return result
			if not comment and not commentOne and isInt( lexema ):
				if lenLine > j + 1:
					for k in xrange( j + 1, lenLine ):
						if isInt( lines[i][k] ):
							lexema += lines[i][k]
							lenLexema = len( lexema )
						elif lines[i][k] == '.' or not isInt( lines[i][k] ):
							if not real and lines[i][k] == '.' and lenLine > k + 1 and isInt( lines[i][k + 1] ):
								real = True
								lexema += lines[i][k]
								lenLexema = len( lexema )
								continue
							elif isInt( lexema[lenLexema - 1] ):
								break
						else:
							break
				if not real:
					#print "<%s,%s,%d,%d>" % ( "tk_entero", lexema, line, column )
					result.append( tuple( [lexema, line, column] ) )
					if k + 1 == lenLine:
						if symbols.has_key( lines[i][k] ):
							[iterable.next() for x in xrange( k - j - 1 )]
						else:
							[iterable.next() for x in xrange( k - j )]
					else:
						[iterable.next() for x in xrange( k - j - 1 )]
				else:
					#print "<%s,%s,%d,%d>" % ( "tk_real", lexema, line, column )
					result.append( tuple( [lexema, line, column] ) )
					if k + 1 == lenLine:
						if symbols.has_key( lines[i][k] ):
							[iterable.next() for x in xrange( k - j - 1 )]
						else:
							[iterable.next() for x in xrange( k - j )]
					else:
						[iterable.next() for x in xrange( k - j - 1 )]
					real = False
				lexema = ""
				continue

			###### Reserved words and identificators ######
			
			if not comment and not commentOne:
				aux = lexema
				if lenLine == j + 1:
					#print "<%s,%s,%d,%d>" % ( "id", aux, line, column )
					result.append( tuple( ["id", aux, line, column] ) )
					lexema = ""
					identificator = False
					continue
				for k in xrange( j + 1, lenLine ):
					if isChar( lines[i][k] ):
						aux += lines[i][k]
					elif isChar( aux ):
						#print "<%s,%s,%d,%d>" % ( "id", aux, line, column )
						result.append( tuple( ["id", aux, line, column] ) )
						lexema = ""
						identificator = False
						break
					elif lines[i][k] == ' ' or symbols.has_key( lines[i][k] ):
						if not reservedWords.has_key( aux ):
							#print "<%s,%s,%d,%d>" % ( "id", aux, line, column )
							result.append( tuple( ["id", aux, line, column] ) )
							lexema = ""
							identificator = False
							[iterable.next() for x in xrange( k - j - 1 )]
							break
					if reservedWords.has_key( aux ):
						if lenLine == k + 1 or ( lenLine > k + 1 and lines[i][k + 1] != '_' and ( lines[i][k + 1] == ' ' or symbols.has_key( lines[i][k + 1] ) ) ):
							#print "<%s,%d,%d>" % ( reservedWords[aux], line, column )
							result.append( tuple( [reservedWords[aux], line, column] ) )
							aux = ""
							lexema = ""
							identificator = False
							[iterable.next() for x in xrange( k - j )]
							break
						elif lines[i][k + 1] == '_':
							l = 0
							for l in xrange( k + 1, lenLine ):
								aux += lines[i][l]
								if reservedWords.has_key( aux ) and ( lenLine == l + 1 or ( lenLine > l + 1 and ( lines[i][l + 1] == ' ' or symbols.has_key( lines[i][l + 1] ) ) ) ):
									#print "<%s,%d,%d>" % ( reservedWords[aux], line, column )
									result.append( tuple( [reservedWords[aux], line, column] ) )
									aux = ""
									lexema = ""
									identificator = False
									break
							if aux == "":
								[iterable.next() for x in xrange( l - j )]
								break
							else:
								identificator = True
								break
						break
					else:
						identificator = True
				if identificator:
					if lenLine == k + 1 or ( lenLine > k + 1 and ( lines[i][k + 1] == ' ' or symbols.has_key( lines[i][k + 1] ) ) ):
						#print "<%s,%s,%d,%d>" % ( "id", aux, line, column )
						result.append( tuple( ["id", aux, line, column] ) )
						lexema = ""
						identificator = False
						if k + 1 == lenLine:
							[iterable.next() for x in xrange( k - j )]
						else:
							[iterable.next() for x in xrange( k - j - 1 )]
				continue
		if i == lenLines - 1:
			result.append( tuple( ["EOF", i + 2, 1] ) )
	return result

lines = sys.stdin.readlines()
tokens = lexicalAnalyzer( lines )
lenTokens = len( tokens )
index = 0
token = tokens[index]
afterPrincipal = False

tipo_dato = { "entero": "entero", "booleano": "booleano", "caracter": "caracter", "cadena": "cadena" }

def expectedValues( array ):
	string = ""
	for i in xrange( len( array ) ):
		if i == len( array ) - 1:
			string += "\"%s\"." % array[i]
		else:
			string += "\"%s\", " % array[i]

	return string

def getNextToken():
	global index
	global token
	if lenTokens - 1 >= index + 1:
		index += 1
		token = tokens[index]
	else:
		token = tokens[lenTokens - 1]

def ID():
	return token[0] == "id"

def B2( dato ):
	global index
	global token
	if token[0] == "identificador":
		pred2 = ["=", ";", ","]
		getNextToken()
		if token[0] == ';':
			getNextToken()
			B()
		elif token[0] == ',':
			getNextToken()
			M()
		elif dato == "entero" or dato == "real":
			M()
		elif dato in tipo_dato:
			M4()
		else:
			print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba:" % ( token[1], token[2], token[0] ), expectedValues( pred2 )
			sys.exit()
	else:
		print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"identificador\"." % ( token[1], token[2], token[0] )
		sys.exit()

def B():
	pred = ["identificador", "fin_principal", "leer", "imprimir", "booleano", "caracter", "entero", "real", "cadena", "si", "fin_si", "mientras", "hacer", "fin_mientras", "para", "fin_para", "seleccionar", "caso", "romper", "defecto", "fin_seleccionar"]
	if token[0] == "identificador":
		getNextToken()
		B3()
	elif token[0] == "leer":
		getNextToken()
		if token[0] == '(':
			getNextToken()
			if token[0] == "identificador":
				getNextToken()
				if token[0] == ')'
					getNextToken()
					if token[0] == ';'
						getNextToken()
						B()
					else:
						print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \";\"" % ( token[1], token[2], token[0] )
						sys.exit()
				else:
					print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \")\"" % ( token[1], token[2], token[0] )
					sys.exit()
			else:
				print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"identificador\"" % ( token[1], token[2], token[0] )
				sys.exit()
		else:
			print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"(\"" % ( token[1], token[2], token[0] )
			sys.exit()
	elif token[0] == "imprimir":
		getNextToken()
		if token[0] == '(':
			getNextToken()
			V()
			if token[0] == ')'
				getNextToken()
				if token[0] == ';'
					getNextToken()
					B()
				else:
					print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \";\"" % ( token[1], token[2], token[0] )
					sys.exit()
			else:
				print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \")\"" % ( token[1], token[2], token[0] )
				sys.exit()
		else:
			print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"(\"" % ( token[1], token[2], token[0] )
			sys.exit()
	elif token[0] in tipo_dato:
		dat = token[0]
		getNextToken()
		B2( dat )
	elif token[0] == "si":
		getNextToken()
		if token[0] == '(':
			getNextToken()
			Q()
			if token[0] == ')':
				getNextToken()
				if token[0] == "entonces":
					getNextToken()
					B()
					#getNextToken()
					R()
					#getNextToken()
					if token[0] == "fin_si":
						getNextToken()
						B()
					else:
						print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"fin_si\"" % ( token[1], token[2], token[0] )
						sys.exit()
				else:
					print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"entonces\"" % ( token[1], token[2], token[0] )
					sys.exit()
			else:
				print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \")\"" % ( token[1], token[2], token[0] )
				sys.exit()
		else:
			print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"(\"" % ( token[1], token[2], token[0] )
			sys.exit()
	elif token[0] == "mientras":
		getNextToken()
		if token[0] == '(':
			getNextToken()
			Q()
			if token[0] == ')':
				getNextToken()
				if token[0] == "hacer":
					getNextToken()
					B()
					#getNextToken()
					if token[0] == "fin_mientras":
						getNextToken()
						B()
					else:
						print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"fin_mientras\"" % ( token[1], token[2], token[0] )
						sys.exit()
				else:
					print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"hacer\"" % ( token[1], token[2], token[0] )
					sys.exit()
			else:
				print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \")\"" % ( token[1], token[2], token[0] )
				sys.exit()
		else:
			print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"(\"" % ( token[1], token[2], token[0] )
			sys.exit()
	elif token[0] == "hacer":
		getNextToken()
		B()
		#getNextToken()
		if token[0] == "mientras"
			getNextToken()
			if token[0] == '(':
				getNextToken()
				Q()
				#getNextToken()
				if token[0] == ')':
					getNextToken()
					if token[0] == ';':
						getNextToken()
						B()
					else:
						print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \";\"" % ( token[1], token[2], token[0] )
						sys.exit()
				else:
					print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \")\"" % ( token[1], token[2], token[0] )
					sys.exit()
			else:
				print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"(\"" % ( token[1], token[2], token[0] )
				sys.exit()
		else:
			print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"mientras\"" % ( token[1], token[2], token[0] )
			sys.exit()
	elif token[0] == "para":
		getNextToken()
		if token[0] == '(':
			getNextToken()
			T()
			#getNextToken()
			if token[0] == ')'
				getNextToken()
				if token[0] == "hacer":
					getNextToken()
					B()
					#getNextToken()
					if token[0] == "fin_para":
						getNextToken()
						B()
					else:
						print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"fin_para\"" % ( token[1], token[2], token[0] )
						sys.exit()
				else:
					print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"hacer\"" % ( token[1], token[2], token[0] )
					sys.exit()
			else:
				print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \")\"" % ( token[1], token[2], token[0] )
				sys.exit()
		else:
			print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"(\"" % ( token[1], token[2], token[0] )
			sys.exit()
	elif token[0] == "seleccionar":
		getNextToken()
		if token[0] == '(':
			getNextToken()
			if token[0] == "identificador":
				getNextToken()
				if token[0] == ')'
					getNextToken()
					if token[0] == "entre":
						getNextToken()
						U()
						#getNextToken()
						if token[0] == "fin_seleccionar":
							getNextToken()
							B()
						else:
							print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"fin_seleccionar\"." % ( token[1], token[2], token[0] )
							sys.exit()
					else:
						print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"entre\"." % ( token[1], token[2], token[0] )
						sys.exit()
				else:
					print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \")\"." % ( token[1], token[2], token[0] )
					sys.exit()
			else:
				print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"identificador\"." % ( token[1], token[2], token[0] )
				sys.exit()
		else:
			print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"(\"." % ( token[1], token[2], token[0] )
			sys.exit()
	elif token[0] == "romper":
		getNextToken()
		if token[0] == ';':
			getNextToken()
			B()
		else:
			print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \";\"." % ( token[1], token[2], token[0] )
			sys.exit()
	else:
		print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba:" % ( token[1], token[2], token[0] ), expectedValues( pred )
		sys.exit()

def A4():
	pred = ["=", ";"]
	if token[0] == '=':
		getNextToken()
		J()
	elif token[0] == ';'
		pass
	else:
		print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba:" % ( token[1], token[2], token[0] ), expectedValues( pred )
		sys.exit()

def A3():
	pred = ["-", "!", ";", "(", "identificador", "valor_entero", "valor_real", "valor_caracter", "valor_cadena"]
	if token[0] == ';':
		getNextToken()
		if token[0] == "fin_funcion":
			getNextToken()
			A()
		else:
			print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"fin_funcion\"" % ( token[1], token[2], token[0] )
			sys.exit()
	elif token[0] in pred:
		getNextToken()
		if token[0] == ';':
			getNextToken()
			if token[0] == "fin_funcion":
				getNextToken()
				A()
			else:
				print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"fin_funcion\"" % ( token[1], token[2], token[0] )
				sys.exit()
	else:
		print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba:" % ( token[1], token[2], token[0] ), expectedValues( pred )
		sys.exit()

def A2():
	pred = [")", "identificador", "booleano", "caracter", "entero", "real", "cadena"]
	if token[0] == ')':
		getNextToken()
		if token[0] == "hacer":
			getNextToken()
			B()
			if token[0] == "retornar":
				A3()
			else:
				print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"retornar\"" % ( token[1], token[2], token[0] )
				sys.exit()
		else:
			print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"hacer\"" % ( token[1], token[2], token[0] )
			sys.exit()
	elif token[0] == "identificador" or token[0] in tipo_dato:
		getNextToken()
		if token[0] == ')':
			getNextToken()
			if token[0] == "hacer":
				getNextToken()
				B()
				if token[0] == "retornar":
					A3()
				else:
					print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"retornar\"" % ( token[1], token[2], token[0] )
					sys.exit()
			else:
				print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"hacer\"" % ( token[1], token[2], token[0] )
				sys.exit()
	else:
		print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba:" % ( token[1], token[2], token[0] ), expectedValues( pred )
		sys.exit()

def A():
	pred = ["funcion_principal", "booleano", "caracter", "entero", "real", "cadena", "estructura", "funcion"]
	if token[0] == "estructura":
		#getNextToken()
		if ID():
			#getNextToken()
			C()
			#getNextToken()
			if token[0] == "fin_estructura":
				#getNextToken()
				A()
			else:
				print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"fin_estructura\"." % ( token[1], token[2], token[0] )
				sys.exit()
		else:
			print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"identificador\"." % ( token[1], token[2], token[0] )
			sys.exit()
	elif token[0] == "funcion":
		D()
		#getNextToken()
		if ID():
			#getNextToken()
			if token[0] == '(':
				#getNextToken()
				A2()
			else:
				print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"(\"." % ( token[1], token[2], token[0] )
				sys.exit()
		else:
			print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"identificador\"." % ( token[1], token[2], token[0] )
			sys.exit()
	elif not afterPrincipal and token[0] == "funcion_principal":
		afterPrincipal = True
		#getNextToken()
		B()
		#getNextToken()
		if token[0] == "fin_principal":
			#getNextToken()
			A()
		else:
			print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"fin_principal\"." % ( token[1], token[2], token[0] )
			sys.exit()
	elif token[0] == "EOF":
		print "El analisis sintactico ha finalizado exitosamente."
		sys.exit()
	elif token[0] in pred:
		#getNextToken()
		F()
		A4()
		if token[0] == ';':
			A()
		else:
			print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \";\"." % ( token[1], token[2], token[0] )
			sys.exit()
	else:
		print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba:" % ( token[1], token[2], token[0] ), expectedValues( pred )
		sys.exit()

def G():
	pred = ["funcion_principal", "booleano", "caracter", "entero", "real", "cadena", "estructura", "funcion"]
	if token[0] == "funcion_principal":
		afterPrincipal = True
		#getNextToken()
		B()
		#getNextToken()
		if token[0] == "fin_principal":
			getNextToken()
			A()
		else:
			print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba: \"fin_principal\"." % ( token[1], token[2], token[0] )
			sys.exit()
	elif token[0] == "estructura" or token[0] == "funcion" or token[0] in tipo_dato:
		A()
	else:
		print "<%d:%d> Error sintactico: se encontro: \"%s\"; se esperaba:" % ( token[1], token[2], token[0] ), expectedValues( pred )
		return

isPrincipal = False 

for tokenI in tokens:
	if tokenI[0] == "funcion_principal":
		isPrincipal = True
		break

if isPrincipal:
	G()
else:
	print "Error sintactico: falta funcion_principal"