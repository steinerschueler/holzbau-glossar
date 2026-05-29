/* Wickelt jeden H2-Abschnitt einer Seite in ein <details>-Element, sodass
 * lange Glossar-Einträge sich auf ihre Sektionsköpfe reduzieren und der
 * Leser gezielt aufklappt, was ihn interessiert.
 *
 * Default:
 *   - Desktop (>= 76.1875em): alle Sektionen offen. Material zeigt
 *     auf dieser Breite die rechte TOC fix an — der Leser navigiert
 *     ohne Klick-Aufwand zur gewünschten Sektion.
 *   - Mobile/Tablet (<  76.1875em): alle Sektionen zu, Klick öffnet.
 *     Die rechte TOC ist hier nicht sichtbar, der Akkordeon-Stil
 *     verhindert seitenlanges Scrollen.
 * Anchor-Direktlinks (z.B. /ressourcen/punkt/#beziehungen) öffnen die
 * adressierte Sektion in beiden Modi automatisch.
 */
(function () {
  // Material's Breakpoint zur permanenten linken+rechten Sidebar.
  // Identisch mit der SCSS-Variable $break-devices--screen (76.1875em).
  const DESKTOP_MQ = "(min-width: 76.1875em)";

  function wrapSections() {
    const article = document.querySelector("article.md-content__inner")
      || document.querySelector("article");
    if (!article) return;

    // Wir wickeln nur die Top-Level-H2 des Inhalts, nicht H2 in Tabellen
    // oder Code-Blöcken.
    const headings = Array.from(article.children).filter(
      el => el.tagName === "H2"
    );
    if (headings.length === 0) return;

    const openByDefault = window.matchMedia(DESKTOP_MQ).matches;

    headings.forEach(h2 => {
      const details = document.createElement("details");
      details.className = "glossar-section";
      if (openByDefault) details.open = true;

      // Anker-ID des H2 auf das <details>-Element übernehmen, damit
      // direkte Anchor-Links (.../#prosa-definition) weiterhin auf die
      // jetzt aufklappbare Section zeigen.
      if (h2.id) details.id = h2.id;

      // Material's Permalink-Anchor (¶) aus dem H2-Inhalt entfernen,
      // bevor wir ihn ins Summary übernehmen — das Summary ist selbst
      // klickbar zum Öffnen, ein zusätzlicher Permalink-Anchor stört
      // visuell (Material's hover-only-CSS greift auf <h2>, nicht auf
      // <summary>).
      const clone = h2.cloneNode(true);
      clone.querySelectorAll("a.headerlink").forEach(a => a.remove());

      const summary = document.createElement("summary");
      summary.className = "glossar-section-summary";
      summary.innerHTML = clone.innerHTML;
      details.appendChild(summary);

      // Alle Geschwister-Elemente bis zum nächsten H2 hineinverschieben.
      let next = h2.nextElementSibling;
      while (next && next.tagName !== "H2") {
        const toMove = next;
        next = next.nextElementSibling;
        details.appendChild(toMove);
      }

      h2.parentNode.replaceChild(details, h2);
    });

    // Falls die URL einen Anchor enthält, öffne die enthaltende Section.
    if (window.location.hash) {
      const target = document.querySelector(window.location.hash);
      if (target) {
        let host = target.closest("details.glossar-section");
        if (host) {
          host.open = true;
          target.scrollIntoView({ block: "start" });
        }
      }
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", wrapSections);
  } else {
    wrapSections();
  }

  // Material-Theme nutzt Instant-Navigation; nach jedem internen
  // Seitenwechsel den Wrapping-Schritt erneut anwenden.
  if (window.document$) {
    window.document$.subscribe(wrapSections);
  }
})();
