from manim import *
from math import sqrt
from manim.utils import scale

class TestPrincipal(MovingCameraScene):
    def construct(self):
        delta(self)
        gamma(self)
        vega(self)
        theta(self)
        rho(self)

def delta(self):
    pass

def gamma(self):
    pass

def vega(self):
    pass

def rho(self):
    pass

def theta(self):
    # Old func: -(1/145)*(x**2)+100
    # New func: (100/sqrt(120))*sqrt(abs(x-120))

    self.camera.frame.save_state()
    
    # Define the axes and the function:
    ax = Axes(x_range=[0, 120, 30], y_range=[0, 100, 100], tips = False)
    graph = ax.plot(lambda x: (100/sqrt(120))*sqrt(abs(x-120)), color=WHITE, x_range=[0, 120])
    curve_1 = ax.plot(lambda x: (100/sqrt(120))*sqrt(abs(x-120)), x_range=[0, 120], color=WHITE)

    # Define the title:
    myTemplate = TexTemplate()
    myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
    tex = Tex(r'\underline{$\theta$ - Time decay:}', tex_template=myTemplate, font_size=40).next_to(curve_1, UP)

    # Define three vertical lines (Days remaining until expiration)
    line_1 = ax.get_vertical_line(ax.i2gp(30, curve_1), color=BLUE_C)
    line_2 = ax.get_vertical_line(ax.i2gp(60, curve_1), color=BLUE_C)
    line_3 = ax.get_vertical_line(ax.i2gp(90, curve_1), color=BLUE_C)

    # Define the dots:
    moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
    dot_1 = Dot(ax.i2gp(graph.t_min, graph))
    dot_2 = Dot(ax.i2gp(graph.t_max, graph))

    # We create and show a Vector Group with all our elements 
    # to be able to move it around the screen:
    theta = VGroup(tex, line_1, line_2, line_3, ax, graph, dot_1, dot_2, moving_dot)
    self.play(FadeIn(theta))

    # We zoom in into the orange dot:
    self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

    # Updater to follow the dot with the camera:
    def update_curve(mob):
        mob.move_to(moving_dot.get_center())

    # We follow the orange dot along the function and 
    # restore the camera to its original position:
    self.camera.frame.add_updater(update_curve)
    self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
    self.camera.frame.remove_updater(update_curve)
    self.play(Restore(self.camera.frame))
    self.wait(0.25)

    # We draw a frame around our VGroup:
    framebox1 = always_redraw(lambda: SurroundingRectangle(theta, buff = .1))
    self.play(Write(framebox1))

    # We move everything into the left down corner:
    self.play(theta.animate.scale(0.2).shift(LEFT*5.5,DOWN*3))
    self.wait(3) 

