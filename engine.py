import math

#  that for normal calculator funciton with somearithmatic operartors
import math
from fractions import Fraction

import math
from fractions import Fraction
import math
from fractions import Fraction

def on_click(value, display, result_label, history_display, history):
    current_text = display.text()
    science = ['sin', 'cos', 'tan', 'log', '√']

    # Clear display if the current text contains an error
    if 'Error' in current_text:
        current_text = ''
        display.setText('')

    if value == 'RESET':
        display.clear()
        result_label.clear()
        history.clear()
        history_display.clear()
    elif value == 'AC':
        display.clear()
        result_label.clear()
    elif value == '⌫':
        display.setText(current_text[:-1])
        result_label.setText(current_text[:-1])
    elif value == '=':
        try:
            # Convert common symbols to Python-friendly format
            expression = (
                current_text
                .replace('⌃', '**')  # Convert '^' to '**' for power
                .replace('×', '*')  # Convert '×' to '*' for multiplication
                .replace('÷', '/')  # Convert '÷' to '/' for division
                .replace('mod', '%')  # Convert 'mod' to '%' for modulo
                .replace('π',str(math.pi))  # Replace 'π' with math.pi
                .replace('√', 'math.sqrt')  # Replace '√' with math.sqrt for square root
            )

            # Ensure that scientific functions like sin, cos, etc., are handled correctly
            for func in science:
                # Replace with math function and radians for angle functions
                expression = expression.replace(f"{func}(", f"math.{func}(math.radians(")

            # Handle missing closing parentheses for scientific functions
            for func in science:
                if expression.count(f"math.{func}(math.radians(") > expression.count(")") :
                    expression += ")"

            # Evaluate the expression safely
            result = eval(expression)
            calculator_result(result, f"{current_text}", current_text, display, result_label, history, history_display)
        except ZeroDivisionError:
            display.setText("Error: Division by Zero")
            result_label.setText("Error: Division by Zero")
        except Exception as e:
            display.setText(f"Error: {str(e)}")
            result_label.setText(f"Error: {str(e)}")

    elif value == '!':
        try:
            num = int(current_text)
            if num < 0:
                display.setText("Error: Negative Factorial")
                result_label.setText("Error: Negative Factorial")
            else:
                result = math.factorial(num)
                calculator_result(result, f"{num}!", current_text, display, result_label, history, history_display)
        except ValueError:
            display.setText("Error: Invalid Input")
            result_label.setText("Error: Invalid Input")
    elif value == '⇄':  # Fraction <-> Decimal Converter
        try:
            if '/' in current_text:  # Convert fraction to decimal
                num = float(eval(current_text))  # Evaluates '1/3' -> 0.3333
                calculator_result(num, f"{current_text} -> {num}", current_text, display, result_label, history, history_display)
            else:  # Convert decimal to fraction
                num = float(current_text)
                fraction = Fraction(num).limit_denominator()
                calculator_result(fraction, f"{num} -> {fraction}", current_text, display, result_label, history, history_display)
        except ValueError:
            display.setText("Error: Invalid Input")
            result_label.setText("Error: Invalid Input")
    elif value in ('(', ')'):  # Handle brackets
        display.setText(current_text + value)
        result_label.setText(current_text + value)
    else:
        if value in science:
            value += '('  # Append '(' when scientific function is pressed
        display.setText(current_text + value)
        result_label.setText(current_text + value)




        
# bin hex oct converter keyboard
def on_converter(value, display, result_label, history_display, history,window,clear_history):
    current_text = display.text()
    if 'Error' in current_text or current_text=='' and (not value=='History'):
        current_text = ''
        display.setText('')
        return
    if value =='.' and  ('.' in current_text):
        return
 
    
    conversion_map = {
        'Dec-Bin': lambda x: bin(int(x))[2:],
        'Bin-Dec': lambda x: str(int(x, 2)),
        'Dec-Oct': lambda x: oct(int(x))[2:],
        'Oct-Dec': lambda x: str(int(x, 8)),
        'Dec-Hex': lambda x: hex(int(x))[2:],
        'Hex-Dec': lambda x: str(int(x, 16))
    }

    if value in conversion_map:
        try:
            result = conversion_map[value](current_text)
            calculator_result(result, f"{current_text}({value.split('-')[0]}) = {result}({value.split('-')[1]})", current_text, display, result_label, history, history_display)
        except Exception as e:
            display.setText('Error: Invalid Input')
            result_label.setText("Error: Invalid Input" )
    if value == "History":
        history_display.setVisible(not history_display.isVisible())
        clear_history.setVisible(not clear_history.isVisible())
        window.resize(700, 550) if history_display.isVisible() else window.resize(450, 550)




 
def calculator_result(result, operations, current_text, display, result_label, history, history_display):
    # if history == '':
    #     history.append(f"You Previos All History ›")
    if len(history) == 0:
        history.append(f"You Previos All History ›")
        history.append("")

    if len(str(result))>50:
        display.setText("Error: limit cross data! Overloaded 50 digit")
        result_label.setText("Error: limit cross data")
        return 
    display.setText(str(result))
    result_label.setText(f"{operations} = {result}")
    history.append(f"{operations} = {result}")
    history_display.clear()
    for entry in history:
        history_display.append(entry)
