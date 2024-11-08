def process_math_operation(math_op):
    try:
        # Use eval to evaluate the expression
        result = eval(math_op)
        return result
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return None