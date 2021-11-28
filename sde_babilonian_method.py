from math import *
from manim import *
from manim.utils import scale, tex_templates
from numpy import array, left_shift

class MainFunction(MovingCameraScene):
    def construct(self):
        mt = TexTemplate()
        mt.add_to_preamble(r"\usepackage{mathrsfs, amsmath}")

        eq1 = MathTex("x^2-","4x","+","3", tex_template=mt, font_size=40)
        eq0 = MathTex(r'= 0', font_size = 40).move_to(RIGHT*1.1)
        t1 = Tex(r'\text{?}').move_to(RIGHT*1.75)
        t2 = Tex(r'\text{¿}').move_to(LEFT*1.75)
        
        self.play(Write(eq1))
        self.play(eq1.animate.shift(LEFT*0.4))
        self.play(Write(eq0), Write(t1), Write(t2))
        self.wait(0.5)

        ax = Axes(
            x_range=[-1,5,1],
            y_range=[-2,8,2],
            tips=False,
            axis_config={"include_numbers":True}
        )

        graph = ax.plot(lambda x: x**2-4*x+3, x_range=[-1,5],use_smoothing=True).set_color_by_gradient([YELLOW,PINK,PURPLE])
        
        G = VGroup(ax,graph).scale(0.5)
        d1 = Dot(ax.i2gp(1, graph))
        d2 = Dot(ax.i2gp(3, graph))

        gEq = VGroup(eq1,eq0,t1,t2)
        self.play(gEq.animate.shift(UP*2.5))
        self.play(Write(ax),FadeOut(t1), FadeOut(t2))
        self.play(Create(graph),rate_func=rate_functions.smooth)
        self.play(Write(d1), Write(d2))

        ar1 = Arrow(stroke_width=3, max_tip_length_to_length_ratio=0.1).rotate(-PI/2).scale(0.5).move_to(d1.get_center())
        ar2 = Arrow(stroke_width=3, max_tip_length_to_length_ratio=0.1).rotate(-PI/2).scale(0.5).move_to(d2.get_center())

        ar1.shift(UP*0.6)
        ar2.shift(UP*0.6)

        self.play(Write(ar1), Write(ar2))
        self.wait()

        VG = VGroup(ax,graph,d1,d2,ar1,ar2)
        self.play(FadeOut(eq0), eq1.animate.shift(RIGHT*0.4), FadeOut(VG))
        
        eq2 = MathTex(r'x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}', tex_template=mt, font_size=55)
        self.play(Write(eq2))
        self.wait(0.5)

        rf1 = ImageMobject("media/images/sde/rf.png").move_to(RIGHT*3.3).scale(0.7)
        rf2 = ImageMobject("media/images/sde/rf.png").move_to(LEFT*3).scale(0.7)

        cross = Cross(eq2).set_color(PURE_RED)

        self.play(eq2.animate.set_color(RED),Write(cross), FadeIn(rf1), FadeIn(rf2))
        self.wait(0.5)
        self.play(Uncreate(cross), Unwrite(eq2), FadeOut(rf1), FadeOut(rf2), run_time=1)

        eq3 = MathTex(r'= (x - x_1)(x - x_2)', font_size = 40).move_to(UP*2.45,LEFT*0.2).set_color(YELLOW)
        eq4 = MathTex(r'= x^2 - x x_1 - x x_2 + x_1 x_2').move_to(UP*1.75,LEFT*0.2).set_color(YELLOW)
        eq5 = MathTex("= x^2 - ","(x_1+x_2)x","+","x_1 x_2").move_to(UP*1.05,LEFT*0.2).set_color(YELLOW)

        self.play(eq1.animate.shift(LEFT*1.2))
        self.play(Write(eq3))

        self.wait(0.5)
        self.play(TransformMatchingTex(eq3.copy(),eq4, transform_mismatches=True), eq3.animate.set_color(WHITE))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq4.copy(),eq5, transform_mismatches=True, key_map={"-":"-", "x x_1":"(x_1+x_2)x", "x x_2":")x"}), eq4.animate.set_color(WHITE))
        self.wait(0.5)
        self.play(FadeOut(eq3),FadeOut(eq4), eq5.animate.shift(UP*1.45).set_color(WHITE))
        self.wait(0.5)


        feqGroup = VGroup(eq1,eq5)
        self.play(feqGroup.animate.shift(LEFT))

        rec1 = SurroundingRectangle(eq1[1]).set_color_by_gradient([ORANGE,PINK,PURPLE])
        rec2 = SurroundingRectangle(eq5[1]).set_color_by_gradient([ORANGE,PINK,PURPLE])

        rec3 = SurroundingRectangle(eq1[3]).set_color_by_gradient([GREEN,BLUE_C])
        rec4 = SurroundingRectangle(eq5[3], buff=.2).set_color_by_gradient([GREEN,BLUE_C])
        
        self.play(Write(rec1))
        self.play(ReplacementTransform(rec1.copy(),rec2))

        self.play(Write(rec3))
        self.play(eq5[2].animate.set_scale(0.8),ReplacementTransform(rec3.copy(),rec4))

        #seg1 = Line(d1.get_center(), d2.get_center()).set_color_by_gradient(GREEN,BLUE)
        # circumflejo = Brace(seg1)

        self.wait(2)
