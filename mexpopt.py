from math import *
from os import write
from manim import *
from numpy import array, left_shift

class MainFunction(MovingCameraScene):
    def construct(self):

        v = Tex(r'Nuestra estrategia será ',r'vender',r' (cubiertos) las opciones con una probabilidad de expirar ',r'30\% ITM $(\Delta \approx .30)$',r' ${} \implies {}$',r' 70\% OTM ', r' a 45 días de expiración.', font_size=35)
        v[1].set_color_by_gradient([RED,PINK])
        v[2].set_color_by_gradient([ORANGE,YELLOW])
        #v[5].set_color_by_gradient([PINK,PURPLE])
        p = Tex(r'Probabilidad de Ganar: ',r'70\%',r'\\Probabilidad de Perder: ',r'30\%', font_size=35).move_to(DOWN*0.3)

        p[1].set_color_by_gradient([PURE_GREEN,GREEN_C])
        p[3].set_color_by_gradient([PURE_RED,RED_C])

        self.play(Write(v))
        self.play(v.animate.shift(UP*2.5))
        self.play(Write(p))
        self.play(p.animate.shift(UP*1.5))

        eq = MathTex(r'\mathbb{E}[x] > 0 \quad \iff \quad  0 < ', r'\text{?}_G', r' \cdot ', r'0.7', r' - ', r'\text{?}_P', r' \cdot ', r'0.3', font_size=35)
        eq[1].set_color_by_gradient([YELLOW, GREEN_C])
        eq[3].set_color_by_gradient([GREEN_C, BLUE_C])
        eq[5].set_color_by_gradient([YELLOW, RED_C])
        eq[7].set_color_by_gradient([ORANGE,PINK])

        self.play(Write(eq))

        eq2 = MathTex(r'\mathbb{E}[x] > 0 \quad \iff \quad 0 < ', r'1', r' \cdot ', r'0.7', r' - ', r'2', r' \cdot ', r'0.3', font_size=35)
        eq2[1].set_color_by_gradient([YELLOW, GREEN_C])
        eq2[3].set_color_by_gradient([GREEN_C, BLUE_C])
        eq2[5].set_color_by_gradient([YELLOW, RED_C])
        eq2[7].set_color_by_gradient([ORANGE,PINK])

        self.play(TransformMatchingTex(eq,eq2,transform_mismatches=True))
        self.play(Circumscribe(eq2[1], color=PURE_GREEN))
        self.play(Circumscribe(eq2[5], color=PURE_RED))

        tp = Tex(r'Take Proffit: ',r'100\$', r'$\, \cdot \, 0.7 = $',r'$70\$$', font_size=35).move_to(DOWN)
        tp[1].set_color_by_gradient([PURE_GREEN,GREEN_C])
        sl = Tex(r'Stop Loss: ',r'200\$', r'$\, \cdot \, 0.3 = $',r'$60\$$', font_size=35).move_to(DOWN*1.5)
        sl[1].set_color_by_gradient([PURE_RED,RED_C])

        gg = VGroup(tp, sl)

        self.play(Write(tp), Write(sl))

        self.play(
            tp[1].animate.set_color(WHITE),
            tp[3].animate.set_color_by_gradient([PURE_GREEN, GREEN_C]),
            sl[1].animate.set_color(WHITE),
            sl[3].animate.set_color_by_gradient([PURE_RED, RED_C])
        )

        br = Brace(gg,direction=[1,0,0])

        self.play(Write(br))

        re = MathTex(r'70\$-60\$ = ',r'10\$', font_size=35).move_to(br.get_center())
        re.shift(RIGHT*1.7)

        self.play(Write(re))
        self.play(
            Circumscribe(re[1], color=GREEN_C), 
            re[1].animate.set_color_by_gradient([PURE_GREEN,GREEN_C]),
            tp[3].animate.set_color(WHITE),    
            sl[3].animate.set_color(WHITE)
        )

        
        self.wait(5)
