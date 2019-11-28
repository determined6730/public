# praat


## files
```
# open a sound file 
Read from file: "1.wav" 
Read from file: "./../../1.wav"
Open long sound file: "long.wav"

# save a sound file as WAV file ( sound object must be selected! )
Save as WAV file: "3.wav"

# save a TextGrid as text file ( TextGrid object must be selected! )
Sava as text file: "4.TextGrid"

# 
```
### Create Strings as file list


## variables 



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

```
# directory 생성하는 부분임 `
directory$ = chooseDirectory$: "Choose a directory with 'sound_file_extension$'
... files to annotate."
@getFiles: directory$, sound_file_extension$

tiers$ = interval_tiers$ + " " + point_tiers$
```


## generate textGrid & insert boundary 
```
form Settings
    sentence Interval_tiers Utterance Word Rhyme
    sentence Point_tiers SynBoundary
    optionmenu If_TextGrid_already_exists: 1
        option skip the sound file
        option create a TextGrid with a different filename
        option open and edit the existing TextGrid
    word Sound_file_extension .wav
    comment Press OK to choose a directory of sound files to annotate.
endform

directory$ = chooseDirectory$: "Choose a directory with 'sound_file_extension$'
... files to annotate."
@getFiles: directory$, sound_file_extension$

tiers$ = interval_tiers$ + " " + point_tiers$

# getFiles : directory에서 sound_file_extension들만 가지고온 것 
# length : 위에서의 그 갯수 
# 즉 아래 for구문은  해당 디렉토리에서 wav파일의 수만큼 반복하는 것 

for i to getFiles.length
    soundfile = Read from file: getFiles.files$ [i]

    @getTextGrid: getFiles.files$ [i]

    if !fileReadable (getTextGrid.path$) or if_TextGrid_already_exists > 1
        selectObject: soundfile, getTextGrid.textgrid
        View & Edit

		selectObject: getTextGrid.textgrid

		total_duration = Get duration

		first_duration = total_duration / 3
		second_duration = total_duration / 14
		third_duration = total_duration / 25

		writeInfoLine: "Hello World"
		appendInfoLine: total_duration
		numberOfIntervals = Get number of intervals: 1

		i = 1
		while i <= 2
			Insert boundary: 1,i*first_duration
			i = i + 1
		endwhile

		i = 1
		while i <= 13
			Insert boundary: 2,i*second_duration
			i = i + 1
		endwhile
		
		i = 1
		while i <= 24
			Insert boundary: 3,i*third_duration
			i = i + 1
		endwhile


		newlab$ = "<<replace_string>>"
		Set interval text: 1, 2, newlab$

		Set interval text: 2, 2, "w1"
		Set interval text: 2, 3, "w2"
		Set interval text: 2, 4, "w3"
		Set interval text: 2, 5, "w4"
		Set interval text: 2, 6, "w5"
		Set interval text: 2, 7, "w6"
		Set interval text: 2, 8, "w7"
		Set interval text: 2, 9, "w8"
		Set interval text: 2, 10, "w9"
		Set interval text: 2, 11, "w10"
		Set interval text: 2, 12, "w11"
		Set interval text: 2, 13, "w12"

		Set interval text: 3, 2, "D1"
		Set interval text: 3, 4, "<<2>>"
		Set interval text: 3, 6, "<<3>>"
		Set interval text: 3, 8, "<<4>>"
		Set interval text: 3, 10, "<<5>>"
		Set interval text: 3, 12, "<<6>>"
		Set interval text: 3, 14, "<<7>>"
		Set interval text: 3, 16, "<<8>>"
		Set interval text: 3, 18, "<<9>>"
		Set interval text: 3, 20, "<<10>"
		Set interval text: 3, 22, "<<11>>"
		Set interval text: 3, 24, "<<12>>"		


        selectObject: getTextGrid.textgrid
        Save as text file: getTextGrid.path$

        removeObject: getTextGrid.textgrid

    endif

    removeObject: soundfile

endfor

procedure getTextGrid: .soundfile$
    .path$ = replace$: .soundfile$, sound_file_extension$, ".TextGrid", 0

    if !fileReadable: .path$
        .textgrid = To TextGrid: tiers$, point_tiers$

    elif if_TextGrid_already_exists == 2
        .textgrid = To TextGrid: tiers$, point_tiers$
        .default$ = mid$: .path$, rindex (.path$, "/") + 1, length (.path$)
        .default$ = replace$: .default$, sound_file_extension$, ".TextGrid", 1

        .path$ = chooseWriteFile$: "TextGrid already exists in this directory. 
        ... Choose where to save the new TextGrid.", .default$

    elif if_TextGrid_already_exists == 3
        .textgrid = Read from file: .path$

    endif

endproc

procedure getFiles: .dir$, .ext$
    .obj = Create Strings as file list: "files", .dir$ + "/*" + .ext$
    .length = Get number of strings

    for .i to .length
        .fname$ = Get string: .i
        .files$ [.i] = .dir$ + "/" + .fname$

    endfor

    removeObject: .obj

endproc
```

## python module?
- TextGridTools
- parselmouth
- praat-textgrids
- textgrid

