/* Pin-Toggle für die linke Navigation.
 *
 * Fügt im Header einen Knopf ein, der die Navigations-Spalte „anheftet":
 * Statt als Overlay-Drawer (Hamburger) bleibt sie dann permanent links
 * stehen und der Inhalt rückt daneben (siehe extra.css, html.nav-pinned).
 * Der Zustand wird in localStorage gemerkt und beim Laden wiederhergestellt.
 *
 * Material-Instant-Loading: Bei aktivem navigation.instant tauscht Material
 * den Seiteninhalt per XHR aus, ohne das Script neu auszuführen. Das globale
 * Observable `document$` emittiert bei jedem (auch instant-) Seitenwechsel —
 * daran hängen wir das Wiederherstellen + erneute Einhängen des Knopfes.
 */
(function () {
  "use strict";

  var KEY = "holzbau-nav-pinned";
  var PIN_SVG =
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">' +
    '<path d="M16,12V4H17V2H7V4H8V12L6,14V16H11.2V22H12.8V16H18V14L16,12Z"/>' +
    "</svg>";

  function isPinned() {
    return localStorage.getItem(KEY) === "1";
  }

  function applyState() {
    var on = isPinned();
    document.documentElement.classList.toggle("nav-pinned", on);
    var btn = document.getElementById("nav-pin-toggle");
    if (btn) {
      btn.setAttribute("aria-pressed", on ? "true" : "false");
      btn.title = on ? "Menü lösen" : "Menü anheften";
    }
  }

  function ensureButton() {
    if (document.getElementById("nav-pin-toggle")) return;
    var header = document.querySelector(".md-header__inner");
    if (!header) return;
    var btn = document.createElement("button");
    btn.id = "nav-pin-toggle";
    btn.type = "button";
    btn.className = "md-header__button md-icon nav-pin-toggle";
    btn.setAttribute("aria-label", "Menü anheften");
    btn.innerHTML = PIN_SVG;
    btn.addEventListener("click", function () {
      localStorage.setItem(KEY, isPinned() ? "0" : "1");
      applyState();
    });
    // Direkt nach dem Hamburger-Knopf einsortieren, sonst ans Ende.
    var hamburger = header.querySelector('label[for="__drawer"]');
    if (hamburger && hamburger.parentNode === header) {
      header.insertBefore(btn, hamburger.nextSibling);
    } else {
      header.appendChild(btn);
    }
  }

  function init() {
    ensureButton();
    applyState();
  }

  // Klasse so früh wie möglich setzen (vermeidet Aufblitzen des Overlays).
  if (isPinned()) document.documentElement.classList.add("nav-pinned");

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(init);
  } else if (document.readyState !== "loading") {
    init();
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
