# Repository-Controlled Fonts

## TDCC Weekly PDF Font

`TDCCSansTC-Regular.ttf` is the required CJK font asset for TDCC weekly
holder-flow production PDFs. It is a renamed static weight=400 instance
generated from the bundled Google Fonts source `NotoSansTC-wght.ttf` so
ReportLab renders a stable Regular face instead of selecting a variable-font
Thin instance. The derived font is renamed to avoid using the upstream Reserved
Font Name for a modified font.

Source:

```text
https://github.com/google/fonts/blob/main/ofl/notosanstc/NotoSansTC%5Bwght%5D.ttf
```

License:

```text
SIL Open Font License, Version 1.1
```

The license text is stored in:

```text
assets/fonts/OFL-NotoSansTC.txt
```

SHA256:

```text
NotoSansTC-wght.ttf        864727D210D54F2537BBE23B3A839436C3992AF72DE9322AF5270897246BD44F
TDCCSansTC-Regular.ttf     A4A1E1758CF89B5EFA65B154BE55D8DC7A67F11CADF3DBEFF83F2C63E22E0404
OFL-NotoSansTC.txt         0DD431A8AE39F2183C12CE9DDF433CD320399C106096D713D65F1AE8803E6FF9
```

Static instance generation:

```text
python -m fontTools.varLib.instancer assets/fonts/NotoSansTC-wght.ttf wght=400 -o assets/fonts/TDCCSansTC-Regular.ttf
```

After instancing, the font name table is rewritten from the upstream `Noto`
family names to `TDCC Sans TC` / `TDCCSansTC-Regular`.

TDCC weekly PDF generation must fail closed if this font cannot be registered.
Production TDCC weekly PDFs must not silently fall back to ReportLab built-in
CID fonts such as `STSong-Light`.
