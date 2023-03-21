import ast

class Helper():
    
    def cast_to_type(resultString):
        if resultString is not None:
            resultString=resultString.strip()
            if len(resultString) == 0 or resultString == "null" : return None
            try:
                t=ast.literal_eval(resultString)
                return t

            except ValueError:
                return resultString
            except SyntaxError:
                return resultString
        else:
            return None

if __name__ == "__main__":
    print()
    print(Helper.cast_to_type("test"))