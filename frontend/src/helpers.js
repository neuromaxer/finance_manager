class FiFoQueue {
    constructor() {
        this.queue = [];
    }
    // add a trade to the end of the queue
    enqueue(trade) {
        this.queue.push(trade);
    }

    // remove and return the first trade in the queue
    dequeue() {
        if (this.isEmpty()) return null;
        return this.queue.shift();
    }

    // return the first trade in the queue without removing it
    peek() {
        if (this.isEmpty()) return null;
        return this.queue[0];
    }

    // check if the queue is empty
    isEmpty() {
        return this.queue.length === 0;
    }

    length() {
        return this.queue.length;
    }
}
