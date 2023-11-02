# Generated from Lua.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LuaParser import LuaParser
else:
    from LuaParser import LuaParser

# This class defines a complete generic visitor for a parse tree produced by LuaParser.

class LuaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LuaParser#chunk.
    def visitChunk(self, ctx:LuaParser.ChunkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#block.
    def visitBlock(self, ctx:LuaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#stat.
    def visitStat(self, ctx:LuaParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#attnamelist.
    def visitAttnamelist(self, ctx:LuaParser.AttnamelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#attrib.
    def visitAttrib(self, ctx:LuaParser.AttribContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#laststat.
    def visitLaststat(self, ctx:LuaParser.LaststatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#label.
    def visitLabel(self, ctx:LuaParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#funcname.
    def visitFuncname(self, ctx:LuaParser.FuncnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#varlist.
    def visitVarlist(self, ctx:LuaParser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#namelist.
    def visitNamelist(self, ctx:LuaParser.NamelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#explist.
    def visitExplist(self, ctx:LuaParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#exp.
    def visitExp(self, ctx:LuaParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#prefixexp.
    def visitPrefixexp(self, ctx:LuaParser.PrefixexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#functioncall.
    def visitFunctioncall(self, ctx:LuaParser.FunctioncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#varOrExp.
    def visitVarOrExp(self, ctx:LuaParser.VarOrExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#var.
    def visitVar(self, ctx:LuaParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#varSuffix.
    def visitVarSuffix(self, ctx:LuaParser.VarSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#nameAndArgs.
    def visitNameAndArgs(self, ctx:LuaParser.NameAndArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#args.
    def visitArgs(self, ctx:LuaParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#functiondef.
    def visitFunctiondef(self, ctx:LuaParser.FunctiondefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#funcbody.
    def visitFuncbody(self, ctx:LuaParser.FuncbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#parlist.
    def visitParlist(self, ctx:LuaParser.ParlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#tableconstructor.
    def visitTableconstructor(self, ctx:LuaParser.TableconstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#fieldlist.
    def visitFieldlist(self, ctx:LuaParser.FieldlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#field.
    def visitField(self, ctx:LuaParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#fieldsep.
    def visitFieldsep(self, ctx:LuaParser.FieldsepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorOr.
    def visitOperatorOr(self, ctx:LuaParser.OperatorOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorAnd.
    def visitOperatorAnd(self, ctx:LuaParser.OperatorAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorComparison.
    def visitOperatorComparison(self, ctx:LuaParser.OperatorComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorStrcat.
    def visitOperatorStrcat(self, ctx:LuaParser.OperatorStrcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorAddSub.
    def visitOperatorAddSub(self, ctx:LuaParser.OperatorAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorMulDivMod.
    def visitOperatorMulDivMod(self, ctx:LuaParser.OperatorMulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorBitwise.
    def visitOperatorBitwise(self, ctx:LuaParser.OperatorBitwiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorUnary.
    def visitOperatorUnary(self, ctx:LuaParser.OperatorUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorPower.
    def visitOperatorPower(self, ctx:LuaParser.OperatorPowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#number.
    def visitNumber(self, ctx:LuaParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#string.
    def visitString(self, ctx:LuaParser.StringContext):
        return self.visitChildren(ctx)



del LuaParser