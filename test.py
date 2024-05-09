from manim import *
from intro import playIntro


class construct(MovingCameraScene):
    DEPTH = 2
    CHILDREN_PER_VERTEX = 2
    LAYOUT_CONFIG = {"vertex_spacing": (0.001, 1)}
    VERTEX_CONF = {"radius": 0.35, "color": WHITE}

    # def expand_vertex(self, g, vertex_id: str, depth: int):
    #     new_vertices = [f"{vertex_id}/{i}" for i in range(self.CHILDREN_PER_VERTEX)]

    #     new_edges = [(vertex_id, child_id) for child_id in new_vertices]

    #     g.add_edges(*new_edges, vertex_config=self.VERTEX_CONF, positions={k: g.vertices[vertex_id].get_center() + 0.1 * DOWN for k in new_vertices})

    #     if depth < self.DEPTH:
    #         for child_id in new_vertices:
    #             self.expand_vertex(g, child_id, depth + 1)

    #     return g

    def construct(self):
        g = Graph([0], [], vertex_config=self.VERTEX_CONF, labels=True, layout_scale=0.5)
        
        self.add(g)
    

        self.play(g.animate.change_layout("tree", root_vertex=0, layout_config=self.LAYOUT_CONFIG))
        self.play(g.vertices[0].animate.shift(3 * UP))

        c = Circle(radius=.35)
        text = MathTex(f"curr = {0}", color=RED, font_size=25)
        self.add(text)

        text.move_to(g.vertices[0].get_center() + RIGHT)

        self.play(c.animate.move_to(g.vertices[0].get_center()))

        self.wait()

        g._add_vertex(1, vertex_config=self.VERTEX_CONF, label=True, position=g.vertices[0].get_center() + DOWN + 2 *LEFT)
        g._add_edge((0,1))

        self.remove(text)

        

        g._add_vertex(2, vertex_config=self.VERTEX_CONF, label=True, position=g.vertices[0].get_center() + DOWN + 2 * RIGHT)
        g._add_edge((0,2))

        g._add_vertex(3, vertex_config=self.VERTEX_CONF, label=True, position=g.vertices[1].get_center() + DOWN + LEFT)
        g._add_edge((1,3))

        g._add_vertex(4, vertex_config=self.VERTEX_CONF, label=True, position=g.vertices[1].get_center() + DOWN + RIGHT)
        g._add_edge((1,4))

        g._add_vertex(5, vertex_config=self.VERTEX_CONF, label=True, position=g.vertices[2].get_center() + DOWN + LEFT)
        g._add_edge((2,5))

        g._add_vertex(6, vertex_config=self.VERTEX_CONF, label=True, position=g.vertices[2].get_center() + DOWN + RIGHT)
        g._add_edge((2,6))

        self.wait(4)

        self.play(g.vertices[2].animate.shift(RIGHT))

        self.wait()

        self.wait()

        self.play(g.vertices[5].animate.shift(RIGHT))

        self.wait()

        self.play(g.vertices[6].animate.shift(RIGHT))

        # Single addition to node
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        g._add_vertex(7, vertex_config=self.VERTEX_CONF, label=True, position=g.vertices[5].get_center())

        self.play(g.vertices[7].animate.shift(LEFT + DOWN))
        self.play(c.animate.move_to(g.vertices[7].get_center()))

        if (text):
            self.remove(text)

        text = MathTex(f"curr = 7", color=RED, font_size=25)
        text.move_to(g.vertices[7].get_center() + RIGHT)

        g._add_edge((5,7))

        self.add(text)

        self.wait()
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        

        g._add_vertex(8, vertex_config=self.VERTEX_CONF, label=True, position=g.vertices[5].get_center())
     
        self.play(g.vertices[8].animate.shift(RIGHT + DOWN))
        self.play(c.animate.move_to(g.vertices[8].get_center()))
        self.remove(text)
        text = MathTex(f"curr = 8", color=RED, font_size=25)
        text.move_to(g.vertices[8].get_center() + RIGHT)
        g._add_edge((5,8))
        self.add(text)
        self.wait()

        self.play(g.vertices[1].animate.shift(LEFT))
        self.wait()

        self.play(g.vertices[3].animate.shift(LEFT))
        self.wait()

        self.play(g.vertices[4].animate.shift(LEFT))
        self.wait()

        g._add_vertex(9, vertex_config=self.VERTEX_CONF, label=True, position=g.vertices[3].get_center())

        self.play(g.vertices[9].animate.shift(LEFT + DOWN))
        self.play(c.animate.move_to(g.vertices[9].get_center()))
        self.remove(text)
        text = MathTex(f"curr = 9", color=RED, font_size=25)
        text.move_to(g.vertices[9].get_center() + RIGHT)
        g._add_edge((3,9))
        self.add(text)
        self.wait()

        g._add_vertex(10, vertex_config=self.VERTEX_CONF, label=True, position=g.vertices[3].get_center())

        self.play(g.vertices[10].animate.shift(RIGHT + DOWN))
        self.play(c.animate.move_to(g.vertices[10].get_center()))
        self.remove(text)
        text = MathTex(f"curr = 10", color=RED, font_size=25)
        text.move_to(g.vertices[10].get_center() + RIGHT)
        self.add(text)
        g._add_edge((3,10))
        self.remove(text)

        # Traverse Example
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        text = MathTex(f"curr = 0", color=RED, font_size=25)
        text.move_to(g.vertices[0].get_center() + RIGHT)
        self.add(text)
        self.play(c.animate.move_to(g.vertices[0].get_center()))
        self.wait()
        self.remove(text)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        text = MathTex(f"curr = 2", color=RED, font_size=25)
        text.move_to(g.vertices[2].get_center() + RIGHT)
        self.add(text)
        self.play(c.animate.move_to(g.vertices[2].get_center()))
        self.wait()
        self.remove(text)

        text = MathTex(f"curr = 5", color=RED, font_size=25)
        text.move_to(g.vertices[5].get_center() + RIGHT)
        self.add(text)
        self.play(c.animate.move_to(g.vertices[5].get_center()))
        self.wait()
        self.remove(text)

        text = MathTex(f"curr = 8", color=RED, font_size=25)
        text.move_to(g.vertices[8].get_center() + RIGHT)
        self.add(text)
        self.play(c.animate.move_to(g.vertices[8].get_center()))
        self.wait()

        self.remove(text)
        self.remove(c)      


        self.wait(3)

        self.remove(g)

        playIntro(self)

