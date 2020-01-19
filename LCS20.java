import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for(int i = 0; i < s.length(); i++)
        {
           char c = s.charAt(i); 
            if (stack.empty())
            {
                stack.push(c);
            }
            else
            {
                if (bracketMatch(stack.peek(), c))
                {
                    stack.pop();
                }
                else
                {
                    stack.push(c);
                }
            }
        }
        if (stack.empty())
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    
    // checks if the new char pairs with the top of the stack
    public boolean bracketMatch(char top, char c)
    {
        if (top == '(' && c == ')')
        {
            return true;
        }
        else if (top == '{' && c == '}')
        {
            return true;
        }
        else if (top == '[' && c == ']')
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}