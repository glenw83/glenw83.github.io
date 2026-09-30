(() => {
  const viewer = document.querySelector("[data-curvature-viewer]");
  if (!viewer) return;

  const controls = viewer.querySelector(".sd-curvature-controls");
  const buttons = [...controls.querySelectorAll("button")];
  const frames = [...viewer.querySelectorAll(".sd-curvature-frame")];
  const status = viewer.querySelector(".sd-curvature-status");
  const descriptions = ["Connected neck", "Narrowing neck", "Further thinning", "Very thin neck", "After separation"];

  function showStage(index) {
    frames.forEach((frame, i) => {
      frame.hidden = i !== index;
      buttons[i].setAttribute("aria-pressed", String(i === index));
    });
    status.textContent = `Stage ${index + 1} of ${frames.length} · ${descriptions[index]}`;
  }

  buttons.forEach((button, index) => button.addEventListener("click", () => showStage(index)));
  showStage(0);
  controls.hidden = false;
  status.hidden = false;
})();
