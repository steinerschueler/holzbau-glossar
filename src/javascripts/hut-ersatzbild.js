/* Ersatzbild für den Buchstaben mit Hut.
 *
 * Der Build-Hook setzt «n_hat» aus den Quellen als MathML (<math class="hut">).
 * Ein Browser ohne MathML, etwa Chrome und Edge vor Version 109 (Januar 2023),
 * zeigt davon nur «n^», und das sieht aus wie eine Hochzahl. Dort ersetzt
 * dieses Skript jede solche Formel durch ein kleines Bild (SVG): Buchstabe,
 * Hut darüber, Index und Hochzahl daneben, in der Schrift und Farbe der
 * Umgebung. Ein Browser mit MathML bleibt unberührt.
 */
(function () {
  "use strict";

  const SVG_NS = "http://www.w3.org/2000/svg";
  const MATHML_NS = "http://www.w3.org/1998/Math/MathML";
  // Dieselben Formen wie im Build-Hook (hooks/build_pages.py, _HUT): Index
  // ohne oder mit Klammern oder tiefgestellt, danach eine Hochzahl.
  const FORM = /^(\p{L})_hat(?:_(\{[^{}]+\}|[^_^{}]+)|([₀-₉ₐ-ₜᵢ-ᵪⱼ]+))?(?:\^(\{[^{}]+\}|.+))?$/u;
  // Buchstaben, die über die Mittellänge reichen: Der Hut sitzt dann höher.
  const HOHER_BUCHSTABE = /[A-ZbdfhkltΑ-Ωβδζθλξ]/u;
  const messflaeche = document.createElement("canvas").getContext("2d");
  let kannMathML = null;

  function pruefeMathML() {
    // Ein Browser mit MathML gibt dem leeren mspace die verlangte Breite,
    // einer ohne MathML kennt das Element nicht und lässt es leer.
    const probe = document.createElement("div");
    probe.style.cssText = "position:absolute;top:0;left:0;visibility:hidden";
    const formel = document.createElementNS(MATHML_NS, "math");
    const raum = document.createElementNS(MATHML_NS, "mspace");
    raum.setAttribute("width", "80px");
    raum.setAttribute("height", "20px");
    formel.appendChild(raum);
    probe.appendChild(formel);
    document.body.appendChild(probe);
    const breite = raum.getBoundingClientRect().width;
    document.body.removeChild(probe);
    return breite > 40;
  }

  function textbreite(text, kursiv, groesse, stil) {
    messflaeche.font = `${kursiv ? "italic" : "normal"} ${stil.fontWeight} ${groesse}px ${stil.fontFamily}`;
    return messflaeche.measureText(text).width;
  }

  function tspan(text, x, y, groesse, kursiv) {
    const teil = document.createElementNS(SVG_NS, "tspan");
    teil.setAttribute("x", x.toFixed(2));
    teil.setAttribute("y", y.toFixed(2));
    teil.setAttribute("font-size", groesse.toFixed(2));
    teil.setAttribute("font-style", kursiv ? "italic" : "normal");
    teil.textContent = text;
    return teil;
  }

  // Index oder Hochzahl: ein Zeichen oder Wort, in Klammern eine Folge wie
  // «a,i» oder «A_i». Gibt die Breite zurück.
  function zusatz(text, roh, x, y, groesse, stil) {
    const inKlammern = roh.startsWith("{");
    const zeichen = inKlammern ? Array.from(roh.slice(1, -1)) : [roh];
    let breite = 0;
    let tiefer = false;
    for (const z of zeichen) {
      if (inKlammern && z === "_") {
        tiefer = true;
        continue;
      }
      const g = tiefer ? groesse * 0.8 : groesse;
      const kursiv = /^\p{L}$/u.test(z);
      text.appendChild(tspan(z, x + breite, tiefer ? y + 0.25 * groesse : y, g, kursiv));
      breite += textbreite(z, kursiv, g, stil);
      tiefer = false;
    }
    return breite;
  }

  function ersatzbild(formel) {
    const titel = formel.getAttribute("title") || "";
    const teile = FORM.exec(titel);
    if (!teile || !formel.parentElement) return;
    const [, buchstabe, index, tiefgestellt, hochzahl] = teile;
    const stil = getComputedStyle(formel.parentElement);
    const fs = parseFloat(stil.fontSize) || 16;
    const grundlinie = 1.05 * fs;
    const unterlaenge = 0.4 * fs;

    const bild = document.createElementNS(SVG_NS, "svg");
    const titelElement = document.createElementNS(SVG_NS, "title");
    titelElement.textContent = titel;
    bild.appendChild(titelElement);

    const text = document.createElementNS(SVG_NS, "text");
    text.setAttribute("fill", "currentColor");
    text.appendChild(tspan(buchstabe, 0, grundlinie, fs, true));
    const bBreite = textbreite(buchstabe, true, fs, stil);

    // Hut als Winkel über der Mitte des Buchstabens, wegen der Neigung der
    // Kursiven etwas nach rechts.
    const mitte = bBreite * 0.58;
    const halb = 0.2 * fs;
    const spitze = grundlinie - (HOHER_BUCHSTABE.test(buchstabe) ? 1.0 : 0.76) * fs;
    const fuss = spitze + 0.16 * fs;
    const hut = document.createElementNS(SVG_NS, "path");
    hut.setAttribute("d", `M${(mitte - halb).toFixed(2)} ${fuss.toFixed(2)} L${mitte.toFixed(2)} ${spitze.toFixed(2)} L${(mitte + halb).toFixed(2)} ${fuss.toFixed(2)}`);
    hut.setAttribute("fill", "none");
    hut.setAttribute("stroke", "currentColor");
    hut.setAttribute("stroke-width", (0.065 * fs).toFixed(2));
    hut.setAttribute("stroke-linecap", "round");
    hut.setAttribute("stroke-linejoin", "round");

    const x = bBreite + 0.05 * fs;
    let breiteIndex = 0;
    let breiteHoch = 0;
    const indexText = index || (tiefgestellt && tiefgestellt.normalize("NFKC"));
    if (indexText) breiteIndex = zusatz(text, indexText, x, grundlinie + 0.28 * fs, 0.7 * fs, stil);
    if (hochzahl) breiteHoch = zusatz(text, hochzahl, x, grundlinie - 0.45 * fs, 0.7 * fs, stil);

    const breite = x + Math.max(breiteIndex, breiteHoch) + 0.05 * fs;
    const hoehe = grundlinie + unterlaenge;
    bild.setAttribute("class", "hut-bild");
    bild.setAttribute("role", "img");
    bild.setAttribute("aria-label", titel);
    bild.setAttribute("width", breite.toFixed(2));
    bild.setAttribute("height", hoehe.toFixed(2));
    bild.setAttribute("viewBox", `0 0 ${breite.toFixed(2)} ${hoehe.toFixed(2)}`);
    bild.style.verticalAlign = `${(-unterlaenge).toFixed(2)}px`;
    bild.style.overflow = "visible";
    bild.appendChild(text);
    bild.appendChild(hut);
    formel.parentNode.replaceChild(bild, formel);
  }

  function setzeErsatzbilder() {
    const formeln = document.querySelectorAll("math.hut");
    if (!formeln.length) return;
    // Mit «?hut=bild» in der Adresse zeigt jeder Browser das Ersatzbild, zum
    // Ansehen und Prüfen.
    const erzwungen = new URLSearchParams(window.location.search).get("hut") === "bild";
    if (kannMathML === null) kannMathML = pruefeMathML();
    if (kannMathML && !erzwungen) return;
    formeln.forEach(ersatzbild);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setzeErsatzbilder);
  } else {
    setzeErsatzbilder();
  }

  // Instant-Navigation von Material: nach jedem Seitenwechsel erneut.
  if (window.document$) {
    window.document$.subscribe(setzeErsatzbilder);
  }
})();
