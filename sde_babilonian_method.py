from math import *
from os import write
from manim import *
from numpy import array, left_shift

class MainFunction(MovingCameraScene):
    def construct(self):
        eq1 = MathTex("x^2-","4x","+","3", font_size=40)
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
        
        eq2 = MathTex(r'x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}', font_size=55)
        self.play(Write(eq2))
        self.wait(0.5)

        #rf1 = ImageMobject("media/images/sde/rf.png").move_to(RIGHT*3.3).scale(0.7)
        #rf2 = ImageMobject("media/images/sde/rf.png").move_to(LEFT*3).scale(0.7)

        cross = Cross(eq2).set_color(PURE_RED)

        self.play(eq2.animate.set_color(RED),Write(cross))
        self.wait(0.5)
        self.play(Uncreate(cross), Unwrite(eq2), run_time=1)

        eq3 = MathTex(r'= (x - x_1)(x - x_2)', font_size = 40).move_to(UP*2.45,LEFT*0.2).set_color(YELLOW)
        eq4 = MathTex(r'= x^2 - x x_1 - x x_2 + x_1 x_2').move_to(UP*1.75,LEFT*0.2).set_color(YELLOW)
        eq5 = MathTex("= x^2 - ","(x_1+x_2)x","+","x_1 x_2").move_to(UP*1.05,LEFT*0.2).set_color(YELLOW)

        self.play(eq1.animate.shift(LEFT*1.2))
        self.play(Write(eq3))

        self.wait(0.5)
        self.play(TransformMatchingTex(eq3.copy(),eq4, transform_mismatches=True), eq3.animate.set_color(WHITE))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq4.copy(),eq5, transform_mismatches=True, key_map={"x^2":"x^2","-":"-", "x x_1":"(x_1+x_2)x", "x x_2":")x"}), eq4.animate.set_color(WHITE))
        self.wait(0.5)
        self.play(FadeOut(eq3),FadeOut(eq4), eq5.animate.shift(UP*1.45).set_color(WHITE))
        self.wait(0.5)


        feqGroup = VGroup(eq1,eq5)
        self.play(feqGroup.animate.shift(UP*0.5,LEFT*1.5))

        rec1 = SurroundingRectangle(eq1[1]).set_color_by_gradient([ORANGE,PINK,PURPLE])
        rec2 = SurroundingRectangle(eq5[1]).set_color_by_gradient([ORANGE,PINK,PURPLE])
        rec3 = SurroundingRectangle(eq1[3]).set_color_by_gradient([GREEN_C,BLUE_C])
        rec4 = SurroundingRectangle(eq5[3]).set_color_by_gradient([GREEN_C,BLUE_C])

        self.play(Write(rec1))
        self.play(ReplacementTransform(rec1.copy(),rec2))

        self.play(Write(rec3))
        self.play(ReplacementTransform(rec3.copy(),rec4))

        suma = MathTex("Sum: ", "x_1 + x_2 = 4", "midpoint(x_1,x_2) = \dfrac{x_1 + x_2}{2} = 2", font_size=30)
        suma[0].set_color_by_gradient([ORANGE,PINK,PURPLE])
        suma[0].move_to(UP*1.5)
        suma[0].shift(LEFT*3.5)

        prod = MathTex("Product: ","x_1 \cdot x_2"," = 3", font_size=30).move_to(UP)
        prod[0].set_color_by_gradient([GREEN_C,BLUE_C])

        d3 = Dot().set_color(PURPLE_C)
        d4 = Dot().set_color(ORANGE)
        mp = Dot().move_to(DOWN*2)

        u1 = MathTex(r"u", font_size = 25).move_to(DOWN*1.2)
        u1.shift(LEFT)
        u2 = MathTex(r"u", font_size=25).move_to(DOWN*1.2)
        u2.shift(RIGHT)

        iff = MathTex("{} \iff {}").move_to(UP*1.5)
        iff.shift(LEFT*0.5)

        self.play(Write(suma[0]))

        suma[1].move_to(UP*1.5)
        suma[1].shift(LEFT*2)

        suma[2].move_to(UP*1.5)
        suma[2].shift(RIGHT*2.3)

        self.play(Write(suma[1]), Write(iff), Write(suma[2]))

        self.play(Write(d3), d3.animate.shift(LEFT*2, DOWN*2)) 
        self.play(Write(d4), d4.animate.shift(RIGHT*2, DOWN*2)) 

        x1 = MathTex(r"x_1", font_size = 20).move_to(d3.get_center())
        x1.shift(DOWN*0.3)
        x2 = MathTex(r"x_2", font_size = 20).move_to(d4.get_center())
        x2.shift(DOWN*0.3)

        mpx = MathTex(r"2", font_size = 25).move_to(mp.get_center())
        mpx.shift(DOWN*0.3)

        self.play(Write(x1), Write(x2))

        l2 = always_redraw(lambda:Line(d3,d4).set_color_by_gradient([ORANGE,PINK,PURPLE_C]))

        self.play(Create(l2), Write(mp),Write(mpx)) 

        l0 = always_redraw(lambda:Line(d3,mp).set_color_by_gradient([PINK,PURPLE_C]))
        l1 = always_redraw(lambda:Line(mp,d4).set_color_by_gradient([ORANGE,PINK]))

        b0 = always_redraw(lambda:Brace(l0,UP))
        b1 = always_redraw(lambda:Brace(l1,UP))

        self.play(Write(b0), Write(b1), Write(u1), Write(u2), Write(l0), Write(l1))
        self.play(d3.animate.shift(LEFT), u1.animate.shift(LEFT*0.5), d4.animate.shift(RIGHT),u2.animate.shift(RIGHT*0.5), x1.animate.shift(LEFT), x2.animate.shift(RIGHT))
        self.wait(0.25)
        self.play(d3.animate.shift(RIGHT), u1.animate.shift(RIGHT*0.5), d4.animate.shift(LEFT),u2.animate.shift(LEFT*0.5), x1.animate.shift(RIGHT), x2.animate.shift(LEFT))

        equ1 = MathTex("x_1 = 2 - u", font_size=30)
        equ1.move_to(RIGHT*3.5)
        equ1.shift(UP*0.2)

        equ2 = MathTex("x_2 = 2 + u", font_size=30)
        equ2.move_to(RIGHT*3.5)
        equ2.shift(DOWN*0.3)
 
        gd = VGroup(d3,d4,u1,u2,x1,x2,mpx,mp)
        self.play(gd.animate.move_to(UP*0.1))

        self.play(Write(equ1), Write(equ2))
        gequs = VGroup(equ1,equ2)

        sol0 = MathTex(r"= 3", font_size=30)
        sol0.move_to(DOWN*1.7)
        sol0.shift(RIGHT*0.4)

        sol1 = MathTex(r"(2-u)(2+u)", font_size=30)
        sol1.move_to(DOWN*1.7)
        sol1.shift(LEFT)

        sol2 = MathTex(r"4-u^2 = 3", font_size=30)
        sol2.move_to(LEFT*0.1)
        sol2.shift(DOWN*2.2)

        sol3 = MathTex(r"4-3 = u^2", font_size=30)
        sol3.move_to(LEFT*0.1)
        sol3.shift(DOWN*2.7)

        sol4 = MathTex(r"u = \pm \sqrt{1} = \pm 1",font_size = 30)
        sol4.move_to(LEFT*0.1)
        sol4.shift(DOWN*3.2)

        sol_final = MathTex(r" \mid \mid u \mid \mid = 1",font_size = 30)
        sol_final.move_to(DOWN*1.5)

        prod[0].shift(LEFT*2.8, DOWN*2)
        prod[1].shift(LEFT*2.5, DOWN*2)
        prod[2].shift(LEFT*2.4, DOWN*2)

        self.play(Write(prod[0]), Write(prod[1]), Write(prod[2]))

        seq = SurroundingRectangle(gequs)
        sprod = SurroundingRectangle(prod[1])
        snext = SurroundingRectangle(sol1[0])

        self.play(Write(seq))
        self.play(ReplacementTransform(seq,sprod))

        #sol0.move_to()

        self.play(ReplacementTransform(sprod,snext),Write(sol1),Write(sol0))
        self.play(Uncreate(snext), sol1[0].animate.set_color(YELLOW_C))
        self.play(TransformMatchingTex(sol1.copy(),sol2, transform_mismatches=True), sol1[0].animate.set_color(WHITE))
        self.wait(0.5)
        self.play(TransformMatchingTex(sol2.copy(),sol3, transform_mismatches=True))
        self.wait(0.5)
        self.play(TransformMatchingTex(sol3.copy(),sol4, transform_mismatches=True))
        self.wait(0.5)

        suresult = SurroundingRectangle(sol4).set_color([BLUE_C])
        self.play(Create(suresult))
        self.wait(0.25)

        self.play(Uncreate(suresult),FadeOut(sol0),FadeOut(sol1),FadeOut(sol2),FadeOut(sol3))
        self.play(sol4.animate.shift(UP*1.5))

        self.play(TransformMatchingTex(sol4,sol_final, transform_mismatches=True))
        sol4.remove()
        suresult.remove()

        final_u1 = MathTex(r"1", font_size = 25).move_to(u1.get_center())
        final_u2 = MathTex(r"1", font_size = 25).move_to(u2.get_center())

        self.play(FadeOut(u1), FadeIn(final_u1), FadeOut(u2), FadeIn(final_u2))

        equ1_final = MathTex("x_1 = 2 - 1 = 1", font_size=30)
        equ1_final.shift(DOWN*2.3)

        equ2_final = MathTex("x_2 = 2 + 1 = 3", font_size=30)
        equ2_final.shift(DOWN*2.6)

        ff = MathTex("x_1 = 1", font_size=30)
        ff2 = MathTex("x_2 = 3", font_size=30)
        ff.shift(DOWN*3.2)
        ff2.shift(DOWN*3.6)

        ffg = VGroup(ff,ff2)

        ff_rec = always_redraw(lambda:SurroundingRectangle(ffg).set_color_by_gradient([ORANGE,PINK,PURPLE_C]))
        self.play(TransformMatchingTex(equ1.copy(),equ1_final, transform_mismatches=True),TransformMatchingTex(equ2.copy(),equ2_final, transform_mismatches=True))

        self.play(Write(ff),Write(ff2), Create(ff_rec))    

        FINALG = VGroup(eq2,eq5,iff,x1,x2,final_u1,final_u2,mpx,prod,suma,equ1,equ2,equ1_final,equ2_final,sol_final,rec1,rec2,rec3,rec4,d3,d4,mp,b0,b1,l1,l2,l0)
        self.play(FadeOut(FINALG))

        self.play(eq1.animate.shift(RIGHT*2.7), ffg.animate.shift(UP*5))
        self.play(Write(ax))
        self.play(Create(graph),Write(ar1), Write(ar2),Write(d1),Write(d2),rate_func=rate_functions.smooth)

        self.wait(2)
