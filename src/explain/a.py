class Node[T]:
    def __init__(
        self,
        value: T,
        previous: "Node[T] | None" = None,
        next_node: "Node[T] | None" = None,
    ) -> None:
        self.value = value
        self.previous = previous
        self.next_node = next_node


class A[T]:
    def __init__(self) -> None:
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None

    def append_to_tail(self, value: T) -> None:
        n_node = Node(value, previous=self.tail)
        if self.head is None:
            self.head = n_node

        if self.tail is not None:
            self.tail.next_node = n_node

        self.tail = n_node

    def append_to_head(self, value: T) -> None:
        n_node = Node(value, next_node=self.head)
        if self.tail is None:
            self.tail = n_node

        if self.head is not None:
            self.head.previous = n_node

        self.head = n_node

    def peek_tail(self) -> T | None:
        return self.tail.value if self.tail is not None else None

    def peek_head(self) -> T | None:
        return self.head.value if self.head is not None else None

    def pull_tail(self) -> T | None:
        if self.tail is None:
            return None

        old_tail = self.tail
        self.tail = old_tail.previous
        if self.tail is not None:
            self.tail.next_node = None
        else:
            self.head = None  # List becomes empty

        return old_tail.value

    def pull_head(self) -> T | None:
        if self.head is None:
            return None

        old_head = self.head
        self.head = old_head.next_node
        if self.head is not None:
            self.head.previous = None
        else:
            self.tail = None  # List becomes empty

        return old_head.value

    def is_empty(self) -> bool:
        return self.head is None
