#include<iostream>
using namespace std;


// A Bianry Tree node
struct Node
{
    int key;
    struct Node *left, *right;
};
 
// Utility function creates a new binary tree node with given key
Node * newNode(int k)
{
    Node *temp = new Node;
    temp->key = k;
    temp->left = temp->right = NULL;
    return temp;
}

// bool basecase(Node *root, int n1, int n2){
// 	if(root == NULL){
// 		return true;
// 	}
// 	cout<<root->key<<endl;
// 	if( (root -> key == n1) || (root -> key == n2) ){
// 		cout<<"in if"<<endl;
// 		return true;
// 	}

// 	//return basecase(root->left,n1,n2) && basecase(root->right, n1, n2);
// 	basecase(root->left, n1, n2);
// 	basecase(root->right, n1, n2);
// 	//basecase(root->right, n1, n2);
// }


// void preorder(Node *root){
// 	if(root == NULL){
// 		return;
// 	}
// 	cout<<root->key;
// 	preorder(root->left);
// 	preorder(root->right);
// }

void preorderLCA(Node *root, int n1, int n2, int* presence){
	if(root == NULL){
		return;
	}
	cout<<root->key;
	if( (root -> key == n1) || (root -> key == n2) ){
		*presence = 1;
	}
	preorderLCA(root->left, n1, n2, presence);
	preorderLCA(root->right, n1, n2, presence);
}


// This function returns pointer to LCA of two given values n1 and n2.
// This function assumes that n1 and n2 are present in Binary Tree
struct Node *findLCA(struct Node* root, int n1, int n2)
{
    // Base case
    if (root == NULL) return NULL;
 
    // If either n1 or n2 matches with root's key, report
    // the presence by returning root (Note that if a key is
    // ancestor of other, then the ancestor key becomes LCA
    if (root->key == n1 || root->key == n2)
        return root;
 
    // Look for keys in left and right subtrees
    Node *left_lca  = findLCA(root->left, n1, n2);
    Node *right_lca = findLCA(root->right, n1, n2);
 
    // If both of the above calls return Non-NULL, then one key
    // is present in once subtree and other is present in other,
    // So this node is the LCA
    if (left_lca && right_lca)  return root;
 
    // Otherwise check if left subtree or right subtree is LCA
    return (left_lca != NULL)? left_lca: right_lca;
}
// Driver program to test above functions
int main()
{
    // Let us create the Binary Tree shown in above diagram.
    Node * root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    root->right->left = newNode(6);
    root->right->right = newNode(7);
    cout << "LCA(4, 7) = " << findLCA(root, 2, 7)->key<<endl;
    //preorder(root);
    cout << "nLCA(4, 6) = " << findLCA(root, 4, 6)->key;
    cout << "nLCA(3, 4) = " << findLCA(root, 3, 4)->key;
    cout << "nLCA(2, 4) = " << findLCA(root, 2, 4)->key;
    return 0;
}