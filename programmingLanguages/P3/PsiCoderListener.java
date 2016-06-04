// Generated from PsiCoder.g4 by ANTLR 4.5.3
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PsiCoderParser}.
 */
public interface PsiCoderListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#psicoder}.
	 * @param ctx the parse tree
	 */
	void enterPsicoder(PsiCoderParser.PsicoderContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#psicoder}.
	 * @param ctx the parse tree
	 */
	void exitPsicoder(PsiCoderParser.PsicoderContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#global}.
	 * @param ctx the parse tree
	 */
	void enterGlobal(PsiCoderParser.GlobalContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#global}.
	 * @param ctx the parse tree
	 */
	void exitGlobal(PsiCoderParser.GlobalContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#estructura}.
	 * @param ctx the parse tree
	 */
	void enterEstructura(PsiCoderParser.EstructuraContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#estructura}.
	 * @param ctx the parse tree
	 */
	void exitEstructura(PsiCoderParser.EstructuraContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#estructuraAux1}.
	 * @param ctx the parse tree
	 */
	void enterEstructuraAux1(PsiCoderParser.EstructuraAux1Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#estructuraAux1}.
	 * @param ctx the parse tree
	 */
	void exitEstructuraAux1(PsiCoderParser.EstructuraAux1Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#estructuraAux}.
	 * @param ctx the parse tree
	 */
	void enterEstructuraAux(PsiCoderParser.EstructuraAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#estructuraAux}.
	 * @param ctx the parse tree
	 */
	void exitEstructuraAux(PsiCoderParser.EstructuraAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#globalAux1}.
	 * @param ctx the parse tree
	 */
	void enterGlobalAux1(PsiCoderParser.GlobalAux1Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#globalAux1}.
	 * @param ctx the parse tree
	 */
	void exitGlobalAux1(PsiCoderParser.GlobalAux1Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#globalAux}.
	 * @param ctx the parse tree
	 */
	void enterGlobalAux(PsiCoderParser.GlobalAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#globalAux}.
	 * @param ctx the parse tree
	 */
	void exitGlobalAux(PsiCoderParser.GlobalAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#globalAuxAux}.
	 * @param ctx the parse tree
	 */
	void enterGlobalAuxAux(PsiCoderParser.GlobalAuxAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#globalAuxAux}.
	 * @param ctx the parse tree
	 */
	void exitGlobalAuxAux(PsiCoderParser.GlobalAuxAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#funcion}.
	 * @param ctx the parse tree
	 */
	void enterFuncion(PsiCoderParser.FuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#funcion}.
	 * @param ctx the parse tree
	 */
	void exitFuncion(PsiCoderParser.FuncionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#parametro1}.
	 * @param ctx the parse tree
	 */
	void enterParametro1(PsiCoderParser.Parametro1Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#parametro1}.
	 * @param ctx the parse tree
	 */
	void exitParametro1(PsiCoderParser.Parametro1Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#parametro}.
	 * @param ctx the parse tree
	 */
	void enterParametro(PsiCoderParser.ParametroContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#parametro}.
	 * @param ctx the parse tree
	 */
	void exitParametro(PsiCoderParser.ParametroContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#parametroAux}.
	 * @param ctx the parse tree
	 */
	void enterParametroAux(PsiCoderParser.ParametroAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#parametroAux}.
	 * @param ctx the parse tree
	 */
	void exitParametroAux(PsiCoderParser.ParametroAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#parametroAuxAux}.
	 * @param ctx the parse tree
	 */
	void enterParametroAuxAux(PsiCoderParser.ParametroAuxAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#parametroAuxAux}.
	 * @param ctx the parse tree
	 */
	void exitParametroAuxAux(PsiCoderParser.ParametroAuxAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#retornar}.
	 * @param ctx the parse tree
	 */
	void enterRetornar(PsiCoderParser.RetornarContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#retornar}.
	 * @param ctx the parse tree
	 */
	void exitRetornar(PsiCoderParser.RetornarContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#variableG}.
	 * @param ctx the parse tree
	 */
	void enterVariableG(PsiCoderParser.VariableGContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#variableG}.
	 * @param ctx the parse tree
	 */
	void exitVariableG(PsiCoderParser.VariableGContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#comaAsignacion1}.
	 * @param ctx the parse tree
	 */
	void enterComaAsignacion1(PsiCoderParser.ComaAsignacion1Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#comaAsignacion1}.
	 * @param ctx the parse tree
	 */
	void exitComaAsignacion1(PsiCoderParser.ComaAsignacion1Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#comaAsignacion2}.
	 * @param ctx the parse tree
	 */
	void enterComaAsignacion2(PsiCoderParser.ComaAsignacion2Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#comaAsignacion2}.
	 * @param ctx the parse tree
	 */
	void exitComaAsignacion2(PsiCoderParser.ComaAsignacion2Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#comaAsignacion}.
	 * @param ctx the parse tree
	 */
	void enterComaAsignacion(PsiCoderParser.ComaAsignacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#comaAsignacion}.
	 * @param ctx the parse tree
	 */
	void exitComaAsignacion(PsiCoderParser.ComaAsignacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#comaAsignacionAux}.
	 * @param ctx the parse tree
	 */
	void enterComaAsignacionAux(PsiCoderParser.ComaAsignacionAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#comaAsignacionAux}.
	 * @param ctx the parse tree
	 */
	void exitComaAsignacionAux(PsiCoderParser.ComaAsignacionAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#comaAsignacionAuxAux}.
	 * @param ctx the parse tree
	 */
	void enterComaAsignacionAuxAux(PsiCoderParser.ComaAsignacionAuxAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#comaAsignacionAuxAux}.
	 * @param ctx the parse tree
	 */
	void exitComaAsignacionAuxAux(PsiCoderParser.ComaAsignacionAuxAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#principal}.
	 * @param ctx the parse tree
	 */
	void enterPrincipal(PsiCoderParser.PrincipalContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#principal}.
	 * @param ctx the parse tree
	 */
	void exitPrincipal(PsiCoderParser.PrincipalContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#idContenido}.
	 * @param ctx the parse tree
	 */
	void enterIdContenido(PsiCoderParser.IdContenidoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#idContenido}.
	 * @param ctx the parse tree
	 */
	void exitIdContenido(PsiCoderParser.IdContenidoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#idAux}.
	 * @param ctx the parse tree
	 */
	void enterIdAux(PsiCoderParser.IdAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#idAux}.
	 * @param ctx the parse tree
	 */
	void exitIdAux(PsiCoderParser.IdAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#comaExpresion1}.
	 * @param ctx the parse tree
	 */
	void enterComaExpresion1(PsiCoderParser.ComaExpresion1Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#comaExpresion1}.
	 * @param ctx the parse tree
	 */
	void exitComaExpresion1(PsiCoderParser.ComaExpresion1Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#comaExpresion2}.
	 * @param ctx the parse tree
	 */
	void enterComaExpresion2(PsiCoderParser.ComaExpresion2Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#comaExpresion2}.
	 * @param ctx the parse tree
	 */
	void exitComaExpresion2(PsiCoderParser.ComaExpresion2Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#comaExpresion}.
	 * @param ctx the parse tree
	 */
	void enterComaExpresion(PsiCoderParser.ComaExpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#comaExpresion}.
	 * @param ctx the parse tree
	 */
	void exitComaExpresion(PsiCoderParser.ComaExpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#estructuraPunto1}.
	 * @param ctx the parse tree
	 */
	void enterEstructuraPunto1(PsiCoderParser.EstructuraPunto1Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#estructuraPunto1}.
	 * @param ctx the parse tree
	 */
	void exitEstructuraPunto1(PsiCoderParser.EstructuraPunto1Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#estructuraPunto}.
	 * @param ctx the parse tree
	 */
	void enterEstructuraPunto(PsiCoderParser.EstructuraPuntoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#estructuraPunto}.
	 * @param ctx the parse tree
	 */
	void exitEstructuraPunto(PsiCoderParser.EstructuraPuntoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#estructuraPuntoAux}.
	 * @param ctx the parse tree
	 */
	void enterEstructuraPuntoAux(PsiCoderParser.EstructuraPuntoAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#estructuraPuntoAux}.
	 * @param ctx the parse tree
	 */
	void exitEstructuraPuntoAux(PsiCoderParser.EstructuraPuntoAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#estructuraPunto2}.
	 * @param ctx the parse tree
	 */
	void enterEstructuraPunto2(PsiCoderParser.EstructuraPunto2Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#estructuraPunto2}.
	 * @param ctx the parse tree
	 */
	void exitEstructuraPunto2(PsiCoderParser.EstructuraPunto2Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#estructuraPuntoAux2}.
	 * @param ctx the parse tree
	 */
	void enterEstructuraPuntoAux2(PsiCoderParser.EstructuraPuntoAux2Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#estructuraPuntoAux2}.
	 * @param ctx the parse tree
	 */
	void exitEstructuraPuntoAux2(PsiCoderParser.EstructuraPuntoAux2Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(PsiCoderParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(PsiCoderParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#leer}.
	 * @param ctx the parse tree
	 */
	void enterLeer(PsiCoderParser.LeerContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#leer}.
	 * @param ctx the parse tree
	 */
	void exitLeer(PsiCoderParser.LeerContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#imprimir}.
	 * @param ctx the parse tree
	 */
	void enterImprimir(PsiCoderParser.ImprimirContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#imprimir}.
	 * @param ctx the parse tree
	 */
	void exitImprimir(PsiCoderParser.ImprimirContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#comaImpresion1}.
	 * @param ctx the parse tree
	 */
	void enterComaImpresion1(PsiCoderParser.ComaImpresion1Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#comaImpresion1}.
	 * @param ctx the parse tree
	 */
	void exitComaImpresion1(PsiCoderParser.ComaImpresion1Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#comaImpresion}.
	 * @param ctx the parse tree
	 */
	void enterComaImpresion(PsiCoderParser.ComaImpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#comaImpresion}.
	 * @param ctx the parse tree
	 */
	void exitComaImpresion(PsiCoderParser.ComaImpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#si}.
	 * @param ctx the parse tree
	 */
	void enterSi(PsiCoderParser.SiContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#si}.
	 * @param ctx the parse tree
	 */
	void exitSi(PsiCoderParser.SiContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#siNo1}.
	 * @param ctx the parse tree
	 */
	void enterSiNo1(PsiCoderParser.SiNo1Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#siNo1}.
	 * @param ctx the parse tree
	 */
	void exitSiNo1(PsiCoderParser.SiNo1Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#siNo}.
	 * @param ctx the parse tree
	 */
	void enterSiNo(PsiCoderParser.SiNoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#siNo}.
	 * @param ctx the parse tree
	 */
	void exitSiNo(PsiCoderParser.SiNoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#mientras}.
	 * @param ctx the parse tree
	 */
	void enterMientras(PsiCoderParser.MientrasContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#mientras}.
	 * @param ctx the parse tree
	 */
	void exitMientras(PsiCoderParser.MientrasContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#principal1}.
	 * @param ctx the parse tree
	 */
	void enterPrincipal1(PsiCoderParser.Principal1Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#principal1}.
	 * @param ctx the parse tree
	 */
	void exitPrincipal1(PsiCoderParser.Principal1Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#hacer}.
	 * @param ctx the parse tree
	 */
	void enterHacer(PsiCoderParser.HacerContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#hacer}.
	 * @param ctx the parse tree
	 */
	void exitHacer(PsiCoderParser.HacerContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#principalHacer}.
	 * @param ctx the parse tree
	 */
	void enterPrincipalHacer(PsiCoderParser.PrincipalHacerContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#principalHacer}.
	 * @param ctx the parse tree
	 */
	void exitPrincipalHacer(PsiCoderParser.PrincipalHacerContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#para}.
	 * @param ctx the parse tree
	 */
	void enterPara(PsiCoderParser.ParaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#para}.
	 * @param ctx the parse tree
	 */
	void exitPara(PsiCoderParser.ParaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#principalPara}.
	 * @param ctx the parse tree
	 */
	void enterPrincipalPara(PsiCoderParser.PrincipalParaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#principalPara}.
	 * @param ctx the parse tree
	 */
	void exitPrincipalPara(PsiCoderParser.PrincipalParaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#seleccionar}.
	 * @param ctx the parse tree
	 */
	void enterSeleccionar(PsiCoderParser.SeleccionarContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#seleccionar}.
	 * @param ctx the parse tree
	 */
	void exitSeleccionar(PsiCoderParser.SeleccionarContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#seleccionarAux1}.
	 * @param ctx the parse tree
	 */
	void enterSeleccionarAux1(PsiCoderParser.SeleccionarAux1Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#seleccionarAux1}.
	 * @param ctx the parse tree
	 */
	void exitSeleccionarAux1(PsiCoderParser.SeleccionarAux1Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#seleccionarAux}.
	 * @param ctx the parse tree
	 */
	void enterSeleccionarAux(PsiCoderParser.SeleccionarAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#seleccionarAux}.
	 * @param ctx the parse tree
	 */
	void exitSeleccionarAux(PsiCoderParser.SeleccionarAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#seleccionarAuxAux}.
	 * @param ctx the parse tree
	 */
	void enterSeleccionarAuxAux(PsiCoderParser.SeleccionarAuxAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#seleccionarAuxAux}.
	 * @param ctx the parse tree
	 */
	void exitSeleccionarAuxAux(PsiCoderParser.SeleccionarAuxAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#romper}.
	 * @param ctx the parse tree
	 */
	void enterRomper(PsiCoderParser.RomperContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#romper}.
	 * @param ctx the parse tree
	 */
	void exitRomper(PsiCoderParser.RomperContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterExpresion(PsiCoderParser.ExpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitExpresion(PsiCoderParser.ExpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expE}.
	 * @param ctx the parse tree
	 */
	void enterExpE(PsiCoderParser.ExpEContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expE}.
	 * @param ctx the parse tree
	 */
	void exitExpE(PsiCoderParser.ExpEContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expE2}.
	 * @param ctx the parse tree
	 */
	void enterExpE2(PsiCoderParser.ExpE2Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expE2}.
	 * @param ctx the parse tree
	 */
	void exitExpE2(PsiCoderParser.ExpE2Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expE3}.
	 * @param ctx the parse tree
	 */
	void enterExpE3(PsiCoderParser.ExpE3Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expE3}.
	 * @param ctx the parse tree
	 */
	void exitExpE3(PsiCoderParser.ExpE3Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expE4}.
	 * @param ctx the parse tree
	 */
	void enterExpE4(PsiCoderParser.ExpE4Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expE4}.
	 * @param ctx the parse tree
	 */
	void exitExpE4(PsiCoderParser.ExpE4Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expE5}.
	 * @param ctx the parse tree
	 */
	void enterExpE5(PsiCoderParser.ExpE5Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expE5}.
	 * @param ctx the parse tree
	 */
	void exitExpE5(PsiCoderParser.ExpE5Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expR}.
	 * @param ctx the parse tree
	 */
	void enterExpR(PsiCoderParser.ExpRContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expR}.
	 * @param ctx the parse tree
	 */
	void exitExpR(PsiCoderParser.ExpRContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expR2}.
	 * @param ctx the parse tree
	 */
	void enterExpR2(PsiCoderParser.ExpR2Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expR2}.
	 * @param ctx the parse tree
	 */
	void exitExpR2(PsiCoderParser.ExpR2Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expR3}.
	 * @param ctx the parse tree
	 */
	void enterExpR3(PsiCoderParser.ExpR3Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expR3}.
	 * @param ctx the parse tree
	 */
	void exitExpR3(PsiCoderParser.ExpR3Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expR4}.
	 * @param ctx the parse tree
	 */
	void enterExpR4(PsiCoderParser.ExpR4Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expR4}.
	 * @param ctx the parse tree
	 */
	void exitExpR4(PsiCoderParser.ExpR4Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expR5}.
	 * @param ctx the parse tree
	 */
	void enterExpR5(PsiCoderParser.ExpR5Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expR5}.
	 * @param ctx the parse tree
	 */
	void exitExpR5(PsiCoderParser.ExpR5Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expS}.
	 * @param ctx the parse tree
	 */
	void enterExpS(PsiCoderParser.ExpSContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expS}.
	 * @param ctx the parse tree
	 */
	void exitExpS(PsiCoderParser.ExpSContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expS2}.
	 * @param ctx the parse tree
	 */
	void enterExpS2(PsiCoderParser.ExpS2Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expS2}.
	 * @param ctx the parse tree
	 */
	void exitExpS2(PsiCoderParser.ExpS2Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expBool}.
	 * @param ctx the parse tree
	 */
	void enterExpBool(PsiCoderParser.ExpBoolContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expBool}.
	 * @param ctx the parse tree
	 */
	void exitExpBool(PsiCoderParser.ExpBoolContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expB}.
	 * @param ctx the parse tree
	 */
	void enterExpB(PsiCoderParser.ExpBContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expB}.
	 * @param ctx the parse tree
	 */
	void exitExpB(PsiCoderParser.ExpBContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expB2}.
	 * @param ctx the parse tree
	 */
	void enterExpB2(PsiCoderParser.ExpB2Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expB2}.
	 * @param ctx the parse tree
	 */
	void exitExpB2(PsiCoderParser.ExpB2Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expB3}.
	 * @param ctx the parse tree
	 */
	void enterExpB3(PsiCoderParser.ExpB3Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expB3}.
	 * @param ctx the parse tree
	 */
	void exitExpB3(PsiCoderParser.ExpB3Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expB4}.
	 * @param ctx the parse tree
	 */
	void enterExpB4(PsiCoderParser.ExpB4Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expB4}.
	 * @param ctx the parse tree
	 */
	void exitExpB4(PsiCoderParser.ExpB4Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expB5}.
	 * @param ctx the parse tree
	 */
	void enterExpB5(PsiCoderParser.ExpB5Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expB5}.
	 * @param ctx the parse tree
	 */
	void exitExpB5(PsiCoderParser.ExpB5Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expB6}.
	 * @param ctx the parse tree
	 */
	void enterExpB6(PsiCoderParser.ExpB6Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expB6}.
	 * @param ctx the parse tree
	 */
	void exitExpB6(PsiCoderParser.ExpB6Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expB7}.
	 * @param ctx the parse tree
	 */
	void enterExpB7(PsiCoderParser.ExpB7Context ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expB7}.
	 * @param ctx the parse tree
	 */
	void exitExpB7(PsiCoderParser.ExpB7Context ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#dt}.
	 * @param ctx the parse tree
	 */
	void enterDt(PsiCoderParser.DtContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#dt}.
	 * @param ctx the parse tree
	 */
	void exitDt(PsiCoderParser.DtContext ctx);
}