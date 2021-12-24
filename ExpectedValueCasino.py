from math import *
from os import write
from manim import *
from numpy import array, left_shift

class MainFunction(MovingCameraScene):
    def construct(self):

        fst = 30
        fs = 25

        # Jugadas:
        ci = Tex(r'\underline{Tipo de Apuesta:}', font_size=fst).move_to(UP*0.55*5)
        c0 = Tex(r'Rojo / Negro', font_size=fs).move_to(UP*0.55*4)
        c1 = Tex(r'Par / Impar', font_size=fs).move_to(UP*0.55*3)
        c2 = Tex(r' Falta (1-18) / Pasa (19-36)', font_size=fs).move_to(UP*0.55*2)
        c3 = Tex(r'Doble Docena / Doble Columna', font_size=fs).move_to(UP*0.55*1)
        c4 = Tex(r'Docena / Columna', font_size=fs).move_to(UP*0.55*0)
        c5 = Tex(r'Seisena', font_size=fs).move_to(DOWN*0.55)
        c6 = Tex(r'Cuadro (4 números) / Esquina (0-3)', font_size=fs).move_to(DOWN*0.55*2)
        c7 = Tex(r'Transversal (Línea)', font_size=fs).move_to(DOWN*0.55*3)
        c8 = Tex(r'Caballo (2 números)', font_size=fs).move_to(DOWN*0.55*4)
        c9 = Tex(r'Pleno (1 número)', font_size=fs).move_to(DOWN*0.55*5)

        # G/P:
        gi = Tex(r'\underline{G/P:}', font_size=fst).move_to(UP*0.55*5)
        g0 = Tex(r'1:1', font_size=fs).move_to(UP*0.55*4)
        g1 = Tex(r'1:1', font_size=fs).move_to(UP*0.55*3)
        g2 = Tex(r'1:1', font_size=fs).move_to(UP*0.55*2)
        g3 = Tex(r'0.5:1', font_size=fs).move_to(UP*0.55*1)
        g4 = Tex(r'2:1', font_size=fs).move_to(UP*0.55*0)
        g5 = Tex(r'5:1', font_size=fs).move_to(DOWN*0.55)
        g6 = Tex(r'8:1', font_size=fs).move_to(DOWN*0.55*2)
        g7 = Tex(r'11:1', font_size=fs).move_to(DOWN*0.55*3)
        g8 = Tex(r'17:1', font_size=fs).move_to(DOWN*0.55*4)
        g9 = Tex(r'35:1', font_size=fs).move_to(DOWN*0.55*5)

        # Prob. Proffit:
        pi = Tex(r'\underline{Probabilidad de Ganar:}', font_size=fst).move_to(UP*0.55*5)
        p0 = Tex(r'18/37 = 48.6\%', font_size=fs).move_to(UP*0.55*4)
        p1 = Tex(r'18/37 = 48.6\%', font_size=fs).move_to(UP*0.55*3)
        p2 = Tex(r'18/37 = 48.6\%', font_size=fs).move_to(UP*0.55*2)
        p3 = Tex(r'24/37 = 64.8\%', font_size=fs).move_to(UP*0.55*1)
        p4 = Tex(r'12/37 = 32.4\%', font_size=fs).move_to(UP*0.55*0)
        p5 = Tex(r'6/37 = 16.2\%', font_size=fs).move_to(DOWN*0.55)
        p6 = Tex(r'4/37 = 10.8\%', font_size=fs).move_to(DOWN*0.55*2)
        p7 = Tex(r'3/37 = 8.1\%', font_size=fs).move_to(DOWN*0.55*3)
        p8 = Tex(r'2/37 = 5.4\%', font_size=fs).move_to(DOWN*0.55*4)
        p9 = Tex(r'1/37 = 2.7\%', font_size=fs).move_to(DOWN*0.55*5)

        # Esperanza matemática:
        ei = Tex(r'\underline{$\mathbb{E}[X]:$}', font_size=fst).move_to(UP*0.55*5)
        e0 = Tex(r'-0.028', font_size=fs).move_to(UP*0.55*4).set_color_by_gradient([PURE_RED,RED_C])
        e1 = Tex(r'-0.028', font_size=fs).move_to(UP*0.55*3).set_color_by_gradient([PURE_RED,RED_C])
        e2 = Tex(r'-0.028', font_size=fs).move_to(UP*0.55*2).set_color_by_gradient([PURE_RED,RED_C])
        e3 = Tex(r'-0.028', font_size=fs).move_to(UP*0.55*1).set_color_by_gradient([PURE_RED,RED_C])
        e4 = Tex(r'-0.028', font_size=fs).move_to(UP*0.55*0).set_color_by_gradient([PURE_RED,RED_C])
        e5 = Tex(r'-0.028', font_size=fs).move_to(DOWN*0.55).set_color_by_gradient([PURE_RED,RED_C])
        e6 = Tex(r'-0.028', font_size=fs).move_to(DOWN*0.55*2).set_color_by_gradient([PURE_RED,RED_C])
        e7 = Tex(r'-0.028', font_size=fs).move_to(DOWN*0.55*3).set_color_by_gradient([PURE_RED,RED_C])
        e8 = Tex(r'-0.028', font_size=fs).move_to(DOWN*0.55*4).set_color_by_gradient([PURE_RED,RED_C])
        e9 = Tex(r'-0.028', font_size=fs).move_to(DOWN*0.55*5).set_color_by_gradient([PURE_RED,RED_C])

        vgc = VGroup(ci,c0,c1,c2,c3,c4,c5,c6,c7,c8,c9)
        vgg = VGroup(gi,g0,g1,g2,g3,g4,g5,g6,g7,g8,g9)
        vgp = VGroup(pi,p0,p1,p2,p3,p4,p5,p6,p7,p8,p9).move_to(RIGHT)
        vge = VGroup(ei,e0,e1,e2,e3,e4,e5,e6,e7,e8,e9).move_to(RIGHT*4)
        vgtot = VGroup(vgc,vgp,vgg, vge)

        self.play(Write(vgc))
        self.play(vgc.animate.shift(LEFT*4))

        self.play(Write(vgg))
        self.play(vgg.animate.shift(LEFT))
    
        self.play(Write(vgp))
        self.play(vgp.animate.shift(RIGHT*0.5))

        self.play(Write(vge))

        sr = SurroundingRectangle(vgtot, buff=0.5).set_color_by_gradient([RED,PINK])
        self.play(Write(sr))

        self.wait(5)
