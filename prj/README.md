# opensw23_JSH
장서현 - 202211360

Topic Introduction
=
이번 프로젝트에서 선택한 주제는 pytorch-openpose라는 프로젝트의 레포지토리이다. 해당 프로젝트는 사진 상에서 사람의 몸과 손의 골격을 추정하여 결과물로 내보내는 딥러닝 프로젝트로, 사람이 포함되어있는 사진을 데이터셋으로 넣으면 사진 상에 존재하는 사람들의 몸과 손의 골격을 대략적으로 추정하고, 데이터셋으로 넣은 사진 위에 추정된 골격을 그려넣어 해당 사진을 결과물로 내보낸다. 해당 레포지토리의 주소는 https://github.com/Hzzone/pytorch-openpose 이다.

이번 프로젝트는 m1맥북에서 진행되었다.

Results
=
데이터셋 구성은 한명만 있는 사진들과 여러명이 있는 사진으로 구성되었다. 한명만 있는 사진 중에서는 상체만 나와 손이 자세히 보이는 사진과 전신이 나온 사진으로 구성했고, 여러명이 있는 사진은 몸의 형태가 떨어져있는 사진들과 붙어있는 사진들로 구성하였다.

![Figure_22](https://github.com/Solsol1014/opensw23_JSH/assets/106345468/12c79419-8f5c-4c2f-a35d-be3592feab56) ![Figure_14](https://github.com/Solsol1014/opensw23_JSH/assets/106345468/a3a4e9ac-702f-4415-9b59-326b15adb58d)
![Figure_3](https://github.com/Solsol1014/opensw23_JSH/assets/106345468/aaf3ce55-895a-450b-a761-f996a2393c30) ![1output](https://github.com/Solsol1014/opensw23_JSH/assets/106345468/3155af3f-34af-4077-b784-72d276e972ea)

![Figure_15](https://github.com/Solsol1014/opensw23_JSH/assets/106345468/eb6a08b4-86d8-46e7-9da8-878cfa1caf93)


Analysis/Visualization
=
![Figure_14](https://github.com/Solsol1014/opensw23_JSH/assets/106345468/75f726d7-4dee-4a89-a428-3eb526ac4082)
![Figure_22](https://github.com/Solsol1014/opensw23_JSH/assets/106345468/88cf04f9-d51c-4670-b4b5-5ae0e2cfcc34)
![Figure_19](https://github.com/Solsol1014/opensw23_JSH/assets/106345468/2f814e84-425d-4561-b835-0d85047e8dec)
![Figure_11](https://github.com/Solsol1014/opensw23_JSH/assets/106345468/8b885949-4189-4ffc-a983-a489b82a8636)
![Figure_21](https://github.com/Solsol1014/opensw23_JSH/assets/106345468/51572ebb-3a49-440e-9a08-e0de8a130470)

한명만 있는 사진들은 대체적으로 성공적인 결과를 보여주었다. 하지만 마지막 사진처럼 손이 얼굴과 붙어있어 손과 얼굴의 경계가 뚜렷하지 않은 사진의 경우에는 손 골격의 추정이 성공적으로 이루어지지 않았다.

![Figure_17](https://github.com/Solsol1014/opensw23_JSH/assets/106345468/b60d8cdc-0412-4f98-959b-b9f85c988334)

또한 해당 사진처럼 코트같이 온몸을 덮는 옷을 입었을 경우에는 몸, 팔, 다리의 구분이 잘 안되어 추정이 되지 않은 모습을 보여주기도 하였다.

![1output](https://github.com/Solsol1014/opensw23_JSH/assets/106345468/b39b4a32-77ff-4cdc-bdd7-5f69a1ae218f)
![Figure_19](https://github.com/Solsol1014/opensw23_JSH/assets/106345468/754c6aa0-3569-4427-9dc0-1fe7208ae058)

여러명이 나온 사진들의 경우에는, 위의 사진처럼 사람들이 충분히 떨어져있거나 확실한 구분이 가능한 경우에는 개별 사람마다의 골격 추정이 충분히 성공적으로 이루어졌다.

![Figure_12](https://github.com/Solsol1014/opensw23_JSH/assets/106345468/fe748296-11d0-4820-8fbf-fca47fdece79)

하지만 많은 사람들이 떨어져있지 않고 붙어있는 경우 가까이 있는 소수의 사람만 골격 추정이 이루어지고, 나머지는 아예 추정이 되지 않은 모습을 보여주었다.

![Figure_6](https://github.com/Solsol1014/opensw23_JSH/assets/106345468/5269c75b-b0b3-4dff-9402-4dda9b5b6229)
![Figure_7](https://github.com/Solsol1014/opensw23_JSH/assets/106345468/c974831a-72be-4993-855e-8795cfbbaf7a)
![Figure_15](https://github.com/Solsol1014/opensw23_JSH/assets/106345468/1682fba6-ef94-400d-a004-55c4ae4ffe7f)

또한, 소수의 사람이어도 서로 붙어있는 사진의 경우에는 붙어있는 두사람을 한명으로 인식해 하나의 골격으로 추정이 이루어진 모습을 보이기도 하였다.

결과적으로, 사람의 수보다는 사람 한명한명의 구분이 잘되는지에 따라 성공 여부가 갈렸다. 또한, 몸을 전체적으로 덮는 옷을 입어 몸통과 팔, 다리가 구분이 잘 안되면 실패 확률이 현저히 높아짐을 확인할 수 있었다.

Installation
=
가장 먼저, 밑의 코드를 cmd창에 입력하여 요구되는 모듈들을 다운로드 받아준다.

    pip install -r requirements.txt


그리고, 용량이 너무 커 깃에 들어가지 않는 모델들을 하단의 링크들 중 하나에서 받아준다.

[dropbox](https://www.dropbox.com/sh/7xbup2qsn7vvjxo/AABWFksdlgOMXR_r5v3RwKRYa?dl=0)

[google drive](https://drive.google.com/drive/folders/1JsvI4M4ZTg98fmnCZLFM-3TeovnCRElG?usp=sharing)

해당 파일들을 다운받은 후, 현재 프로젝트 폴더 안에 model이라는 이름으로 폴더를 생성하고, 다운받은 파일들을 model 폴더 안에 집어넣는다.

마지막으로, demo.py파일에 들어가 11번째 줄과 12번째 줄의 괄호 안쪽에 좀 전에 다운받은 파일들 중 body_pose_model.pth와 hand_pose_model.pth의 절대경로를 적어주고, 14번째 줄의 작은 따옴표 안에 본인이 실행시키고 싶은 이미지의 경로를 적어준 후 파일을 실행한다.

Presentation
=
