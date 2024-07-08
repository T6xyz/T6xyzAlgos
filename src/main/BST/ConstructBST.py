from manim import *

from BSTNode import BSTNode

from BST import *



def animateAdd(scene, bst, node, parent, edges, nodes, VERTEX_CONF, LAYOUT_CONFIG, circle, text, direction, factor):
    if (parent == None): # Add to empty BST
        bst.g = Graph([node.val], [], vertex_config = VERTEX_CONF, labels = True, layout_scale = 0.25)
        nodes.add(node.val)
        
        scene.add(bst.g)
        scene.play(bst.g.animate.change_layout("tree", root_vertex = node.val, layout_config = LAYOUT_CONFIG))
        scene.play(bst.g.vertices[node.val].animate.shift(3 * UP))

        # text = MathTex(f" curr = {node.val}", color = RED, font_size = 27)
        # scene.add(text)
        # text.move_to(bst.g.vertices[node.val].get_center() + RIGHT)
        # scene.play(circle.animate.move_to(bst.g.vertices[node.val].get_center()))
        # scene.wait()
        # scene.remove(text)

    elif (direction == 'L'):
        bst.g._add_vertex(node.val, vertex_config = VERTEX_CONF, label = True, position = bst.g.vertices[parent.val].get_center())
        nodes.add(node.val)

        scene.play(bst.g.vertices[node.val].animate.shift((factor * LEFT) + DOWN))
        # scene.play(circle.animate.move_to(bst.g.vertices[node.val].get_center()))

        # scene.remove(text)
        
        # text = MathTex(f" curr = {node.val}", color = RED, font_size = 27)
        # text.move_to(bst.g.vertices[node.val].get_center() + RIGHT)

        bst.g._add_edge((parent.val, node.val))
        edges.add((parent.val, node.val))

        

        # scene.add(text)
        # scene.wait()
        # scene.remove(text)
    else:
        bst.g._add_vertex(node.val, vertex_config = VERTEX_CONF, label = True, position = bst.g.vertices[parent.val].get_center())
        nodes.add(node.val)

        scene.play(bst.g.vertices[node.val].animate.shift((factor * RIGHT) + DOWN))
        # scene.play(circle.animate.move_to(bst.g.vertices[node.val].get_center()))

        # scene.remove(text)


        # text = MathTex(f" curr = {node.val}", color = RED, font_size = 27)
        # text.move_to(bst.g.vertices[node.val].get_center() + RIGHT)

        bst.g._add_edge((parent.val, node.val))
        edges.add((parent.val, node.val))

        # scene.add(text)
        # scene.wait()
        # scene.remove(text)
    scene.remove(circle)
    

def animateTraverse(scene, bst, node, circle, text, parent):
        if (parent != None):
            bst.g.edges[(parent.val, node.val)].set_color(RED)

        text = MathTex(f" curr = {node.val}", color = RED, font_size = 23)
        scene.add(text)
        shift = RIGHT + (0.015 * UP)
        if (node.val < 0):
            shift = 1.05 * RIGHT
        text.move_to(bst.g.vertices[node.val].get_center() + shift)
        scene.play(circle.animate.move_to(bst.g.vertices[node.val].get_center()))
        scene.wait()
        bst.g.vertices[node.val].stroke_color = RED

        scene.remove(text)
        
        
#Implement Tomorrow
def animateDelete(scene, node, parent, edges, nodes):
    pass


def shiftTreeAnimate(scene, bst, node, shift, direction):
    if (direction == 'L'):
        scene.play(bst.g.vertices[node.val].animate.shift(shift * LEFT))
    elif (direction == 'R'):
        scene.play(bst.g.vertices[node.val].animate.shift(shift * RIGHT))
     