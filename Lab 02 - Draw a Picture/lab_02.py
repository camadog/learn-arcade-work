# Well, Excuuuuse me princes...
import arcade

arcade.open_window(440, 440, "sm64")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()

# *** draw ***

RED  = (184, 0, 0)
BLUE = (32, 77, 145)
SKIN = (182, 162, 102)
DARK_SKIN = (170, 150, 90)
LIGHT_RED  = (184, 10, 15)

# *Head (maybe that would be it)

# Cap
arcade.draw_polygon_filled((
        (92,  (440 - 182)),
        (42,  (440 - 148)),
        (76,  (440 - 114)),
        (100, (440 - 110)),
        (94,  (440 - 60)),
        (136, (440 - 6)),
        (248, (440 - 12)),
        (366, (440 - 94)),
        (392, (440 - 180)),
        (380, (440 - 210)),
        (348, (440 - 194)),
        (296, (440 - 148)),
        (180, (440 - 124)),
        (100, (440 - 145)),
        (92,  (440 - 182))
    ), RED)
# Cap Detail... An arc just for practice...
arcade.draw_arc_filled(150, (440 - 98), 100, 120, arcade.csscolor.WHITE, 5, 192)
arcade.draw_polygon_filled((
        (105,  (440 - 105)),
        (122,  (440 - 55)),
        (132,  (440 - 51)),
        (135,  (440 - 62)),
        (137,  (440 - 62)),
        (144,  (440 - 44)),
        (155,  (440 - 40)),
        (182,  (440 - 78)),
        (160,  (440 - 94)),
        (150,  (440 - 60)),
        (142,  (440 - 78)),
        (130,  (440 - 80)),
        (128,  (440 - 70)),
        (124,  (440 - 74)),
        (118,  (440 - 106)),
        (105,  (440 - 105))
    ), LIGHT_RED)

# Head
arcade.draw_polygon_filled((
        (92,  (440 - 182)),
        (100, (440 - 145)),
        (180, (440 - 124)),
        (296, (440 - 148)),
        (348, (440 - 194)),
        (392, (440 - 214)),
        (390, (440 - 270)),
        (338, (440 - 300)),
        (310, (440 - 340)),
        (240, (440 - 365)),
        (182, (440 - 380)),
        (138, (440 - 370)),
        (95,  (440 - 328)),
        (92,  (440 - 182))
    ), SKIN)


# Eyebrows ????
# arcade.draw_arc_filled(center_x, center_y, width, height, color, start_angle, end_angle)
# Left
arcade.draw_arc_filled(110, (440 - 155), 25, 18, arcade.csscolor.BLACK, 0, 180)
arcade.draw_arc_filled(110, (440 - 162), 25, 18, SKIN, 0, 180)
# Right
arcade.draw_arc_filled(175, (440 - 150), 48, 30, arcade.csscolor.BLACK, 0, 180, 20)
arcade.draw_arc_filled(175, (440 - 160), 60, 35, SKIN, 0, 180, 20)

# Eyes
# arcade.draw_ellipse_filled(center_x, center_y, width, height, color)
# Left
arcade.draw_ellipse_filled(112, (440 - 198), 30, 76, arcade.csscolor.WHITE)
arcade.draw_ellipse_filled(118, (440 - 198), 14, 72, BLUE)
arcade.draw_ellipse_filled(120, (440 - 198), 12, 55, arcade.csscolor.BLACK)
arcade.draw_ellipse_filled(122, (440 - 198), 6, 16, arcade.csscolor.WHITE)
# Right
arcade.draw_ellipse_filled(170, (440 - 192), 58, 82, arcade.csscolor.WHITE)
arcade.draw_ellipse_filled(160, (440 - 192), 32, 72, BLUE)
arcade.draw_ellipse_filled(155, (440 - 192), 20, 55, arcade.csscolor.BLACK)
arcade.draw_ellipse_filled(150, (440 - 192), 10, 16, arcade.csscolor.WHITE)

# Hair
# Patilla
arcade.draw_polygon_filled((
        (346, (440 - 192)),
        (334, (440 - 235)),
        (313, (440 - 230)),
        (302, (440 - 210)),
        (326, (440 - 188)),
        (328, (440 - 176)),
        (346, (440 - 192))
    ), arcade.csscolor.SIENNA)
arcade.draw_arc_filled(316, (440 - 224), 42, 42, arcade.csscolor.SIENNA, 0, 180, 148)
arcade.draw_arc_filled(310, (440 - 206), 15, 15, arcade.csscolor.SIENNA, 0, 180, 45)

# Mustache
arcade.draw_polygon_filled((
        (165, (440 - 270)),
        (224, (440 - 236)),
        (224, (440 - 274)),
        (182, (440 - 312)),
        (135, (440 - 300)),
        (165, (440 - 270))
    ), arcade.csscolor.BLACK)

arcade.draw_arc_filled(106, (440 - 328), 7, 7, arcade.csscolor.BLACK, 0, 180, 180)
arcade.draw_arc_filled(126, (440 - 322), 10, 10, arcade.csscolor.BLACK, 0, 180, 180)

arcade.draw_arc_filled(160, (440 - 302), 30, 30, arcade.csscolor.BLACK, 0, 180, 180)
arcade.draw_arc_filled(185, (440 - 300), 30, 35, arcade.csscolor.BLACK, 0, 180, 200)
arcade.draw_arc_filled(206, (440 - 290), 25, 30, arcade.csscolor.BLACK, 0, 180, 220)
arcade.draw_arc_filled(218, (440 - 260), 50, 50, arcade.csscolor.BLACK, 0, 180, 255)
# fix
arcade.draw_arc_filled(194, (440 - 250), 60, 20, SKIN, 0, 180, 205)

# Mullet
arcade.draw_polygon_filled((
        (338, (440 - 300)),
        (310, (440 - 340)),
        (345, (440 - 344)),
        (375, (440 - 316)),
        (360, (440 - 287)),
        (338, (440 - 300))
    ), arcade.csscolor.SIENNA)

# Nose
arcade.draw_polygon_filled((
        (38,   (440 - 236)),
        (74,   (440 - 206)),
        (145,  (440 - 224)),
        (166,  (440 - 250)),
        (164,  (440 - 300)),
        (116,  (440 - 330)),
        (78,   (440 - 330)),
        (42,   (440 - 308)),
        (34,   (440 - 270)),
        (38,   (440 - 236))
    ), SKIN)
arcade.draw_polygon_outline((
        (38,   (440 - 236)),
        (74,   (440 - 206)),
        (145,  (440 - 224)),
        (166,  (440 - 250)),
        (164,  (440 - 300)),
        (116,  (440 - 330)),
        (78,   (440 - 330)),
        (42,   (440 - 308)),
        (34,   (440 - 270)),
        (38,   (440 - 236))
    ), DARK_SKIN)

arcade.finish_render()
arcade.run()
