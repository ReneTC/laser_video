from pymin import *

frames = 40
# def draw_line(p1,p2,when_frame,out = 9999):
#     p1 = Vector(p1[0],p1[1])
#     p2 = Vector(p2[0],p2[1])
#
#     p1x = interpolate(p1[0],p2[0],when_frame)
#     p2x = interpolate(p1[0],p2[0],out)
#
#     if abs(p1x - p2x) < 2:
#         return
#     p1y = interpolate(p1[1],p2[1],when_frame)
#     p2y = interpolate(p1[1],p2[1],out)
#
#     start_pos = Vector(p1x,p1y)
#     end_pos = Vector(p2x,p2y)
#     line(start_pos,end_pos)
#
# def dist_shower(p1,p2,when_frame,out = 999):
#     draw_line(p1,p2,when_frame,out)
#     p1 = Vector(p1[0],p1[1])
#     p2 = Vector(p2[0],p2[1])
#     p3 = p1-p2
#     angle = atan2(p3[1], p3[0]) + PI/2
#     with push_matrix():
#         translate(p1[0],p1[1])
#         rotate(angle)
#         draw_line((-25,0),(25,0),when_frame+5,out+5)
#     with push_matrix():
#         translate(p2[0],p2[1])
#         rotate(angle)
#         draw_line((-25,0),(25,0),when_frame+10,out+10)


def setup():
    size(width, height)

def draw():
    translate(width/2,height/2)
    background(255)
    dist_shower((0,0),(500,100),15)
    stroke_weight(5)


    if frame_count > frames:
        exit()

if __name__ == '__main__':
    run(frame_rate=30)
