# TDCC Weekly PDF Font Asset

TDCC weekly production PDFs use a repo-controlled Traditional Chinese Kai font
so local builds, Codex automation, and GitHub Actions render with the same CJK
font contract.

Bundled asset:

- `TW-Kai-98_1.ttf`

Source:

- CNS11643 open data Kai font package:
  `https://www.cns11643.gov.tw/opendata/Fonts_Kai.zip`
- The upstream package also includes a Chinese source note. The bundled copy is
  stored as `README-TW-Kai-source.txt`.

SHA256:

- `TW-Kai-98_1.ttf`:
  `C206333EDCC3C8C86EE547DA4C78AD1C8F7EC2670A2B550A768532258F75806A`
- `README-TW-Kai-source.txt`:
  `F791CD042191B72BFCD9829DAAD571FF34B4E334D6E6B43611D4BF48C47271B6`

Do not replace this with runner-installed fonts, Windows `kaiu.ttf`, ReportLab
CID fallback fonts such as `STSong-Light`, Noto Sans, or a generic sans-serif
font. The TDCC weekly builder and validator must fail closed if this font asset
is missing or if generated PDFs do not contain an allowed Kai font token.
