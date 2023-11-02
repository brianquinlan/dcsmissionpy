from dcsmissionpy._parser import lua_to_python


def test_true_assignment():
    assert lua_to_python(r"happy = true") == {"happy": True}


def test_false_assignment():
    assert lua_to_python(r"sad = false") == {"sad": False}


def test_nil_assignment():
    assert lua_to_python(r"pet = nil") == {"pet": None}


def test_float_assignment():
    assert lua_to_python(r"gravity = 9.8") == {"gravity": 9.8}


def test_int_assignment():
    assert lua_to_python(r"dozen = 12") == {"dozen": 12}


def test_normal_string_assignment():
    assert lua_to_python(r'name = "Brian"') == {"name": "Brian"}


def test_normal_string_assignment_line_continuation():
    assert lua_to_python('name = "Brian\\\r\nQuinlan"') == {"name": "Brian\nQuinlan"}
    assert lua_to_python('name = "Brian\\\nQuinlan"') == {"name": "Brian\nQuinlan"}


def test_normal_string_assignment_escaped_quotes():
    assert lua_to_python('name = "\\"Hello World\\""') == {"name": '"Hello World"'}
    assert lua_to_python('''name = "\\'Hello World\\'"''') == {"name": "'Hello World'"}


def test_normal_string_assignment_escape_backslash():
    assert lua_to_python('escape = "\\\\"') == {"escape": "\\"}


def test_normal_string_assignment_escapes():
    assert lua_to_python('escape = "\\a"') == {"escape": "\a"}
    assert lua_to_python('escape = "\\b"') == {"escape": "\b"}
    assert lua_to_python('escape = "\\n"') == {"escape": "\n"}


def test_var_args():
    assert lua_to_python(r'name, age, male = "Brian", 48, true') == {
        "name": "Brian",
        "age": 48,
        "male": True,
    }


def test_unary_minus():
    assert lua_to_python(r"gravity = -9.8") == {"gravity": -9.8}
    assert lua_to_python(r"gravity = -9") == {"gravity": -9}


def test_binary_plus():
    assert lua_to_python(r"sum = 1+2+3") == {"sum": 6}


def test_binary_minus():
    assert lua_to_python(r"sum = 3-2-1") == {"sum": 0}


def test_binary_multiply():
    assert lua_to_python(r"product = 1*2*3") == {"product": 6}


def test_binary_divide():
    assert lua_to_python(r"quotient = 6/3/2") == {"quotient": 1}


def test_math_parenthesis():
    assert lua_to_python(r"result = 2*(3+5)/4+1") == {"result": 5}


def test_math_order_of_operations():
    assert lua_to_python(r"result = 3+2*5") == {"result": 13}
    assert lua_to_python(r"result = 3*2+5") == {"result": 11}
    assert lua_to_python(r"result = 2+4*(5-1)") == {"result": 18}
    assert lua_to_python(r"result = 2*4+(5-1)") == {"result": 12}


def test_expression_key_table():
    assert (lua_to_python(r'gravity = {["earth"] = 9.8; ["mars"] = 4.7}')) == {
        "gravity": {"earth": 9.8, "mars": 4.7}
    }


def test_list_table():
    assert (lua_to_python(r'fruit = {"apple", "banana", "cantaloupe"}')) == {
        "fruit": {1: "apple", 2: "banana", 3: "cantaloupe"}
    }


def test_table_mixed():
    assert (
        lua_to_python(
            r"""fruits_and_animals = {
                    [0] = "ape",
                    "banana", "cantaloupe",
                    [0] = "ant", [1] = "bat", [2] = "cat",
                    "date", "elderberry"
                }"""
        )
        == {
            "fruits_and_animals": {
                0: "ant",
                1: "banana",
                2: "cantaloupe",
                3: "date",
                4: "elderberry",
            }
        }
    )


def test_use_variable_in_expression():
    assert (lua_to_python(r'greeting = "hello"; again = greeting')) == {
        "greeting": "hello",
        "again": "hello",
    }
    assert (lua_to_python(r"c = 25; f = c * 9 / 5 + 32")) == {"c": 25, "f": 77.0}


def test_ignore_funct():
    assert (
        lua_to_python(
            r"""

a = "value1"
function f(a,b)
    b = "value2"
    return result
end
c = "value3"
"""
        )
        == {"a": "value1", "c": "value3"}
    )


def test_multiple_string_assignment():
    assert (
        lua_to_python(
            r"""
string1 = "value1"
string2 = "value2"
"""
        )
        == {"string1": "value1", "string2": "value2"}
    )


def test_multiple_boolean_assignment():
    assert (
        lua_to_python(
            r"""
CockpitMouse = true
DisableSnapViewsSaving = false"""
        )
        == {"CockpitMouse": True, "DisableSnapViewsSaving": False}
    )


"""
mouseSpeedCoeff = 0.45 -- experimental, need tuning

CockpitMouse = true --false
CockpitMouseSpeedSlow = 1.0 * mouseSpeedCoeff
CockpitMouseSpeedNormal = 10.0 * mouseSpeedCoeff
CockpitMouseSpeedFast = 20.0 * mouseSpeedCoeff
CockpitKeyboardAccelerationSlow = 5.0
CockpitKeyboardAccelerationNormal = 30.0
CockpitKeyboardAccelerationFast = 80.0
CockpitKeyboardZoomAcceleration = 300.0
DisableSnapViewsSaving = false
UseDefaultSnapViews = true
CockpitPanStepHor = 45.0
CockpitPanStepVert = 30.0
CockpitNyMove = true

mission = 
{
    ["requiredModules"] = 
"""
