# Key-Holding-Macro
쓸모없어 보이지만 적어도 키보드에 동전을 올려두는 일은 없어집니다 !

### 싱글게임에서 무료한 노가다를 하지 않기 위해 만들었습니다 !! 싱글게임에서만 쓰세요 !!
>###### _※ 해당 프로그램은 DirectX 프로그램에서 정상 작동하는 것을 목표로 제작되었습니다_
>###### _※ 해당 프로그램을 사용함으로써 발생하는 불이익은 책임지지 않습니다._


------------------

## 1. HOW TO USE

1. 창을 선택합니다.
##### `Simplified Windows` 가 체크된 경우 - 단순화된 창 목록을 보여줍니다.
<img src="https://user-images.githubusercontent.com/88299137/223338813-c06aec3f-f67b-45be-971e-1106f6e5ed75.gif" width="200" height="150">

##### `Simplified Windows` 가 체크되지 않은 경우 - 모든 창 목록을 보여줍니다.
<img src="https://user-images.githubusercontent.com/88299137/223339387-37b38542-9141-4ce9-b2c0-ee0da88d1f8d.gif" width="200" height="150">

2. 원하는 키를 키보드로 입력합니다.
<img src="https://user-images.githubusercontent.com/88299137/223340304-9307b619-9d06-42c2-979c-d216f91c1506.gif" width=200 height=150>

3. `Hold Key` 버튼을 누르면 키 홀딩을 시작합니다.
<img src="https://user-images.githubusercontent.com/88299137/223340736-3c3a065d-4826-4ce2-9087-6e7791ae573b.gif" width=200 height=150>

4. 지정한 창이 활성화된 상태일 때 키 홀딩을 `Activating` 하고, 지정한 창이 비활성화되면 키 홀딩이 `Not Activating` 됩니다.
<img src=https://user-images.githubusercontent.com/88299137/223341100-24443806-aa00-4525-905a-373771ca3e35.gif width=200 height=150>

5. `Release Key` 버튼을 누르면 키 홀딩을 종료하고 새로운 창을 선택할 수 있습니다.
<img src=https://user-images.githubusercontent.com/88299137/223343391-4e279c12-5373-4055-9794-fa523941041d.gif width=200 height=150>

--------------

## 2. IN DETAIL
### USED MODULE
+ Input Module : `ClassDD` by [ddxoff](https://github.com/ddxoft)
  + Low-level hardware bitmap을 변경하여 실제 hardware input을 만들어냅니다.
+ Window detection : `Pywinin32` & `Pywinauto`
  + win에서만 동작하는 모듈입니다.
+ GUI : `tkinter`
  + Python built-in module입니다

### GUI
###### ※ Images from v0.1.1

>#### 1. UPPER FRAME
>+ 창 선택을 담당하는 부분들이 모여있습니다.
>
>![image](https://user-images.githubusercontent.com/88299137/223347804-19b965a3-81bd-4cdb-98cf-4202e1a61ea8.png)
>
>>##### 1-1. COMBOBOX
>>+ 원하는 창을 선택할 수 있습니다.
>>
>>![image](https://user-images.githubusercontent.com/88299137/223348047-7f5fb5fb-dd73-4935-a5b0-da474f656f60.png)
>
>>##### 1-2. CHECK BUTTON
>>+ COMBOBOX에서 보여주는 창의 목록을 단순화할 것인지 묻는 체크버튼입니다.
>>
>>![image](https://user-images.githubusercontent.com/88299137/223348112-2a39ea60-7610-40ea-81b4-c2b052aa594a.png)

>#### 2. LOWER FRAME
>+ 키 입력을 담당하는 부분들이 모여있습니다
>
>![image](https://user-images.githubusercontent.com/88299137/223348440-a1903a29-f3bf-4f2e-8068-5ec1aaa59b0e.png)
>
> >##### 2-1. KEY LABEL
> >+ 키 홀딩을 지속할 키를 보여줍니다. 키보드 입력을 통해 설정이 가능합니다.
> >
> >![image](https://user-images.githubusercontent.com/88299137/223348514-424bacca-7f39-4599-9ee6-b595e5ab3b73.png)
>
> >##### 2-2. START/STOP BUTTON
> >+ 키 홀딩을 시작하고 중지합니다. 에러가 발생한 경우 강제로 종료됩니다.
> >
> >![image](https://user-images.githubusercontent.com/88299137/223349094-529149b9-6922-4707-8c10-fe544524c222.png)
>
> >##### 2-3. ACTIVATING/NOT ACTIVATING LABEL
> >+ 키 홀딩이 시작됐을 때만 나타나는 글귀입니다. 현재 키 입력이 진행되고 있는 지를 표시합니다.
> >
> >![image](https://user-images.githubusercontent.com/88299137/223349187-acb6f028-9c73-4180-a9ef-40225b9b0e74.png)
> >![image](https://user-images.githubusercontent.com/88299137/223349596-2420319b-0165-4559-9e8a-8084b28e6442.png)

----------------

## 3. VERSION INFO
[Download Latest Version](https://github.com/JngVedere/Key-Holding-Macro/releases/tag/v0.1.1)

+ [v0.1.0](https://github.com/JngVedere/Key-Holding-Macro/releases/tag/v0.1.0) - RELEASED on 03-06-2023
+ [v0.1.1](https://github.com/JngVedere/Key-Holding-Macro/releases/tag/v0.1.1) - RELEASED on 03-07-2023

--------------

## 4. ADDITIONAL INFORMATION

### 4-1. IMPORTED MODULE(S)/FILE(S) REFERENCE
1. `ClassDD` https://github.com/ddxoft/master by [ddxoft](https://github.com/ddxoft)
2. `XK_TO_DD.py` https://github.com/JngVedere/XK_TO_DD created for myself

### 4-2. SUPPORTED KEY LIST
..UPDATING..
