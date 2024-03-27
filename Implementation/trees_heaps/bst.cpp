#include <iostream>

// Struct - don't care to change default public access specifier
struct TreeNode {
    int value;
    TreeNode* left; // Note - self-referential
    TreeNode* right;
    TreeNode(int x) : value(x), left(nullptr), right(nullptr) {}
}

int main() {
    return 0;
}


/*
Notes

Self-referential: You cannot create instances of an incomplete type but you can include pointers or references to it. This is because the size of a pointer is always known regardless of if or not the size of what it pointers at is known or not. 
 


*/


