
#creating the stack
def create_stack():
    stack=[]
    return stack

#checking stack is empty or not
def checking_stack(stack):
    return len(stack)==0

#Adding items to the stak

def adding_elements(stack,element):
    stack.append(element)
    print("item adding_elementsed to the stack")

#removing item from the stack
def removing_element(stack):
    if(checking_stack(stack)):
        return "stack is  empty"

    stack.pop()


stack = create_stack()
adding_elements(stack, str(1))
adding_elements(stack, str(2))
adding_elements(stack, str(3))
adding_elements(stack, str(4))
print("popped item: " + removing_element(stack))
print("stack after popping an element: " + str(stack))


