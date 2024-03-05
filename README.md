# FreeCAD 형상 정보 저장하기

## 시나리오



## 사용 모듈

```python
import FreeCAD
import FreeCADGui
import Part
import math
```

- `FreeCAD`: 3D 모델을 프로그래밍적으로 분석할 수 있게 Python API 제공.
- `FreeCADGui`: GUI 구성 요소에 접근. 랜더링 뷰 계산이나, 액티브 뷰로 스크린샷을 저장하는 기능 제공. 외부에서 접근 불가능.
- `Part`: 3D 모양과 기하학 처리 및 조작을 담당하는 FreeCAD의 핵심 모듈.

## 모델 로드 코드

```python
FreeCADGui.showMainWindow() # GUI 시작
doc = FreeCAD.open("C:/Users/kim hyun se/Desktop/01.fcstd") # 모델 로드
```

## Z축을 중심으로 회전

```python
rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,1), 10) # 회전 설정
for i in range(100):
    for obj in doc.Objects:
        if obj.isDerivedFrom("Part::Feature"):
            obj.Placement.Rotation = rot.multiply(obj.Placement.Rotation)
```

## 렌더링 뷰 갱신

```python
FreeCADGui.ActiveDocument.ActiveView.viewAxonometric()
FreeCADGui.ActiveDocument.ActiveView.fitAll()
```

## 스크린샷 저장

```python
# 스크린샷 저장
FreeCADGui.ActiveDocument.ActiveView.saveImage(f"C:/Users/kim hyun se/Desktop/screenshots/screenshot_{i}.jpg",1920,1080,"White")
print("Done")
```

## 칼리브레이션: 위치 확인 후 조립 수행

1. **체스보드 캡처**
   - 여러 각도와 위치에서 체스보드 패턴 포착한 여러 이미지 캡처.

2. **코너 검출**
   - `cv2.findChessboardCorners()` 함수 사용하여 각 이미지에서 체스보드의 코너 검출.

3. **칼리브레이션**
   - 검출된 코너의 2D 이미지 위치와 실제 3D 월드 위치를 바탕으로 `cv2.calibrateCamera()` 함수 사용하여 카메라의 내부 및 외부 파라미터 추정.

4. **왜곡 보정**
   - `cv2.undistort()` 함수 사용하여 이미지의 왜곡 보정.
