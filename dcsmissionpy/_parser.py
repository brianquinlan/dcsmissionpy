from typing import Any, Dict

import antlr4

from antlr4.tree.Trees import Trees
from dcsmissionpy._lua_parser.LuaLexer import LuaLexer
from dcsmissionpy._lua_parser.LuaVisitor import LuaVisitor
from dcsmissionpy._lua_parser.LuaParser import LuaParser


class VisitTable(LuaVisitor):
    def __init__(self, namespace: Dict):
        super().__init__()
        self._namespace = namespace
        self._table = {}
        self._list_count = 1

    def visitField(self, ctx: LuaParser.FieldContext):
        match ctx.children:
            case [LuaParser.ExpContext() as val]:
                v = parse_expression(val, self._namespace)
                self._table[self._list_count] = v
                self._list_count += 1
            case _, LuaParser.ExpContext() as key, _, _, LuaParser.ExpContext() as val:
                k = parse_expression(key, self._namespace)
                v = parse_expression(val, self._namespace)
                if k not in range(1, self._list_count):
                    self._table[k] = v
            case _:
                raise NotImplementedError(f"visitField({ctx.getText()})")


def parse_table(ctx: LuaParser.TableconstructorContext, namespace: Dict) -> Any:
    visitor = VisitTable(namespace)
    visitor.visit(ctx)
    return visitor._table


_SINGLE_CHARACTER_ESCAPE_LUA_TO_PYTHON = {
    "a": "\a",
    "b": "\b",
    "n": "\n",
    "\n": "\n",  # Line continuation
    "\\": "\\",
    '"': '"',
    "'": "'",
}


def parse_normal_string(s: str):
    no_quotes = s[1:-1]
    out = ""
    was_escape = False
    for i, c in enumerate(no_quotes):
        if was_escape:
            was_escape = False
            if c == "\r" and i + 1 < len(no_quotes) and no_quotes[i + 1] == "\n":
                was_escape = True
            else:
                out += _SINGLE_CHARACTER_ESCAPE_LUA_TO_PYTHON.get(c, "\\" + c)
        elif c == "\\":
            was_escape = True
        else:
            out += c
    return out


def parse_string(ctx: LuaParser.StringContext):
    if ctx.NORMALSTRING() is not None:
        return parse_normal_string(ctx.getText())
    else:
        raise NotImplementedError(f"parse_string({ctx.getText()})")


def parse_number(ctx: LuaParser.NumberContext):
    if ctx.FLOAT() is not None:
        return float(ctx.getText())
    elif ctx.INT() is not None:
        return int(ctx.getText())
    else:
        raise NotImplementedError(f"parse_number({ctx.getText()})")


def parse_prefix_exp(ctx: LuaParser.PrefixexpContext, namespace: Dict):
    value = None

    class VisitPrefixExp(LuaVisitor):
        def visitPrefixexp(self, ctx: LuaParser.PrefixexpContext):
            if ctx.getChildCount() > 1:
                raise NotImplementedError(f"parse_prefix_exp({ctx.getText()})")
            else:
                super().visitPrefixexp(ctx)

        def visitVarOrExp(self, ctx: LuaParser.VarOrExpContext):
            nonlocal value
            match ctx.children:
                case [LuaParser.VarContext() as v]:
                    var = v.getText()
                    value = namespace[var]
                case [
                    antlr4.TerminalNode(),
                    LuaParser.ExpContext() as e,
                    antlr4.TerminalNode(),
                ]:
                    value = parse_expression(e)

    VisitPrefixExp().visit(ctx)
    return value


class ExpVisitor(LuaVisitor):
    def __init__(self, namespace: Dict):
        super().__init__()
        self._namespace = namespace
        self._value = None

    def visitExp(self, ctx: LuaParser.ExpContext):
        # print(Trees.toStringTree(ctx, None, parser))

        match ctx.children:
            case [antlr4.TerminalNode()]:
                match ctx.getText():
                    case "false":
                        self._value = False
                    case "true":
                        self._value = True
                    case "nil":
                        self._value = None
                    case _:
                        raise NotImplementedError(f"visitExp({ctx.getText()})")
            case [LuaParser.PrefixexpContext() as p]:
                self._value = parse_prefix_exp(p, self._namespace)
            case [LuaParser.NumberContext() as n]:
                self._value = parse_number(n)
            case [LuaParser.StringContext() as s]:
                self._value = parse_string(s)
            case [LuaParser.OperatorUnaryContext() as u, LuaParser.ExpContext() as e]:
                value = parse_expression(e, self._namespace)
                match u.getText():
                    case "-":
                        self._value = -value
                    case _:
                        raise NotImplementedError(
                            f"Unsupported unary operator: {u.getText()})"
                        )
            case [
                LuaParser.ExpContext() as a,
                LuaParser.OperatorMulDivModContext() as u,
                LuaParser.ExpContext() as b,
            ]:
                left = parse_expression(a, self._namespace)
                right = parse_expression(b, self._namespace)
                match u.getText():
                    case "*":
                        self._value = left * right
                    case "/":
                        self._value = left / right
                    case _:
                        raise NotImplementedError(
                            f"Unsupported binary operator: {u.getText()})"
                        )
            case [
                LuaParser.ExpContext() as a,
                LuaParser.OperatorAddSubContext() as u,
                LuaParser.ExpContext() as b,
            ]:
                left = parse_expression(a, self._namespace)
                right = parse_expression(b, self._namespace)
                match u.getText():
                    case "-":
                        self._value = left - right
                    case "+":
                        self._value = left + right
                    case _:
                        raise NotImplementedError(
                            f"Unsupported binary operator: {u.getText()})"
                        )
            case [LuaParser.TableconstructorContext() as table]:
                self._value = parse_table(table, self._namespace)
            case _:
                raise NotImplementedError(f"visitExp({ctx.getText()})")


def parse_expression(ctx: LuaParser.ExpContext, namespace: Dict = {}):
    visitor = ExpVisitor(namespace)
    visitor.visit(ctx)
    return visitor._value


class ExpListVisitor(LuaVisitor):
    def __init__(self, namespace: Dict):
        super().__init__()
        self._values = []
        self._namespace = namespace

    def visitExp(self, ctx: LuaParser.ExpContext):
        self._values.append(parse_expression(ctx, self._namespace))


class VarListVisitor(LuaVisitor):
    def __init__(self):
        super().__init__()
        self._variables = []

    def visitVarlist(self, ctx: LuaParser.VarlistContext):
        return super().visitVarlist(ctx)

    def visitVar(self, ctx: LuaParser.VarContext):
        self._variables.append(ctx.getText())


class TopLevelAssignmentVisitor(LuaVisitor):
    def __init__(self) -> None:
        super().__init__()
        self._namespace = {}

    def visit(self, tree):
        return super().visit(tree)

    def visitStat(self, ctx: LuaParser.StatContext):
        match ctx.children:
            case [
                LuaParser.VarlistContext() as var_list,
                _,
                LuaParser.ExplistContext() as exp_list,
            ]:
                var_list_visitor = VarListVisitor()
                var_list_visitor.visitVarlist(var_list)
                exp_list_visitor = ExpListVisitor(self._namespace)
                exp_list_visitor.visitExplist(exp_list)

                self._namespace.update(
                    zip(var_list_visitor._variables, exp_list_visitor._values)
                )
            case _:
                pass


def lua_to_python(text: str) -> Any:
    lexer = LuaLexer(antlr4.InputStream(text))

    stream = antlr4.CommonTokenStream(lexer)
    parser = LuaParser(stream)
    tree = parser.chunk()
    visitor = TopLevelAssignmentVisitor()
    visitor.visit(tree)
    return visitor._namespace
