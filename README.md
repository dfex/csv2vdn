##csv2vdn.py

Quick'n'dirty script for mapping a CSV full of indials to pilot numbers for FreeSwitch.

The .csv file supplied needs to have headings of ```Indial``` (for destination number) and ```VDN``` for pilot number eg:

```
Indial,Alias,VDN,,
61738529800,Main Number,9800,,
61300365365,Support Number,6800,,
61738529899,Moves Adds Changes,6800,,
```

Will spit out Freeswitch configuration in the form

```
**9800_indial.xml**:
<extension name="61738529800">
  <condition expression="61738529800" field="destination_number">
    <action application="bridge" data="sofia/internal/9800@192.168.2.37:5060"/>
  </condition>
</extension>

**6800_indial.xml**:
<extension name="61300365365">
  <condition expression="61300365365" field="destination_number">
    <action application="bridge" data="sofia/internal/6800@192.168.2.37:5060"/>
  </condition>
</extension>
<extension name="61738529899">
  <condition expression="61738529899" field="destination_number">
    <action application="bridge" data="sofia/internal/6800@192.168.2.37:5060"/>
  </condition>
</extension>
```
