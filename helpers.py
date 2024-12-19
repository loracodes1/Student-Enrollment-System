# Gets input and returns None, can also restruct to simple types e.g.
# integer, float, default string
def get_input(prompt, restrict_to_type = None):
    try:
        if restrict_to_type == "int":
            return int(input(prompt))
        
        if restrict_to_type == "float":
            return float(input(prompt))
        
        return input(prompt)
    
    except:
        return None
    