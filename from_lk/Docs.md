# Manim Cheatsheet

## Mobject
###attributes (kwargs)
color color (default WHITE), dimension dim (default: 3), submobjects (default []),

###functions
remove()
show() -> creates image file
save_image(name) -> saves image
generate_target() -> makes copy of itself

###transformations
shift(vecs) -> applies vecs in succession (vector addition)
scale(scale_factor, about_edge, about_point) -> scales about centre, or about given point
rotate_about_origin(angle)
flip()

###positioning
center()
to_corner(point) -> moves to corner, default corners: DOWN + LEFT (DL), etc.
to_edge(point) -> same as to_corner(), default edges are UP, DOWN, LEFT, RIGHT, IN, OUT, etc.

## Animation
### creation animations
ShowCreation(mobj)
Uncreate(mobj)
DrawBorderThenFill(mobj)

##Example Scenes
```python
class Intro(Scene):

    def construct(self):
        self.intro()
        self.long_division()

    def intro(self):
        """Animates 2 Text objects, writes them to the screen, moves one up, and then fades both out."""
        title = TextMobject("Long Division")
        sub = TextMobject("You've been doing it wrong all along...")

        self.play(Write(title), run_time = 2)
        self.play(ApplyMethod(title.move_to, UP), run_time = 2)
        self.play(Write(sub), run_time = 2)

        self.wait()

        self.play(FadeOut(title), FadeOut(sub), run_time = 2)

class Play(Scene):
    def construct(self):
        c = Circle()
        e = Ellipse()
        r = Rectangle()
        a = Arc(angle = 1/4 * TAU)
        asec = AnnularSector()
        an = Annulus()
        t = Triangle()

        self.play(ShowCreation(c))

        group_a = VGroup(c, e, r, a)
        group_b = VGroup(asec, an, t)
        group_a.arrange(LEFT)
        self.play(FadeIn(group_a))
        self.play(FadeOut(group_a))
        self.play(FadeIn(group_b))
        self.play(FadeOut(group_b))

        l = Line()
        el = Elbow()
        ar = Arrow()
        v = Vector(direction = LEFT)

        lgroup = VGroup(l, el, ar, v)
        lgroup.arrange(DOWN)
        self.play(FadeIn(lgroup))
```
