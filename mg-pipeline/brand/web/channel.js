/* 채널 공용 보조 스크립트 — kit.js 다음에 불러온다.
   data-at2 / data-at3 = 두 번째·세 번째 시각 (예: 순위 카드가 나타나는 시각은 data-at, 이름이 열리는 시각은 data-at2, 불이 켜지는 시각은 data-at3).
   값 형식은 data-at 과 같다: "6", "6:낱말", "+1.2". 앞당기기는 data-off2, data-off3. */
(() => {
  const set = (el, k, v) => el.style.setProperty(k, v.toFixed(3) + 's');
  for (const n of [2, 3]) document.querySelectorAll(`[data-at${n}]`).forEach(el => set(el, `--t${n}`, KIT.at(el.dataset[`at${n}`], +(el.dataset[`off${n}`] || 0))));
})();
