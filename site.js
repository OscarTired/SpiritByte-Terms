(() => {
  const themes = [
    ["amber", "Amber CRT"], ["green", "Green Phosphor"],
    ["synthwave", "Synthwave 84"], ["noir", "IBM Noir"],
    ["commodore", "Commodore 64"],
  ];
  const key = "spiritbyte-legal-theme";
  const english = document.documentElement.lang === "en";
  const apply = (value) => {
    if (!themes.some(([id]) => id === value)) return;
    document.documentElement.dataset.theme = value;
    document.querySelector('meta[name="theme-color"]').content =
      getComputedStyle(document.documentElement).getPropertyValue("--bg").trim();
  };
  const container = document.createElement("div");
  container.className = "appearance";
  const label = document.createElement("label");
  label.htmlFor = "palette";
  label.textContent = english ? "Reading palette" : "Paleta de lectura";
  const select = document.createElement("select");
  select.id = "palette";
  for (const [id, name] of themes) select.add(new Option(name, id));
  try { apply(localStorage.getItem(key)); } catch { /* Reading remains available without storage. */ }
  select.value = document.documentElement.dataset.theme;
  select.addEventListener("change", () => {
    apply(select.value);
    try { localStorage.setItem(key, select.value); } catch { /* Palette still changes for this visit. */ }
  });
  container.append(label, select);
  document.querySelector(".site-header").after(container);
  document.querySelectorAll("[data-print]").forEach((button) => {
    button.hidden = false;
    button.addEventListener("click", () => window.print());
  });
  document.querySelectorAll("[data-language]").forEach((link) => {
    link.addEventListener("click", () => {
      // Matching section IDs keep the reader at the same section in either language.
      link.href = link.getAttribute("href").split("#")[0] + window.location.hash;
    });
  });
})();
