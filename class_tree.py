class Tree:
    """Abstract base class representing a tree structure"""
    #------------------------- nested Position class ------------------------------
    class Position:
        """ An abstraction represention the location of a single element"""

        def element(self):
            """ Return the element stored at this Position"""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """ Return True if other Position represents the same location """
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """ Return True if other does not represent the same location """
            return not (self == other)

    #--------abstract methods that concrete subclass must support----------------
    def root(self):
        """ Return Position representing the tree's root (or None if empty)"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """ Return Position representing p's parent (or None if p is root)"""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """ Return number of children that Position p has """
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """ Generate an iteration of Positions representing p's children """
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return to the total number of elements in the tree"""
        raise NotImplementedError('must be implemented by subclass')

    #------------concrete methods implemented in this class-------------------
    def is_root(self, p):
        """ Return True if Position p represents the root of the tree"""
        return self.root()==p

    def is_leave(self, p):
        """Return True if Position p does not have any children """
        return self.num_children(p)==0

    def is_empty(self):
        """Return True if the tree is empty"""
        return len(self)==0

#---------Class Binary Tree -------------------------------------------------
class BinaryTree (Tree):
    """ Abstract base class representing a binary tree structure """
    #------------------ additional abstract methods -------------------------
    def left(self, p):
        """ Return a Position representing p's left child
        Return None if p does not have a left child
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """ Return a Position representing p's right child
        Return None if p does not have a right child
        """
        raise NotImplementedError('must be implemented by subclass')
    
    #--------------- concerete methods implemented in this class -------------
    def sibling(self, p):
        """ Return a Position represeting p's sibling (or None if no sibling)"""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """ Generate an iteration of Positions representing p's children """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
        










































