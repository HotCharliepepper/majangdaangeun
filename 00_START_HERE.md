# MAJANGDONG × MASHCORE — R1.2 비밀번호 없는 공유용

이번 파일은 당근 마케팅 제안서만 비밀번호 없이 열리는 버전입니다. R1.1 잠금 버전과 ARVO 월간 보고서는 별개이며 변경하지 않습니다.

## 1. 화면 확인
압축 해제 후 `index.html`을 더블클릭합니다. `assets` 폴더는 함께 보관하세요. 기존 썸네일·CPC 계산기·의견 확인·복사·TXT 저장이 유지됩니다.

## 2. GitHub Desktop
File → New repository → `majangdong-daangn-share` (추천 이름) → 압축 해제한 파일과 폴더 전체를 저장소 루트에 복사 → Commit → Publish repository. 소스 자체는 Private 권장. 공개 GitHub가 아니어도 Netlify 페이지는 공개할 수 있습니다. 기존 ARVO 고객 전용 보고서 저장소에는 넣지 않습니다.

## 3. Netlify
Add new project → Import an existing project → GitHub → 새 저장소 선택.
- Branch: main
- Base directory: 공란
- Build command: `python3 build.py`
- Publish directory: `dist`
설정은 `netlify.toml`에 포함. 추가 환경변수 입력이나 비밀번호 설정은 필요 없습니다. Netlify가 제공하는 URL로 OG 이미지 절대주소를 자동 생성합니다. 새 사이트의 Visitor access가 공개 상태인지 확인하세요. 기존 잠금 사이트의 설정을 변경하지 마세요.

## 4. 공유 전 검수
- 시크릿 창에서 비밀번호 없이 전체 제안서가 열리는지 확인.
- 실제 주소의 `/assets/share-thumbnail.jpg`가 열리는지 확인.
- 카카오톡에서 링크를 테스트. 공유앱 캐시·크롭에 따라 실제 썸네일은 달라질 수 있습니다.
- 음식·매장 이미지 공개 권한과 20만 원 관리료 제안 등 외부 노출 범위를 확인한 뒤 링크를 전달합니다. 누구나 주소를 알면 볼 수 있으며 noindex는 보안 기능이 아닙니다.
- 생성 이미지의 휴대폰 화면 및 수치는 콘셉트 예시. 실제 광고 실적이 아닙니다. 의견은 복사·TXT 저장만 가능하고 결제·전송·서버 저장은 하지 않습니다.

운영용 월간 보고서·계약서·실적 원장·내부 KPI는 이 패키지에 포함하지 않았습니다.
