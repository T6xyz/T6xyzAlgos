from manim import *

from BSTNode import BSTNode

from BST import *



def animateAdd(scene, bst, node, parent, edges, nodes, VERTEX_CONF, LAYOUT_CONFIG, circle, text):
    if (parent == None): # Add to empty BST
        bst.g = Graph([node.val], [], vertex_config = VERTEX_CONF, labels = True, layout_scale = 0.5)
        nodes.add(node.val)
        
        scene.add(bst.g)
    
        scene.play(bst.g.animate.change_layout("tree", root_vertex = 0, layout_config = LAYOUT_CONFIG))
        scene.play(bst.g.vertices[node.val].animate.shift(3 * UP))
    else:
        bst.g._add_vertex(node.val, vertex_config = VERTEX_CONF, label = True, position = bst.g.vertices[parent.val].get_center())

        scene.play(bst.g.vertices[node.val].animate.shift(LEFT + DOWN))
        scene.play(circle.animate.move_to(bst.g.vertices[node.val].get_center()))

        scene.remove(text)

        text = MathTex(f"curr = {node.val}", color = RED, font_size = 25)
        text.move_to(bst.g.vertices[node.val].get_center() + RIGHT)

        bst.g._add_edge((parent.val, node.val))
        edges.add((parent.val, node.val))

        scene.add(text)

        scene.wait()

        scene.remove(text)

def animateTraverse(scene, node, circle, parent):
    pass

def animateDelete(scene, node, parent, edges, nodes):
    pass

def shift():
    pass