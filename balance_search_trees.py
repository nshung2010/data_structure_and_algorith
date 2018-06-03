def _relink(self, parent, child, make_left_child):
    """relink parentnode with child node (we allow child to be None)"""
    if make_left_child:
        parent._left = child
    else:
        parent._right = child
    if child is not None:
        child._parent = parent

def _rotate(self, p):
    """Rotate position p above its parent"""
    x = p._node
    y = x._parent                         # We assume this exists
    z = y._parent                         # grandparent (possibly None)
    if z is None:
        self._root = x                    # x becomes root
        x._parent = None
    else:
        self._relink(z, x, y==z._left)    # x becomes a direct child of z
    # now rotae x and y, including transfer of middle subtree
    if x == y._left:
        self._relink(y, x._right, True)   # x._right becomes left child of y
        self._relink(x, y, False)         # y becomes right child of x
    else:
        self._relink(y, x._left, False)   # x._left becomes right child of y
        self._relink(x, y, True)          # y becomes left child of x

def _restructure(self, x):
    """ Perform trinode restructure of position x with parent/grand parent"""
    y = self.parent(x)
    z = self.parent(y)
    if (x==self.right(y))==(y==self.right(z)): # Matching allignments
        self._rotate(y)                        # single rotation (of y)
        return y                               # y is new subtree root
    else:                                      # opposite alignments
        self._rotate(x)                        # double rotation (of x)
        self._rotate(x)
        return x                               # x is new subtree root
class AVLTreeMap(TreeMap):
    """Sorted map implementation using an AVL tree"""
    #------------------------nested _Node class -------------------------------
    class _Node(TreeMap._Node):
        """Node class for AVL maintain height value for balanceing"""
        __slots__ = '_height'      # additional data member to store height

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0                 # will be recomputed during balancing

        def left_height(self):
            return self._left._height if self._left is not None else 0

        def right_height(self):
            return self._right._height if self._right is not None else 0
    #-------------------------positional-based utility methods--------------------
    def _recompute_height(self, p):
        p._node._height = 1 + max(p._node.left_height(), p._node.right_height())

    def _isbalanced(self, p):
        return abs(p._node.left_height() - p._node.right_height()) <= 1

    def _tall_child(self, p, favorleft = False):  #parameter controls tiebreaker
        if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        # if child is on left, favor left grandchild; else favor right gandchild
        alignment = (child==self.left(p))
        return self._tall_child(child, alignment)

    def _rebalance(self, p):
        while p is not None:
            old_height = p._node._height         # trivially 0 if new node
            if not self._isbalanced(p):          # imbalance detected!
                # perform trinode restructuring, setting p to resulting root,
                # and recompute new local heights after the restructuring
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)           # adjust for recent changes
            if p._node._height = old_height:    # has height changed?
                p = None
            else:
                p = self.parent(p)              # repeat with parent

    # --------------- override balancing hooks-------------------------------------
    def _rebalance_insert(self, p):
        self._rebalance(p)
    def _rebalance_delete(self, p):
        self._rebalance(p)

    






































