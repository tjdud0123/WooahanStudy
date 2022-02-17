## [2022.1.17 책풀이 발표]

### 1-8 ) Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to O.

```python
# 숙제로 남긴 풀이
def getZeroMatrix(matrix):
    zero_row, zero_col = set(), set()
    row_len, col_len = len(matrix), len(matrix[0])

    for i in range(row_len):
        for j in range (col_len):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)
    for y in zero_row:
        matrix[y] = [0] * col_len
            
    for x in zero_col:
        for j in range(row_len):
            matrix[j][x] = 0

    return matrix
```

```c++
/* 책 첫번째 풀이 - 각 행, 각 열마다 0이 들어있는지 기록후 변환 */
void setZeros(int[][] matrix) {
    boolean[] row = new boolean[matrix .length];
    boolean[] column = new boolean[matrix[0].length];

    //Store the row and column index with value 0
    for (int i= 0; i < matrix.length; i++) {
        for (int j = 0; j < matrix[0].length;j++) {
            if (matrix[i][j] == 0) {
                row[i] = true;
                column[j] = true;
            }
        }
    } 
    // Nullify rows
    for (inti= 0; i < row.length; i++) {
        if (row[i]) nullifyRow(matrix, i);
    }

    // Nullify columns
    for (int j = 0; j < column.length; j++) {
        if (column[j]) nullifyColumn(matrix, j);
    }
}
void nullifyRow(int[][] matrix, int row) {
    for (int j = 0; j < matrix[0].length; j++) {
        matrix[row][j] = 0;
    }
}
void nullifyColumn(int[][] matrix, int col) {
    for (int i= 0; i < matrix.length; i++) {
        matrix[i][col] = 0;
    }
} 
```
![image](https://user-images.githubusercontent.com/22907830/149650911-4fc45753-f7f1-4633-a502-0e3595de511d.png)

```c++
/* 책 두번째 풀이 - 첫 번째 행을 row배열로, 첫 번째 열을 column배열로 사용 => 공간효율 O(N) -> O(1) */
setZeros(int[][] matrix) {
    boolean rowHasZero = false;
    boolean colHasZero = false;		

    //Check if first row has a zero
    for (int j = 0; j < matrix[0].length; j++) {
        if (matrix[0][j] == 0) {
            rowHasZero = true;
            break;
        }
    }		

    //Check if first column has a zero
    for (int i = 0; i < matrix.length; i++) {
        if (matrix[i][0] == 0) {
            colHasZero = true;
            break;
        }
    }		

    //Check for zeros in the rest of the array
    for (int i = 1; i < matrix.length; i++) {
        for (int j = 1; j < matrix[0].length;j++) {
            if (matrix[i][j] == 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }		

    //Nullify rows based on values in first column
    for (int i = 1; i < matrix.length; i++) {
        if (matrix[i][0] == 0) {
            nullifyRow(matrix, i);
        }
    }		

    //Nullify columns based on values in first row
    for (int j = 1; j < matrix[0].length; j++) {
        if (matrix[0][j] == 0) {
            nullifyColumn(matrix, j);
        }
    }	

    //Nullify first row
    if (rowHasZero) {
        nullifyRow(matrix, 0);
    }

    //Nullify first column
    if (colHasZero) {
        nullifyColumn(matrix, 0);
    }
}	
```

### 2-6 ) Implement a function to check if a linked list is a palindrome.

![image](https://user-images.githubusercontent.com/22907830/149364466-318081cc-e07b-47e7-8f8c-c0e55a404771.png)

```python
# 숙제로 남긴 풀이
def checkIsPalindrome(head):
    slow, fast = head, head
    stack = []

    while fast and fast.next:
        stack.append(slow.data)
        slow, fast = slow.next, fast.next.next
 
    # 홀수개일때 가운데꺼 스킵
    if fast:
        slow = slow.next

    while slow:
        if slow.data != stack[-1]:
            return False
        else:
            stack.pop()
            slow = slow.next

    return True
```
![image](https://user-images.githubusercontent.com/22907830/149365688-0423ec2b-8ef6-4995-851f-0c3033ff2e63.png)


```python
# recursive 다른버전

def ispalindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return ispalindrome(word[1:-1])
```

```c++
/* 책 세번째 풀이 */

// isPalindromeRecurse 타입
class Result {
    // 각 단계에서 회문인지 여부와 다음 비교노드를 반환
    public LinkedListNode node;
    public boolean result;
}
// LinkedListNode 길이 구하기
int lengthOfList(LinkedListNode n) {
    int size = 0;
    while (n != null) {
        size++;
        n = n.next;
    }
    return size;
}

// 팰린드롬인지 판단
boolean isPalindrome(LinkedListNode head) {
    int length = lengthOfList(head);
    Result p = isPalindromeRecurse(head, length);
    return p.result;
}

// 재귀적 호출
Result isPalindromeRecurse(LinkedListNode head, int length) {
    if (head == null || length <= 0) {
        // 노드 개수가 짝수일때
        return new Result(head, true);
    } else if (length == 1) { 
        // 노드 개수가 홀수일때
        return new Result(head.next, true);
    }

    // 부분 리스트를 재귀적으로 호출한다
    Result res = isPalindromeRecurse(head.next, length-2);

    // 아래 호출 결과 회문이 아니라는 사실이 밝혀지면, 그결과값을 반환한다
    if (!res.result || res.node == null) {
        return res;
    }

    // 두 노드의 값이 같은지 확인한다
    res.result = (head.data == res.node.data);

    // 그다음에 비교할 노드를 반환한다
    res.node = res.node.next;

    return res;
}


```

<br>

> +알파 -> sum = 팰린드롬 + 팰린드롬.reverse <br>
sum + sum.reverse =>  팰린드롬!

![image](https://user-images.githubusercontent.com/22907830/149362953-e42d1fcb-74ff-435f-a5be-ce028887fc3e.png)

### 3-2 ) Stack Min : How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.

![image](https://user-images.githubusercontent.com/22907830/149355400-e3f44315-2c06-41fc-bd39-ed8e3c48eae4.png)

```python
# 숙제로 남긴 풀이
class Stack:

    def __init__(self):
        self.arr = []
        self.min_arr = []

    def getMin(self):
        return self.min_arr[-1] if self.min_arr else None

    def push(self, value):
        self.arr.append(value)
        min_val = min(self.min_arr[-1], value) if self.min_arr else value
        self.min_arr.append(min_val)

    def pop(self):
        if not self.arr:
            return None
        self.arr.pop()
        self.min_arr.pop()
```

![image](https://user-images.githubusercontent.com/22907830/149356554-46fcf342-4a21-4496-bd0b-0d2e84731495.png)

```c++

/* 책 마지막 풀이 */

public class StackWithMin2 extends Stack {
    Stack s2;
    public StackWithMin2() {
        s2 = new Stack();    
    }

    public void push(int value) {
        if (value <= min()) {
            s2.push(value);
        }
        super.push(value);
    }

    public Integer pop() {
        int value = super.pop();
        if (value == min()) {
            s2.pop();   
        }
        return value;
    }

    public int min() {
        if (s2.isEmpty()) {
            return Integer.MAX_VALUE;
        } else {
            return s2.peek();
        }
    }

}

```
>  👀 **공간 효율성이 좋아짐** n개 vs n개 미만