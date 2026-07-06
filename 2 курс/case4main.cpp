#include <gtest/gtest.h>
#include <vector>

// =========================================================
// ИНТЕРФЕЙСЫ КЛАССОВ (Заглушки)
// =========================================================

class Queue {
public:
    void push(int value) {} // Интерфейс
    int pop() { return 0; } // Интерфейс
    bool isEmpty() { return true; }
};

class Heap {
public:
    void push(int value) {} // Интерфейс
    int pop() { return 0; } // Интерфейс
    int peek() { return 0; }
};

class BinaryTree {
public:
    void push(int value) {}     // Интерфейс
    void pop(int value) {}      // Интерфейс
    bool search(int value) { return false; } // Интерфейс
};

// =========================================================
// ЮНИТ-ТЕСТЫ
// =========================================================

// Тесты для Очереди (Queue)
TEST(QueueTest, BasicOperations) {
    Queue q;
    q.push(10);
    q.push(20);
    EXPECT_NO_THROW(q.push(30));
    EXPECT_EQ(q.pop(), 0);
}

TEST(QueueTest, EmptyStatus) {
    Queue q;
    EXPECT_TRUE(q.isEmpty());
}

// Тесты для Кучи (Heap)
TEST(HeapTest, PushPopTest) {
    Heap h;
    h.push(5);
    h.push(15);
    EXPECT_NO_THROW(h.push(10));
    EXPECT_EQ(h.pop(), 0);
}

TEST(HeapTest, PeekTest) {
    Heap h;
    h.push(100);
    EXPECT_EQ(h.peek(), 0);
}

// Тесты для Бинарного дерева (Binary Tree)
TEST(BinaryTreeTest, SearchTest) {
    BinaryTree tree;
    tree.push(50);
    tree.push(30);
    tree.push(70);
    EXPECT_FALSE(tree.search(50)); 
}

TEST(BinaryTreeTest, RemoveTest) {
    BinaryTree tree;
    tree.push(10);
    EXPECT_NO_THROW(tree.pop(10));
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
