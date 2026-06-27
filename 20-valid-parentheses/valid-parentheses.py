class Solution(object):
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')' and len(stack)!=0 and stack[-1] == '(' :
                stack.pop()
            elif s[i] == ']' and len(stack)!=0 and stack[-1] == '[' :
                stack.pop()
            elif s[i] == '}' and len(stack)!=0 and stack[-1] == '{':
                stack.pop() 
            elif (s[i] == ')' and len(stack)==0) or (s[i]==')' and len(stack)!=0 and stack[-1]!='('):
                return False
            elif s[i] == ']' and len(stack)==0 or (s[i]==']' and len(stack)!=0 and stack[-1]!='[') :
                return False
            elif s[i] == '}' and len(stack)==0 or (s[i]=='}' and len(stack)!=0 and stack[-1]!='{'):
                return False
        if len(stack)==0:
            return True
        else:
            return False