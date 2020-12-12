class MyStack {

    Queue<Integer> queue;
    Queue<Integer> queueHelp;
    
    /** Initialize your data structure here. */
    public MyStack() {
        this.queue = new LinkedList<Integer>();
        this.queueHelp = new LinkedList<Integer>();
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        queue.add(x);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        int top = 0;
        while (queue.peek() != null) {
            if (queue.size() == 1) {
                top = queue.poll();
                break;
            }
            queueHelp.add(queue.poll());
        }
        while (queueHelp.peek() != null) {
            queue.add(queueHelp.poll());
        }
        return top;
    }
    
    /** Get the top element. */
    public int top() {
        int top = 0;
        while (queue.peek() != null) {
            if (queue.size() == 1) {
                top = queue.peek();
            }
            queueHelp.add(queue.poll());
        }
        while (queueHelp.peek() != null) {
            queue.add(queueHelp.poll());
        }
        return top;
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        return queue.peek() == null;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */