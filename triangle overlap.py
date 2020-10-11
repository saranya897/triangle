f = 0
def on_segment(p, q, r):

    if r[0] <= max(p[0], q[0]) and r[0] >= min(p[0], q[0]) and r[1] <= max(p[1], q[1]) and r[1] >= min(p[1], q[1]):

        return True
    return False



def orientation(p, q, r):

    val = ((q[1] - p[1]) * (r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))
    if val == 0 : return 0
    return 1 if val > 0 else -1

                  

def intersects(seg1, seg2):
    p1, q1 = seg1
    p2, q2 = seg2

    o1 = orientation(p1, q1,p2)

    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:


        return True



    if o1 == 0 and on_segment(p1, q1, p2): return True


    elif o2 == 0 and on_segment(p1, q1, q2): return True
    elif o3 == 0 and on_segment(p2, q2, p1): return True
    elif o4 == 0 and on_segment(p2, q2, q1): return True

    return False
print("input the coordinates")
x1,y1,x2,y2,x3,y3,X1,Y1,X2,Y2,X3,Y3=map(float,input().split(" "))
a1=(x1,y1)
a2=(x2,y2)
a3=(x3,y3)
a4=(X1,Y1)
a5=(X2,Y2)
a6=(X3,Y3)
segment_one=(a1,a2)
segment_two=(a4,a5)
print(intersects(segment_one, segment_two))
segment_one=(a1,a2)
segment_two=(a5,a6)
print(intersects(segment_one, segment_two))
segment_one=(a1,a2)
segment_two=(a4,a6)
print(intersects(segment_one, segment_two))
segment_one=(a2,a3)
segment_two=(a4,a5)
print(intersects(segment_one, segment_two))
segment_one=(a2,a3)
segment_two=(a5,a6)
print(intersects(segment_one, segment_two))
segment_one=(a2,a3)
segment_two=(a4,a6)
print(intersects(segment_one, segment_two))
segment_one=(a1,a3)
segment_two=(a4,a5)
print(intersects(segment_one, segment_two))
segment_one=(a1,a3)
segment_two=(a5,a6)
print(intersects(segment_one, segment_two))
segment_one=(a1,a3)
segment_two=(a4,a6)
print(intersects(segment_one, segment_two))
print("true means intersects ,so triangle overlap")
print("false  means  not intersects ,so triangle  not overlap")























