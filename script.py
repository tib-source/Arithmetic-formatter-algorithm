```python
def arithmetic_arranger(problems, display=False):
    if len(problems) > 5:
      return "Error: Too many problems."
    def check_valid(problem):
        """
        Takes in a problem as a string and checks if its valid
        returns false if either num1 or num2 is not an int
        """
        num1, operator, num2 = problem.split(" ")
        if operator not in ["+","-"]:
            return False, "Error: Operator must be '+' or '-'."
        try:
            four_len_rule = any(len(x.strip()) > 4 for x in (num1,num2))
            if four_len_rule:
                return False, "Error: Numbers cannot be more than four digits."
            num1 = int(num1.strip())
            num2 = int(num2.strip())
            return True, num1, num2, operator
        except:
            return False, "Error: Numbers must only contain digits."

    def draw(num1, num2, ans, operator):
        len_num1 = len(str(num1))
        len_num2 = len(str(num2))
        len_ans = len(str(ans))
        biggest_len = len_num1 + 2 if len_num1 > len_num2 else len_num2 + 2
        space_top =  " "*(biggest_len-len_num1)
        space_bottom = " "*(biggest_len-(len_num2+1))
        bottom_lines = "-"*biggest_len
        if ans  != None:
            ans_spaces = " "*(biggest_len-len_ans)
            final = [
            f"{space_top}{num1}",
            f"{operator}{space_bottom}{num2}",
            f"{bottom_lines}",
            f"{ans_spaces}{ans}"
            ]
        else:
            final = [
            f"{space_top}{num1}",
            f"{operator}{space_bottom}{num2}",
            f"{bottom_lines}",
            ]
        return final
    error = []
    answer_list = []
    for equation in problems:
      values =  check_valid(equation)
      valid = values[0]
      if valid:
          num1 = values[1]
          num2 = values[2]
          operator = values[3]
          ans = (num1 + num2) if operator == "+" else  (num1 - num2)
          if display:
              drawn_answer = draw(num1,num2,ans,operator)
              answer_list.append(drawn_answer)
          else:
              ans=None
              answer_list.append(draw(num1,num2,ans,operator))
      if not valid:
          current_error = values[1]
          error += current_error
          return current_error

    def unpacker(zipped):
      str = []
      for zip in zipped:
          str.append(f"{('    ').join(zip)}") 
      return "\n".join(str)
    zipped = list(zip(*answer_list))
    return unpacker(zipped)
```

