#!/usr/bin/env python2

from eagle import *

app = App( title="Paint",
           id="paint",
           statusbar=True,
           left=( Color( id="fg",
                         label="Foreground:",
                         color="black",
                         ),
                  Color( id="bg",
                         label="Background:",
                         color=( 255, 0, 0 ),
                         ),
                  Selection( id="tool",
                             label="Tool:",
                             ),
                  UIntSpin( id="size",
                            label="Line Size:",
                            min=1,
                            value=1,
                            ),
                  ),
           right=( Group( id="textgroup",
                          label="Text Properties:",
                          children=( Entry( id="text",
                                            label="Contents:",
                                            ),
                                     Font( id="font",
                                           label="Font:",
                                           ),
                                     CheckBox( id="textbgtransp",
                                               label="Transparent background?",
                                               ),
                                     ),
                          ),
                   Group( id="rectgroup",
                          label="Rectangle Properties:",
                          children=( CheckBox( id="rectfill",
                                               label="Fill?",
                                               ),
                                     ),
                          ),
                   ),
           top=( SaveFileButton(),
                 CloseButton(),
                 Button( id="undo",
                         stock="undo",
                         ),
                 Button( id="clear",
                         stock="clear",
                         ),
                 ),
           center=( Canvas( id="canvas",
                            label="Draw Here:",
                            width=400,
                            height=400,
                            bgcolor="white",
                            ),
                    )
           )

run()
