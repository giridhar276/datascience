"""Create and process video frames.
VideoWriter_fourcc() defines codec.
VideoWriter() creates video.
VideoCapture() reads video.
read() returns frames.
cvtColor() converts frames to grayscale.
write() saves processed frames.
release() closes resources.
"""
from pathlib import Path
import cv2, numpy as np
B=Path(__file__).parent
source=B/"outputs"/"sample_input_video.avi"
target=B/"outputs"/"grayscale_output_video.avi"
w,h,fps=640,420,10
fourcc=cv2.VideoWriter_fourcc(*"MJPG")
writer=cv2.VideoWriter(str(source),fourcc,fps,(w,h))
for i in range(50):
    frame=np.full((h,w,3),255,dtype=np.uint8)
    cv2.circle(frame,(20+i*10,210),40,(0,0,255),-1)
    cv2.putText(frame,f"Frame {i}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
    writer.write(frame)
writer.release()
cap=cv2.VideoCapture(str(source))
out=cv2.VideoWriter(str(target),fourcc,fps,(w,h),False)
while True:
    ok,frame=cap.read()
    if not ok: break
    out.write(cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY))
cap.release()
out.release()
print("Saved input and processed videos")
