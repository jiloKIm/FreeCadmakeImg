import sys 
import FreeCAD 
import FreeCADGui 
import Part 
import math 
# GUI 시작 
FreeCADGui.showMainWindow()
 # 모델 로드
 doc = FreeCAD.open("C:/Users/kim hyun se/Desktop/01.fcstd") 
# Z축을 중심으로 회전 
rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,1), 10) 
for i in range(100): 
for obj in doc.Objects: 
if obj.isDerivedFrom("Part::Feature"): 
obj.Placement.Rotation = rot.multiply(obj.Placement.Rotation)
 # 렌더링 뷰 갱신 
FreeCADGui.ActiveDocument.ActiveView.viewAxonometric() FreeCADGui.ActiveDocument.ActiveView.fitAll() # 스크린샷 저장 FreeCADGui.ActiveDocument.ActiveView.saveImage(f"C:/Users/kim hyun se/Desktop/screenshots/screenshot_{i}.jpg",1920,1080,"White") 

print("Done")
