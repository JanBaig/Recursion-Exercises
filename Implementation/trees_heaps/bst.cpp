#include <iostream>

// Struct - don't care to change default public access specifier
struct TreeNode {
    int value;
    TreeNode* left; // Note - self-referential
    TreeNode* right;
    TreeNode(int x) : value(x), left(nullptr), right(nullptr) {}
};

class BST {
public:
    TreeNode* root;
    BST() : root(nullptr) {} 
    
    void insert(int val) { root = insertRecursive(root, val); }
    
    TreeNode* insertRecursive(TreeNode* node, int val) {
        if (node == nullptr) { return new TreeNode(val); }
        if (val < node->value) { node->left = insertRecursive(node->left, val); }
        else { node->right = insertRecursive(node->right, val); } 
        return node;
    }

    void deleteValue(int val) { root = deleteValue(root, val); }
    
    TreeNode* deleteValue(TreeNode* node, int val) {
        if (node == nullptr) { return node; } 
        if (val < node->value) { node->left = deleteValue(node->left, val); }
        else if (val > node->value) { node->right = deleteValue(node->right, val); }
        else {  
            if (node->left == nullptr) {
                TreeNode* temp = node->right;
                delete node; 
                return temp;
            } else if (node->right == nullptr) {
                TreeNode* temp = node->left;
                delete node;
                return temp;    
            } else {
                TreeNode* temp = minValueNode(node->right); 
                node->value = temp->value;
                node->right = deleteValue(node->right, temp->value);
            }
            return node;
        }
    }
    
    TreeNode* minValueNode(TreeNode* node) {
        TreeNode* current = node;
        while(current && current->left != nullptr) { current = current->left; }
        return current;
    }
};

int main() {
    
    BST bst;
    bst.insert(50); bst.insert(30); bst.insert(70); bst.insert(20); bst.insert(40); bst.insert(60);
    bst.insert(80);
    
    return 0;
}

/*
Notes

Self-referential: You cannot create instances of an incomplete type but you can include pointers or references to it. 
This is because the size of a pointer is always known regardless of if or not the size of what it pointsto is known or not. 

*/

