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
    const openByDefault = window.matchMedia(DESKTOP_MQ).matches;

    // Wickelt jede Top-Level-H2 von `container` in eine Akkordeon-Section
    // (.glossar-section). Das Einsammeln stoppt an der Subglossar-Block-
    // Grenze, damit die letzte Hauptglossar-Section („Quelle herunterladen")
    // den separaten SG-Block nicht verschluckt.
    function wrapIn(container) {
      const headings = Array.from(container.children).filter(
        el => el.tagName === "H2"
      );
      headings.forEach(h2 => {
        const details = document.createElement("details");
        details.className = "glossar-section";
        if (openByDefault) details.open = true;

        // Anker-ID des H2 übernehmen, damit Direkt-Links (.../#prosa-
        // definition) weiterhin auf die aufklappbare Section zeigen.
        if (h2.id) details.id = h2.id;

        // Material's Permalink-Anchor (¶) vor der Summary-Übernahme
        // entfernen — das Summary ist selbst klickbar zum Öffnen.
        const clone = h2.cloneNode(true);
        clone.querySelectorAll("a.headerlink").forEach(a => a.remove());

        const summary = document.createElement("summary");
        summary.className = "glossar-section-summary";
        summary.innerHTML = clone.innerHTML;
        details.appendChild(summary);

        let next = h2.nextElementSibling;
        while (
          next &&
          next.tagName !== "H2" &&
          !next.classList.contains("subglossar-block")
        ) {
          const toMove = next;
          next = next.nextElementSibling;
          details.appendChild(toMove);
        }

        h2.parentNode.replaceChild(details, h2);
      });
    }

    // 1) Hauptglossar-Sektionen (Top-Level des Artikels) — stoppt am SG-Block.
    wrapIn(article);
    // 2) Subglossar-Block (ein <div>, kein Collapsible): seine Stufen-H2
    //    werden — wie die HG-Sektionen — zu sichtbar gestapelten, einzeln
    //    ausklappbaren Akkordeon-Kapiteln gewickelt.
    const sgBlock = article.querySelector(".subglossar-block");
    if (sgBlock) wrapIn(sgBlock);

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
