grammar PsiCoder;

psicoder        :   global 'funcion_principal' principal 'fin_principal' global;
global          :   estructura
                |   funcion
                |   variableG
                |   ;
estructura      :   'estructura' ID estructuraAux1 'fin_estructura' global;
estructuraAux1  :   estructuraAux;
estructuraAux   :   ( ID | dt ) globalAux1 ';' estructuraAux
                |   ;
globalAux1      :   globalAux;
globalAux       :   ID globalAuxAux;
globalAuxAux    :   ',' globalAux
                |   ;
funcion         :   'funcion' ( tipoFuncionID = ID | tipoFuncion = dt ) idFuncion = ID '(' parametro1 ')' 'hacer' principal 'retornar' retornar;
parametro1      :   parametro
                |   ;
parametro       :   parametroAux;
parametroAux    :   ( tipoParametro = ID | dt ) idParametro = ID parametroAuxAux;
parametroAuxAux :   ',' parametroAux
                |   ;
retornar        :   ( expresion | expBool | ) ';' 'fin_funcion' global;
variableG       :   ( dt | ID ) comaAsignacion1 ';' global;
comaAsignacion1 :   comaAsignacion;
comaAsignacion2 :   comaAsignacion;
comaAsignacion  :   ID comaAsignacionAux;
comaAsignacionAux:  ',' comaAsignacion
                |   '=' ( expresion | expBool ) comaAsignacionAuxAux
                |   ;
comaAsignacionAuxAux:   ',' comaAsignacion
                |   ;
principal       :   idContenido
                |   leer
                |   imprimir
                |   variable
                |   si
                |   mientras
                |   hacer
                |   para
                |   seleccionar
                |   romper
                |   ;
idContenido     :   ID idAux;
idAux           :   ( '=' ( expID = expresion | expBID = expBool ) | '(' ( expID2 = expresion | expBID2 = expBool | ) comaExpresion1 ')' | '.' estructuraPunto1 '=' ( expID1 = expresion | expBID1 = expBool ) ) ';' principal;
comaExpresion1  :   comaExpresion;
comaExpresion2  :   ',' ( expresion | expBool ) comaExpresion
                |   ;
comaExpresion   :   ',' ( expresion | expBool ) comaExpresion
                |   ;
estructuraPunto1:   estructuraPunto;
estructuraPunto :   ID estructuraPuntoAux;
estructuraPuntoAux: '.' estructuraPunto
                |   ;
estructuraPunto2:   ID estructuraPuntoAux2;
estructuraPuntoAux2: '.' estructuraPunto2
                |   ;
variable        :   ( dt | ID ) comaAsignacion1 ';' principal;
leer            :   'leer' '(' ID ')' ';' principal;
imprimir        :   'imprimir' '(' ( expresion | expBool ) comaImpresion1 ')' ';' principal;
comaImpresion1  :   comaImpresion;
comaImpresion   :   ',' ( expresion | expBool ) comaImpresion
                |   ;
si              :   'si' '(' expBool ')' 'entonces' principal siNo1 'fin_si' principal;
siNo1           :   siNo;
siNo            :   'si_no' principal siNo
                |   ;
mientras        :   'mientras' '(' expBool ')' 'hacer' principal1 'fin_mientras' principal;
principal1      :   principal;
hacer           :   'hacer' principalHacer 'mientras' '(' expBool ')' ';' principal;
principalHacer  :   principal;
para            :   'para' '(' ( tipoInicializacion = 'entero' | ) idPara = ID '=' expInicializacion = expE ';' expBool ';' expIncremento = expE ')' 'hacer' principalPara 'fin_para' principal;
principalPara   :   principal;
seleccionar     :   'seleccionar' '(' ID ')' 'entre' seleccionarAux1 'fin_seleccionar' principal;
seleccionarAux1 :   seleccionarAux;
seleccionarAux  :   'defecto' ':' principal
                |   'caso' INT ':' principal seleccionarAuxAux;
seleccionarAuxAux:  seleccionarAux
                |   ;
romper          :   'romper' ';';
expresion       :   expE
                |   expR
                |   expS;
expE            :   '-' expE
                |   expE2;
expE2           :   expE2 '+' expE
                |   expE2 '-' expE
                |   expE3;
expE3           :   expE3 '*' expE
                |   expE3 '/' expE
                |   expE3 '%' expE
                |   expE4;
expE4           :   '(' expE ')'
                |   INT
                |   CAR
                |   ID expE5;
expE5           :   '(' ( expresion | expBool ) comaExpresion2 ')'
                |   '.' estructuraPunto2
                |   ;
expR            :   '-' expR
                |   expR2;
expR2           :   expR2 '+' expR
                |   expR2 '-' expR
                |   expR3;
expR3           :   expR3 '*' expR
                |   expR3 '/' expR
                |   expR3 '%' expR
                |   expR4;
expR4           :   '(' expR ')'
                |   INT
                |   CAR
                |   FLT
                |   ID expR5;
expR5           :   '(' ( expresion | expBool ) comaExpresion2 ')'
                |   '.' estructuraPunto2
                |   ;
expS            :   expS '+' expS2
                |   expS2;
expS2           :   STR
                |   ID;
expBool         :   expB;
expB            :   '!' expB
                |   expB2;
expB2           :   expB2 '||' expB
                |   expB3;
expB3           :   expB3 '&&' expB
                |   expB4;
expB4           :   expB4 '==' expB
                |   expB4 '!=' expB
                |   ( expE | expR ) '==' ( expE | expR )
                |   ( expE | expR ) '!=' ( expE | expR )
                |   expB5;
expB5           :   ( expE | expR ) '<' ( expE | expR )
                |   ( expE | expR ) '<=' ( expE | expR )
                |   ( expE | expR ) '>' ( expE | expR )
                |   ( expE | expR ) '>=' ( expE | expR )
                |   expB6;
expB6           :   '(' expB ')'
                |   ( 'falso' | 'verdadero' )
                |   ID expB7
                |   STR expB7;
expB7           :   '(' ( expresion | expB ) comaExpresion2 ')'
                |   '.' estructuraPunto2
                |   ;
dt              :   'booleano'
                |   'caracter'
                |   'entero'
                |   'real'
                |   'cadena';

STR :   '\"'(.)*?'\"';
CAR :   '\''( . | ' ' )'\'';
FLT :   [0-9]+'.'[0-9]+;
INT :   [0-9]+;
ID  :   ( [a-z] | [A-Z] )[a-zA-Z0-9]*;
WS  : 	[ \t\r\n]+ -> skip ; 			// skip spaces, tabs, newlines, \r (Windows)
COM :   ( '//' .*? [\n] | '/*' .*? '*/' ) -> skip;