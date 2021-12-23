from math import *
from os import write
from manim import *
from numpy import array, left_shift

class MainFunction(MovingCameraScene):
    def construct(self):

        ax = Axes(
            x_range=[-1.3,1.3,0.1],
            y_range=[-1.3,1.3,0.2],
            tips=False,
            axis_config={"include_numbers":True, "font_size":17}
        )

        func = ax.plot(lambda x: -x*(x-1)*(x+1)).set_color(YELLOW)

        self.play(Write(ax), Write(func))

        rec1 = ax.get_riemann_rectangles(func, x_range=[0.4, 0.7], dx=0.1, color=[ORANGE,PURPLE], stroke_width=0.01, fill_opacity=0.75)
        rec2 = ax.get_riemann_rectangles(func, x_range=[0.4, 0.7], dx=0.05, color=[ORANGE,PURPLE], stroke_width=0.01, fill_opacity=0.75)
        rec3 = ax.get_riemann_rectangles(func, x_range=[0.4, 0.7], dx=0.01, color=[ORANGE,PURPLE], stroke_width=0.01, fill_opacity=0.75)
        rec4 = ax.get_riemann_rectangles(func, x_range=[0.4, 0.7], dx=0.01, color=[ORANGE,PURPLE], stroke_width=0.01, fill_opacity=0.75)
        int = ax.get_area(func, [0.4, 0.7], color=[ORANGE,PURPLE], stroke_width=0.1, opacity=0.75)

        s = MathTex(r'\sum_{k=1}^{n} ',r'f(t_k)',r'(x_k - x_{k-1})',r'; \quad x_{k-1} \leqslant t_k \leqslant x_k', font_size=30).shift(RIGHT*4,UP*3)
        s1 = MathTex(r'\int_{a}^{b} f(x)dx; \quad [a,b] \subset \mathbb{R}^{1}', font_size=30).shift(RIGHT*3,UP*3)
        s2 = MathTex(r'\int_{0.4}^{0.7} f(x)dx', font_size=30).shift(RIGHT*3,DOWN*2)
        s3 = MathTex(r'\int_{0.4}^{0.7} -',r'x',r'(x+1)',r'(x-1)',r'dx \approx 0.11 ', font_size=30).shift(RIGHT*3,DOWN*2)

        gc = VGroup(s[1],s[2])

        s[1].set_color_by_gradient([GREEN_C, BLUE_C])
        s[2].set_color_by_gradient([ORANGE, PURPLE])

        self.play(Write(rec1))
        self.play(Write(s), run_time=2)
        self.wait()

        self.play(rec1[0].animate.scale(3))

        br1 = Brace(rec1[0]).set_color_by_gradient([ORANGE, PURPLE])
        br2 = Brace(rec1[0], direction=[-1,0,0]).set_color_by_gradient([GREEN_C, BLUE_C])

        t1 = MathTex(r'x_k - x_{k-1}', font_size=30).move_to(br1.get_center()).set_color_by_gradient([ORANGE, PURPLE])
        t1.shift(DOWN*0.5)

        t2 = MathTex(r'f(t_k)', font_size=35).move_to(br2.get_center()).set_color_by_gradient([GREEN_C, BLUE_C])
        t2.shift(LEFT*0.7)

        sr = SurroundingRectangle(t2, fill_color=BLACK, fill_opacity=0.95, stroke_width=0, stroke_color=BLACK)

        self.play(Write(br1))
        self.play(Write(t1))

        self.play(ApplyWave(s[2]), run_time=2)
        self.play(ApplyWave(t1))

        self.play(Write(br2))
        self.play(Write(sr),Write(t2))

        self.play(ApplyWave(s[1]))
        self.play(ApplyWave(t2))

        self.wait(2)
        
        self.play(Circumscribe(gc, color=BLUE_C))

        self.wait()

        self.play(FadeOut(br1),FadeOut(br2),FadeOut(t1),FadeOut(t2),FadeOut(sr))

        self.play(rec1[0].animate.scale(1/3))

        self.wait()

        self.play(Write(rec2), FadeOut(rec1))
        self.wait()
        self.play(Write(rec3), FadeOut(rec2))
        self.wait()
        self.play(Write(rec4), FadeOut(rec3))
        self.wait()
        self.play(Write(int), FadeOut(rec4), TransformMatchingTex(s,s1,transform_mismatches=True))
        self.wait()
        self.play(TransformMatchingTex(s1.copy(),s2,transform_mismatches=True))
        self.wait()
        self.play(TransformMatchingTex(s2,s3,transform_mismatches=True))

        d1 = Dot(ax.c2p(0,0)).set_color(PINK)
        d2 = Dot(ax.c2p(-1,0)).set_color(PURPLE)
        d3 = Dot(ax.c2p(1,0)).set_color(ORANGE)
     

        self.play(Write(d1))
        self.play(s3[1].animate.set_color(PINK))
        self.play(Transform(d1.copy(),s3[1]))
        self.wait()

        self.play(Write(d2))
        self.play(s3[2].animate.set_color(PURPLE))
        self.play(Transform(d2.copy(),s3[2]))
        self.wait()

        self.play(Write(d3))
        self.play(s3[3].animate.set_color(ORANGE))
        self.play(Transform(d3.copy(),s3[3]))

        self.wait(5)
