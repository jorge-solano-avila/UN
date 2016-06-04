import sys

language = 	{ 	'+': "+", '-': "-", '*': "*", '/': "/", '%': "%", '=': "=", '<': "<", '>': ">", '&': "&", '|': "|", '!': "!",
				'\'': "\'", '\"': "\"", ';': ";", ':': ":", ',': ",", '.': ".", '(': "(", ')': ")", ' ': " " }

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

def analyzer():
	comment = False
	identificator = False
	real = False
	for i in xrange( len( lines ) ):
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
					print "<%s,%d,%d>" % ( symbols[lines[i][j]], i + 1, j + 1 )
					continue
			# End comment and mul
			elif lines[i][j] == '*':
				if comment and lenLine > j + 1 and lines[i][j + 1] == '/':
					comment = False
					[iterable.next() for x in xrange( 1 )]
					continue
				elif not comment and not commentOne:
					print "<%s,%d,%d>" % ( symbols[lines[i][j]], i + 1, j + 1 )
					continue

			###### Strings and characters ######

			# Strings
			if not comment  and not commentOne and lines[i][j] == '\"' and lenLine > j + 1:
				"""index = lines[i][j + 1:].find( '' )
				if index != -1:
					print ">>> Error lexico(linea: %d, posicion: %d)" % ( i + 1, index + j + 2 )
					return"""
				index = lines[i][j + 1:].find( '\"' )
				if index != -1:
					lexema = lines[i][j:j + index + 2]
					lenLexema = len( lexema )
					for k in xrange( 1, lenLexema - 1 ):
						if not ( isChar( lexema[k] ) or lexema[k] == ' ' ):
							print ">>> Error lexico(linea: %d, posicion: %d)" % ( i + 1, j + k + 1 )
							return
					print "<%s,%s,%d,%d>" % ( "tk_cadena", lexema, i + 1, j + 1 )
					lexema = ""
					[iterable.next() for x in xrange( index + 1 )]
					continue

			# Characters
			elif not comment and not commentOne and lines[i][j] == '\'' and lenLine > j + 1:
				if lenLine > j + 2 and lines[i][j + 2] == '\'':
					lexema = lines[i][j:j + 3]
					if isChar( lexema[1] ) or lexema[1] == ' ':
						print "<%s,%s,%d,%d>" % ( "tk_caracter", lexema, i + 1, j + 1 )
						lexema = ""
						[iterable.next() for x in xrange( 2 )]
						continue
					elif lexema[1] != '\'':
						print ">>> Error lexico(linea: %d, posicion: %d)" % ( i + 1, j + 2 )
						return

			###### Symbols ######

			# Single symbol
			if not comment and not commentOne and symbols.has_key( lines[i][j] ) and ( ( lenLine > j + 1 and not symbols.has_key( str( lines[i][j] + lines[i][j + 1] ) ) ) or lenLine == j + 1 ):
				print "<%s,%d,%d>" % ( symbols[lines[i][j]], i + 1, j + 1 )
				continue
			# Double symbol
			elif not comment and not commentOne and lenLine > j + 1 and symbols.has_key( str( lines[i][j] + lines[i][j + 1] ) ):
				print "<%s,%d,%d>" % ( symbols[str( lines[i][j] + lines[i][j + 1] )], i + 1, j + 1 )
				[iterable.next() for x in xrange( 1 )]
				continue

			###### Integers and floats ######   ?????????????

			if lexema == "":
				line = i + 1
				column = j + 1
			lexema += lines[i][j]
			lenLexema = len( lexema )
			if lexema == " ":
				lexema = ""
				continue
			if not symbols.has_key( lines[i][j] ) and not isChar( lines[i][j] ) and not isInt( lines[i][j] ) and not language.has_key( lines[i][j] ):
				print ">>> Error lexico(linea: %d, posicion: %d)" % ( i + 1, j + 1 )
				return
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
					print "<%s,%s,%d,%d>" % ( "tk_entero", lexema, line, column )
					if k + 1 == lenLine:
						if symbols.has_key( lines[i][k] ):
							[iterable.next() for x in xrange( k - j - 1 )]
						else:
							[iterable.next() for x in xrange( k - j )]
					else:
						[iterable.next() for x in xrange( k - j - 1 )]
				else:
					print "<%s,%s,%d,%d>" % ( "tk_real", lexema, line, column )
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
					print "<%s,%s,%d,%d>" % ( "id", aux, line, column )
					lexema = ""
					identificator = False
					continue
				for k in xrange( j + 1, lenLine ):
					if isChar( lines[i][k] ):
						aux += lines[i][k]
					elif isChar( aux ):
						print "<%s,%s,%d,%d>" % ( "id", aux, line, column )
						lexema = ""
						identificator = False
						break
					elif lines[i][k] == ' ' or symbols.has_key( lines[i][k] ):
						if not reservedWords.has_key( aux ):
							print "<%s,%s,%d,%d>" % ( "id", aux, line, column )
							lexema = ""
							identificator = False
							[iterable.next() for x in xrange( k - j - 1 )]
							break
					if reservedWords.has_key( aux ):
						if lenLine == k + 1 or ( lenLine > k + 1 and lines[i][k + 1] != '_' and ( lines[i][k + 1] == ' ' or symbols.has_key( lines[i][k + 1] ) ) ):
							print "<%s,%d,%d>" % ( reservedWords[aux], line, column )
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
									print "<%s,%d,%d>" % ( reservedWords[aux], line, column )
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
						print "<%s,%s,%d,%d>" % ( "id", aux, line, column )
						lexema = ""
						identificator = False
						if k + 1 == lenLine:
							[iterable.next() for x in xrange( k - j )]
						else:
							[iterable.next() for x in xrange( k - j - 1 )]
				continue

lines = sys.stdin.readlines()
analyzer()