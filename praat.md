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

```
backup 

# USAGE:
#
# This Praat script makes the process of annotating multiple sound files go
# faster by automating most of the mouse-clicks that are needed to create and
# save new TextGrid files. It takes a folder of sound files. For each sound
# file, the script creates a new TextGrid with the annotation tiers that you
# list in the settings window, then opens that TextGrid along with its
# accompanying sound file. The script pauses while you create annotations for
# the sound file. When you are done creating annotations, press "OK" in the
# pop-up window to save the TextGrid to a file with the same filename as the
# sound file plus a ".TextGrid" extension. After saving the file, the script
# moves on to the next sound file in the folder.
#
# SETTINGS:
#
# Interval tiers:               Provide a list of names for the interval tiers
#                               (if any) that will be created in each new
#                               TextGrid. The tier names should be separated by
#                               spaces. The default will create two interval
#                               tiers named "Mary" and "John".
# Point tiers:                  Provide a list of names for the point tiers
#                               (if any) in each new TextGrid, with the tier
#                               names separated by spaces. The default will
#                               create one point tier named "bell".
# If TextGrid already exists:   If the folder that you select already contains
#                               a TextGrid with the same name as one of the
#                               sound files, what should the script do with
#                               that sound file? The default is to skip that
#                               sound file, or you can also choose to be
#                               prompted for a new TextGrid filename, or to
#                               open the existing TextGrid rather than creating
#                               a new one.
# Sound file extensions:        The extension of the sound files in your folder
#                               (.wav, .flac, etc).
#
# After you configure the settings, press OK to choose the directory of sound
# files to annotate.


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
