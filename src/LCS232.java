import java.util.*;

class MyQueue {

    Stack<Integer> stack;
    Stack<Integer> helper;
    /** Initialize your data structure here. */
    public MyQueue() {
        stack = new Stack();
        helper = new Stack();
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        stack.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        while (!stack.empty())
            helper.push(stack.pop());
    
        int result = helper.pop();
        
        while (!helper.empty())
            stack.push(helper.pop());
        
        return result;
    }
    
    /** Get the front element. */
    public int peek() {
        while (!stack.empty())
            helper.push(stack.pop());

        int result = helper.peek();
       
        while (!helper.empty())
            stack.push(helper.pop());
        
        return result;
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return stack.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */