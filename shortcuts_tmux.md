# tmux shortcuts

Fn : Ctrl + b

## Pane 관련 
|         |                            |
|---------|----------------------------|
| Fn -> , | rename current pane        |
| Fn -> % | vertical split             |
| Fn -> " | horizental split           |
| Fn -> x | kill pane                  |
| Fn -> o | swap pane                  |
| Fn -> q | show pane number           |
| Fn -> w | show interactive list      |
| Fn -> z | zoom in on the active pane |

## Resize Panes 

|                                              |                                                                     |
|----------------------------------------------|---------------------------------------------------------------------|
| Fn -> resize-pane [target] [direction] [num] | resizes the pane with the id of [target] [direction] by [num] cells |

ex) 
```
PREFIX : resize-pane -D (Resizes the current pane down)
PREFIX : resize-pane -U (Resizes the current pane upward)
PREFIX : resize-pane -L (Resizes the current pane left)
PREFIX : resize-pane -R (Resizes the current pane right)
PREFIX : resize-pane -D 20 (Resizes the current pane down by 20 cells)
PREFIX : resize-pane -U 20 (Resizes the current pane upward by 20 cells)
PREFIX : resize-pane -L 20 (Resizes the current pane left by 20 cells)
PREFIX : resize-pane -R 20 (Resizes the current pane right by 20 cells)
PREFIX : resize-pane -t 2 20 (Resizes the pane with the id of 2 down by 20 cells)
PREFIX : resize-pane -t -L 20 (Resizes the pane with the id of 2 left by 20 cells)
```


