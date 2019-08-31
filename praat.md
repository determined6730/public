# praat


> 스크립트 문법을 제대로 모르고 시간이 부족해서 기존 스크립트를 분석해서 역으로 알아가자.. 

``` 
# form이 생성 되는 부분 
form Settings
    # Interval_tiers를 미리 입력해 놓는 부분 ( form생성된 이후 수정 가능)
    sentence Interval_tiers Utterance Word Rhyme
    # Point_tiers 를 미리 입력해 놓는 부분 ( form생성된 이후 수정 가능)
    sentence Point_tiers SynBoundary
    # optino을 선택하는 것임 
    optionmenu If_TextGrid_already_exists: 1
        option skip the sound file
        option create a TextGrid with a different filename
        option open and edit the existing TextGrid
    # word -> 왠지 다른 곳에사 사용하기 위해서 지정하는 것 같음 
    # 조금 있다 아래족에서 사용될 것이니 확인해볼것 
    word Sound_file_extension .wav
    comment Press OK to choose a directory of sound files to annotate.
endform
```

``
# directory 생성하는 부분임 `
directory$ = chooseDirectory$: "Choose a directory with 'sound_file_extension$'
... files to annotate."
@getFiles: directory$, sound_file_extension$

tiers$ = interval_tiers$ + " " + point_tiers$
```


