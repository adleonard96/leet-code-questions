/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */


function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let num1 = [l1.val]
    let num2 = [l2.val]

    while(l1.next){
        l1 = l1.next
        num1.push(l1.val);
    }

    while(l2.next){
        l2 = l2.next
        num2.push(l2.val)
    }
    let carryOver = 0;
    let maxLength = num1.length > num2.length ? num1.length : num2.length
    let head;
    let currentNode;
    for (let i = 0; i < maxLength; i ++){
        num1[i] ??= 0;
        num2[i] ??= 0;
        if(!head){
            let value = num1[i] + num2[i];
            head = new ListNode(value % 10);
            currentNode = head;
            if(value > 9){
                carryOver ++;
            }
        } else {
            let value = num1[i] + num2[i] + carryOver;
            carryOver = 0;
            if(value > 9){
                carryOver ++;
            }
            currentNode.next = new ListNode(value % 10);
            currentNode = currentNode.next
        }
        if (carryOver > 0){
            currentNode.next = new ListNode(carryOver)
        }
    }
    
    return head;
};